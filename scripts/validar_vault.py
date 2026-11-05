"""Valida las notas que cambian en un Pull Request.

Revisa en los archivos agregados o modificados:
- Frontmatter con tipo, fecha y resumen (y autor en notas nuevas).
- Fecha con formato AAAA-MM-DD.
- Enlaces [[...]] que apunten a notas existentes.
- Que nadie haya editado a mano la sección automática de un _index.md.
Uso: python scripts/validar_vault.py --base origin/main
"""
from pathlib import Path
import argparse
import re
import subprocess
import sys

RAIZ = Path(__file__).resolve().parent.parent
EXCLUIDOS = {"CLAUDE.md", "README.md"}
INICIO = "<!-- indice-automatico:inicio -->"
FIN = "<!-- indice-automatico:fin -->"
ENLACE = re.compile(r"\[\[([^\]]+)\]\]")


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    errores = validar(parser.parse_args().base)
    if errores:
        print("Se encontraron problemas:\n")
        print("\n".join(f"- {e}" for e in errores))
        return 1
    print("Todo en orden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
