"""Genera tec/data-steward-agentico/novedades.md a partir del historial de main.

Lista los últimos cambios (un cambio = un PR fusionado o un push directo),
agrupados por fecha, con liga a cada nota y su resumen. Lo lee primero
cualquier LLM que trabaje en el vault. Nadie lo edita a mano.
Uso: python scripts/generar_novedades.py
"""
from collections import OrderedDict, defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re
import subprocess
import sys

RAIZ = Path(__file__).resolve().parent.parent
PROYECTO = "tec/data-steward-agentico/"
SALIDA = PROYECTO + "novedades.md"
TAREAS = PROYECTO + "tareas/"  # su estado vive en tareas/_tablero.md, no aquí
MAX_CAMBIOS = 20
MAX_NOTAS_POR_CAMBIO = 6
ZONA = ZoneInfo("America/Mexico_City")
SEP = "\x1f"
ESTADOS = {"A": "Nueva", "M": "Modificada", "D": "Eliminada", "R": "Movida"}
ORDEN_ESTADO = {"A": 0, "R": 1, "M": 2, "D": 3}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, check=True).stdout


def frontmatter(ruta: str) -> dict:
    archivo = RAIZ / ruta
    if not archivo.exists():
        return {}
    m = re.match(r"^---\n(.*?)\n---", archivo.read_text(encoding="utf-8"), re.DOTALL)
    datos = {}
    if m:
        for linea in m.group(1).splitlines():
            if ":" in linea:
                clave, valor = linea.split(":", 1)
                datos[clave.strip()] = valor.strip().strip('"')
    return datos


def commits_de_main() -> list[dict]:
    formato = SEP.join(["%H", "%P", "%cI", "%an", "%s", "%b"]) + "\x1e"
    salida = git("log", "--first-parent", f"--format={formato}", "HEAD")
    commits = []
    for bloque in salida.split("\x1e"):
        bloque = bloque.strip("\n")
        if not bloque:
            continue
        sha, padres, fecha, autor, asunto, cuerpo = (bloque.split(SEP) + [""] * 6)[:6]
        commits.append({
            "sha": sha, "padre": padres.split()[0] if padres else None,
            "fecha": datetime.fromisoformat(fecha).astimezone(ZONA),
            "autor": autor, "asunto": asunto.strip(), "cuerpo": cuerpo.strip(),
        })
    return commits


def es_del_bot(c: dict) -> bool:
    return c["autor"] == "vault-bot" or "[skip ci]" in c["asunto"]


def titulo_pr_y_autor(c: dict) -> tuple[str, str, str]:
    m = re.match(r"Merge pull request #(\d+) from [^/]+/(\S+)", c["asunto"])
    if m:
        titulo = c["cuerpo"].splitlines()[0] if c["cuerpo"] else c["asunto"]
        return titulo, f"PR #{m.group(1)}", m.group(2)
    m = re.search(r"\(#(\d+)\)$", c["asunto"])
    if m:
        return c["asunto"][: m.start()].strip(), f"PR #{m.group(1)}", c["autor"]
    return c["asunto"], "push directo", c["autor"]


def archivos_cambiados(c: dict) -> list[tuple[str, str]]:
    if c["padre"]:
        salida = git("diff", "--name-status", "-M", c["padre"], c["sha"])
    else:
        salida = git("show", "--name-status", "--format=", "-M", c["sha"])
    cambios = []
    for linea in salida.splitlines():
        estado, *rutas = linea.split("\t")
        cambios.append((estado[0], rutas[-1]))
    return [(e, r) for e, r in cambios if r != SALIDA]


def liga(ruta: str) -> str:
    destino = ruta[:-3] if ruta.endswith(".md") else ruta
    return f"[[{destino}|{Path(destino).name}]]"


def lineas_de_notas(notas: list[tuple[str, str]]) -> list[str]:
    def prioridad(nota):
        estado, ruta = nota
        es_decision = Path(ruta).name.startswith("decision-")
        return (0 if es_decision else 1, ORDEN_ESTADO.get(estado, 9), ruta)

    notas = sorted(notas, key=prioridad)
    visibles, resto = notas[:MAX_NOTAS_POR_CAMBIO], notas[MAX_NOTAS_POR_CAMBIO:]
    lineas = []
    for estado, ruta in visibles:
        etiqueta = ESTADOS.get(estado, "Cambiada")
        if estado == "D":
            lineas.append(f"- **{etiqueta}:** `{ruta}`")
            continue
        if not (RAIZ / ruta).exists():
            lineas.append(f"- **{etiqueta}:** `{ruta}` (ya no existe)")
            continue
        lineas.append(f"- **{etiqueta}:** {liga(ruta)}")
        resumen = frontmatter(ruta).get("resumen")
        if resumen:
            lineas.append(f"  {resumen}")
    if resto:
        carpetas = sorted({Path(r).parent.as_posix().replace(PROYECTO, "") + "/" for _, r in resto})
        lineas.append(f"- **{len(resto)} notas más** en {', '.join(f'`{c}`' for c in carpetas)}")
    return lineas


def generar() -> str:
    cambios = []
    for c in commits_de_main():
        if es_del_bot(c):
            continue
        archivos = archivos_cambiados(c)
        notas = [(e, r) for e, r in archivos
                 if r.startswith(PROYECTO) and r.endswith(".md") and not r.startswith(TAREAS)]
        repo = [r for e, r in archivos if not r.startswith(PROYECTO)]
        if notas or repo:
            cambios.append((c, notas, repo))
        if len(cambios) == MAX_CAMBIOS:
            break

    por_fecha: "OrderedDict[str, list]" = OrderedDict()
    for c, notas, repo in cambios:
        por_fecha.setdefault(c["fecha"].strftime("%Y-%m-%d"), []).append((c, notas, repo))

    ultima = next(iter(por_fecha), datetime.now(ZONA).strftime("%Y-%m-%d"))
    lineas = [
        "---",
        "tipo: novedades",
        f"fecha: {ultima}",
        "autor: vault-bot",
        f"resumen: Los últimos {MAX_CAMBIOS} cambios que llegaron a main, con liga a cada nota. Léelo al empezar.",
        "---",
        "# Novedades del vault",
        "",
        "_Lo genera GitHub Actions en cada cambio a `main`. No lo edites a mano._",
        "",
        f"Muestra los últimos {MAX_CAMBIOS} cambios, del más reciente al más antiguo. "
        "Si una novedad toca lo que te piden, abre la nota enlazada antes de responder. "
        "Para cambios más antiguos, consulta el historial de Git de `main`.",
        "",
        "El avance de las tareas no aparece aquí: está en "
        "[[tec/data-steward-agentico/tareas/_tablero|el tablero de tareas]].",
    ]
    if not cambios:
        lineas += ["", "_Todavía no hay cambios._"]
    for fecha, grupo in por_fecha.items():
        lineas += ["", f"## {fecha}"]
        for c, notas, repo in grupo:
            titulo, origen, autor = titulo_pr_y_autor(c)
            lineas += ["", f"### {titulo} · {autor} · {origen}"]
            lineas += lineas_de_notas(notas)
            if repo:
                mostrados = ", ".join(f"`{r}`" for r in sorted(repo)[:5])
                extra = f" y {len(repo) - 5} más" if len(repo) > 5 else ""
                lineas.append(f"- **Cambios en el repo:** {mostrados}{extra}")
    return "\n".join(lineas) + "\n"


def main() -> int:
    destino = RAIZ / SALIDA
    nuevo = generar()
    if destino.exists() and destino.read_text(encoding="utf-8") == nuevo:
        print("Novedades al día.")
        return 0
    destino.write_text(nuevo, encoding="utf-8")
    print(f"Actualizado: {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
