"""Valida las notas que cambian en un Pull Request.

Revisa en los archivos agregados o modificados:
- Frontmatter con tipo, fecha y resumen (y autor en notas nuevas).
- Fecha con formato AAAA-MM-DD.
- Enlaces [[...]] que apunten a notas existentes.
- Que nadie haya editado a mano la sección automática de un _index.md.
- Que cada quien solo modifique archivos de sus áreas, según .github/CODEOWNERS
  y .github/integrantes.txt. Fuera de ellas solo puede crear sus propias
  propuestas (propuesta-<tema>-<rama>.md) y sus sesiones
  (sesiones/AAAA-MM-DD-<rama>-<tema>.md).
Uso: python scripts/validar_vault.py --base origin/main --rama <rama-del-PR>
"""
from pathlib import Path
import argparse
import fnmatch
import re
import subprocess
import sys

RAIZ = Path(__file__).resolve().parent.parent
EXCLUIDOS = {"CLAUDE.md", "README.md"}
INICIO = "<!-- indice-automatico:inicio -->"
FIN = "<!-- indice-automatico:fin -->"
ENLACE = re.compile(r"\[\[([^\]]+)\]\]")
RAMAS_ADMIN = {"juan-pablo"}  # pueden modificar todo el vault
PROYECTO = "tec/data-steward-agentico/"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, check=True).stdout


def archivos_cambiados(base: str) -> list[tuple[str, str]]:
    salida = git("diff", "--name-status", "--diff-filter=AM", f"{base}...HEAD")
    cambios = []
    for linea in salida.splitlines():
        estado, ruta = linea.split("\t", 1)
        if ruta.endswith(".md") and ruta.startswith("tec/") and Path(ruta).name not in EXCLUIDOS:
            cambios.append((estado, ruta))
    return cambios


def frontmatter(texto: str) -> dict | None:
    m = re.match(r"^---\n(.*?)\n---", texto, re.DOTALL)
    if not m:
        return None
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = valor.strip()
    return datos


def enlace_existe(destino: str) -> bool:
    destino = destino.replace("\\|", "|").split("|")[0].split("#")[0].strip()
    if not destino:
        return True
    if (RAIZ / destino).exists() or (RAIZ / f"{destino}.md").exists():
        return True
    if "/" not in destino:  # enlace corto: se busca por nombre en todo el vault
        return any(RAIZ.rglob(f"{destino}.md")) or any(RAIZ.rglob(destino))
    return False


def seccion_automatica(texto: str) -> str:
    if INICIO in texto and FIN in texto:
        return texto.split(INICIO, 1)[1].split(FIN, 1)[0]
    return ""


def validar(base: str) -> list[str]:
    errores = []
    ancestro = git("merge-base", base, "HEAD").strip()
    for estado, ruta in archivos_cambiados(base):
        texto = (RAIZ / ruta).read_text(encoding="utf-8")
        fm = frontmatter(texto)
        requeridos = ["tipo", "fecha", "resumen"] + (["autor"] if estado == "A" else [])
        if fm is None:
            errores.append(f"{ruta}: falta el frontmatter (bloque entre ---).")
        else:
            for campo in requeridos:
                if not fm.get(campo):
                    errores.append(f"{ruta}: falta el campo '{campo}' en el frontmatter.")
            if fm.get("fecha") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm["fecha"]):
                errores.append(f"{ruta}: la fecha debe tener formato AAAA-MM-DD.")
        for destino in ENLACE.findall(texto):
            if not enlace_existe(destino):
                errores.append(f"{ruta}: enlace roto [[{destino}]].")
        if Path(ruta).name == "_index.md" and estado == "M":
            anterior = git("show", f"{ancestro}:{ruta}")
            if seccion_automatica(anterior) != seccion_automatica(texto):
                errores.append(f"{ruta}: se editó a mano la sección automática; deshaz ese cambio.")
    return errores


def usuarios_a_ramas() -> dict[str, str]:
    ramas = {}
    for linea in (RAIZ / ".github/integrantes.txt").read_text(encoding="utf-8").splitlines():
        partes = linea.split()
        if len(partes) == 2 and not linea.startswith("#"):
            ramas[partes[1].lower()] = partes[0]
    return ramas


def reglas_codeowners() -> list[tuple[str, list[str]]]:
    reglas = []
    for linea in (RAIZ / ".github/CODEOWNERS").read_text(encoding="utf-8").splitlines():
        linea = linea.split("#", 1)[0].strip()
        if linea:
            patron, *duenos = linea.split()
            reglas.append((patron, [d.lstrip("@").lower() for d in duenos]))
    return reglas


def coincide(patron: str, ruta: str) -> bool:
    if patron == "*":
        return True
    patron = patron.lstrip("/")
    if patron.endswith("/"):
        return ruta.startswith(patron)
    return fnmatch.fnmatch(ruta, patron)


def ramas_duenas(ruta: str, reglas, ramas) -> set[str]:
    duenos: list[str] = []
    for patron, usuarios in reglas:  # en CODEOWNERS gana la última regla que coincide
        if coincide(patron, ruta):
            duenos = usuarios
    return {ramas[u] for u in duenos if u in ramas}


def cambios_con_estado(base: str) -> list[tuple[str, str]]:
    cambios = []
    for linea in git("diff", "--name-status", "-M", f"{base}...HEAD").splitlines():
        estado, *rutas = linea.split("\t")
        if estado.startswith("R"):  # un renombre es borrar la ruta vieja y crear la nueva
            cambios += [("D", rutas[0]), ("A", rutas[1])]
        else:
            cambios.append((estado[0], rutas[0]))
    return cambios


def permitido_fuera_de_area(estado: str, ruta: str, rama: str) -> bool:
    if estado not in ("A", "M") or not ruta.startswith(PROYECTO):
        return False
    nombre = Path(ruta).name
    if nombre.startswith("propuesta-") and nombre.endswith(f"-{rama}.md"):
        return True
    es_sesion = ruta.startswith(f"{PROYECTO}sesiones/")
    return es_sesion and re.fullmatch(rf"\d{{4}}-\d{{2}}-\d{{2}}-{re.escape(rama)}-.+\.md", nombre) is not None


def validar_areas(base: str, rama: str) -> list[str]:
    if not rama or rama in RAMAS_ADMIN:
        return []
    ramas = usuarios_a_ramas()
    if rama not in ramas.values():
        return [f"La rama '{rama}' no está en .github/integrantes.txt; abre el PR desde tu rama de integrante."]
    reglas = reglas_codeowners()
    errores = []
    for estado, ruta in cambios_con_estado(base):
        if rama in ramas_duenas(ruta, reglas, ramas) or permitido_fuera_de_area(estado, ruta, rama):
            continue
        duenas = ", ".join(sorted(ramas_duenas(ruta, reglas, ramas))) or "juan-pablo"
        accion = {"A": "creaste", "M": "modificaste", "D": "borraste"}.get(estado, "cambiaste")
        errores.append(
            f"{ruta}: {accion} un archivo que no es de tu área (dueños: {duenas}). "
            f"Deshaz ese cambio y, si hace falta, crea una propuesta en esa carpeta: "
            f"propuesta-<tema>-{rama}.md"
        )
    return errores


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--rama", default="", help="rama de origen del PR")
    args = parser.parse_args()
    errores = validar(args.base) + validar_areas(args.base, args.rama)
    if errores:
        print("Se encontraron problemas:\n")
        print("\n".join(f"- {e}" for e in errores))
        return 1
    print("Todo en orden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
