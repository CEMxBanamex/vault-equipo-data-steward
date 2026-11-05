"""Regenera la sección automática de cada _index.md del vault.

Lista las notas hermanas de cada _index.md a partir de su frontmatter.
Solo toca el texto entre los marcadores; el resto del índice no cambia.
Uso: python scripts/generar_indices.py
"""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
CARPETA_PROYECTO = RAIZ / "tec"
INICIO = "<!-- indice-automatico:inicio -->"
FIN = "<!-- indice-automatico:fin -->"


def leer_frontmatter(ruta: Path) -> dict:
    texto = ruta.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", texto, re.DOTALL)
    if not m:
        return {}
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = valor.strip().strip('"')
    return datos


def celda(valor: str) -> str:
    return (valor or "").replace("|", "\\|").replace("\n", " ")


def seccion_para(indice: Path) -> str:
    carpeta = indice.parent
    filas = []
    for nota in sorted(carpeta.glob("*.md")):
        if nota.name == "_index.md":
            continue
        fm = leer_frontmatter(nota)
        ruta = nota.relative_to(RAIZ).with_suffix("").as_posix()
        filas.append((fm.get("tipo", ""), fm.get("fecha", ""), nota.stem, ruta, fm))
    filas.sort(key=lambda f: (f[0], f[1], f[2]))
    lineas = [
        INICIO,
        "## Índice automático",
        "_No edites esta sección: la regenera GitHub Actions en cada cambio a main._",
        "",
    ]
    if not filas:
        lineas.append("_Sin notas en esta área todavía._")
    else:
        lineas += ["| Nota | Tipo | Autor | Fecha | Resumen |", "|---|---|---|---|---|"]
        for tipo, fecha, nombre, ruta, fm in filas:
            lineas.append(
                f"| [[{ruta}\\|{nombre}]] | {celda(tipo)} | {celda(fm.get('autor', ''))} "
                f"| {celda(fecha)} | {celda(fm.get('resumen', ''))} |"
            )
    lineas.append(FIN)
    return "\n".join(lineas)


def actualizar(indice: Path) -> bool:
    original = indice.read_text(encoding="utf-8")
    nueva = seccion_para(indice)
    if INICIO in original and FIN in original:
        antes = original.split(INICIO)[0]
        despues = original.split(FIN, 1)[1]
        texto = antes + nueva + despues
    else:
        texto = original.rstrip("\n") + "\n\n" + nueva + "\n"
    if texto != original:
        indice.write_text(texto, encoding="utf-8")
        return True
    return False


def main() -> int:
    cambiados = [str(i.relative_to(RAIZ)) for i in sorted(CARPETA_PROYECTO.rglob("_index.md")) if actualizar(i)]
    for c in cambiados:
        print(f"Actualizado: {c}")
    if not cambiados:
        print("Índices al día.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
