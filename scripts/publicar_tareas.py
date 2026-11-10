"""Publica en main el archivo de tareas de cada integrante, sin Pull Request.

Para cada rama de .github/integrantes.txt toma tec/data-steward-agentico/tareas/<rama>.md
de origin/<rama> y, si cambió, lo copia a main. Es seguro porque ese archivo solo lo
edita su dueño. Solo publica cuando:
- La rama ya tiene la última versión de main de ese archivo (si juan-pablo agregó
  tareas en main, primero se propagan a la rama; así nunca se pisan).
- El archivo es válido (frontmatter, formato de las tareas e IDs) y no contiene secretos.
Si no es válido, abre (o mantiene) un issue para esa persona; cuando se corrige, lo cierra.
Corre desde main en sincronizar.yml, antes de regenerar índices y tablero.
Uso: python scripts/publicar_tareas.py   (requiere GH_TOKEN para los issues)
"""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from tareas import CARPETA, RAIZ, cargar_todas, errores_de

TITULO_ISSUE = "Tus tareas no se pudieron publicar ({rama})"


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, check=check)


def gh(*args: str) -> str:
    if not shutil.which("gh"):
        return ""
    r = subprocess.run(["gh", *args], cwd=RAIZ, capture_output=True, text=True)
    return r.stdout.strip()


def integrantes() -> list[tuple[str, str]]:
    filas = []
    for linea in (RAIZ / ".github/integrantes.txt").read_text(encoding="utf-8").splitlines():
        partes = linea.split()
        if len(partes) == 2 and not linea.startswith("#"):
            filas.append((partes[0], partes[1]))
    return filas


def frontmatter_valido(texto: str, ruta: str) -> list[str]:
    m = re.match(r"^---\n(.*?)\n---", texto, re.DOTALL)
    if not m:
        return [f"{ruta}: falta el frontmatter (bloque entre ---)."]
    campos = {l.split(":", 1)[0].strip() for l in m.group(1).splitlines() if ":" in l}
    return [f"{ruta}: falta el campo '{c}' en el frontmatter." for c in ("tipo", "fecha", "resumen") if c not in campos]


def secretos(texto: str) -> list[str]:
    binario = shutil.which("gitleaks") or (str(RAIZ / "gitleaks") if (RAIZ / "gitleaks").exists() else None)
    if not binario:
        return []
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "tareas.md").write_text(texto, encoding="utf-8")
        r = subprocess.run([binario, "detect", "--no-git", "--source", tmp, "--redact", "--no-banner"],
                           capture_output=True, text=True)
    return ["Se detectó algo que parece una credencial o un token; quítalo del archivo."] if r.returncode != 0 else []


def issue_abierto(rama: str) -> str:
    titulo = TITULO_ISSUE.format(rama=rama)
    return gh("issue", "list", "--state", "open", "--search", f'"{titulo}" in:title', "--json", "number",
              "--jq", ".[0].number // empty")


def avisar(rama: str, usuario: str, errores: list[str]) -> None:
    print(f"::warning::No se publicaron las tareas de '{rama}':\n" + "\n".join(errores))
    if issue_abierto(rama):
        return
    cuerpo = (
        f"El Action no pudo publicar `{CARPETA}{rama}.md` de tu rama en `main` porque:\n\n"
        + "\n".join(f"- {e}" for e in errores)
        + "\n\n**Cómo resolverlo:** corrige esas líneas en tu archivo de tareas, en tu rama. "
        "El formato está en `tec/data-steward-agentico/tareas/_index.md`. "
        "En la siguiente corrida (cada 15 min) se publica solo y este issue se cierra."
    )
    titulo = TITULO_ISSUE.format(rama=rama)
    if not gh("issue", "create", "--title", titulo, "--body", cuerpo, "--assignee", usuario):
        gh("issue", "create", "--title", titulo, "--body", cuerpo)


def cerrar_aviso(rama: str) -> None:
    numero = issue_abierto(rama)
    if numero:
        gh("issue", "close", numero, "--comment", "Tus tareas ya se publicaron en main. ¡Gracias!")


def publicar(rama: str, usuario: str) -> bool:
    ruta = f"{CARPETA}{rama}.md"
    if git("ls-remote", "--exit-code", "--heads", "origin", rama, check=False).returncode != 0:
        return False
    en_rama = git("show", f"origin/{rama}:{ruta}", check=False)
    if en_rama.returncode != 0:
        return False  # la rama todavía no tiene su archivo de tareas
    nuevo = en_rama.stdout
    destino = RAIZ / ruta
    actual = destino.read_text(encoding="utf-8") if destino.exists() else None
    if nuevo == actual:
        cerrar_aviso(rama)
        return False

    ultimo = git("log", "-1", "--format=%H", "HEAD", "--", ruta).stdout.strip()
    if ultimo and git("merge-base", "--is-ancestor", ultimo, f"origin/{rama}", check=False).returncode != 0:
        print(f"'{rama}': main tiene cambios en sus tareas que su rama aún no tiene; se publica después de propagar.")
        return False

    _, errores = cargar_todas({ruta: nuevo})
    errores = frontmatter_valido(nuevo, ruta) + errores_de({ruta}, errores) + secretos(nuevo)
    if errores:
        avisar(rama, usuario, errores)
        return False

    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(nuevo, encoding="utf-8")
    git("add", ruta)
    git("commit", "-m", f"chore: publicar tareas de {rama} [skip ci]")
    cerrar_aviso(rama)
    print(f"OK: tareas de '{rama}' publicadas en main.")
    return True


def main() -> int:
    git("fetch", "origin", "--prune")
    publicadas = [rama for rama, usuario in integrantes() if publicar(rama, usuario)]
    print(f"Tareas publicadas: {', '.join(publicadas) if publicadas else 'ninguna'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
