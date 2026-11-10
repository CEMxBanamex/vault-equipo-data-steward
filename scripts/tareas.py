"""Lee y valida las tareas de tec/data-steward-agentico/tareas/<rama>.md.

Formato de una tarea (una línea):
  - [ ] **S1-01** Título · vence: 2026-11-10 · apoyo: mario · depende: S1-07, S1-08 · listo cuando: <criterio>

Estados: [ ] pendiente, [/] en proceso, [x] listo, [!] bloqueado (requiere "· bloqueo: <motivo>").
Campos obligatorios: vence (AAAA-MM-DD) y listo cuando. Opcionales: apoyo, depende, bloqueo, nota.
IDs: S<semana>-<nn> (los asigna juan-pablo) o <rama>-<nn> (tareas propias de cada quien).
Un #hito en el título marca la tarea como hito del equipo.

Lo usan validar_vault.py, publicar_tareas.py y generar_tablero.py.
Uso directo: python scripts/tareas.py  (valida todos los archivos de tareas)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
PROYECTO = "tec/data-steward-agentico/"
CARPETA = PROYECTO + "tareas/"
ESPECIALES = {"_index.md", "_tablero.md"}

ESTADOS = {" ": "pendiente", "/": "en proceso", "x": "listo", "X": "listo", "!": "bloqueado"}
CAMPOS = {"vence", "apoyo", "depende", "listo cuando", "bloqueo", "nota"}
OBLIGATORIOS = ("vence", "listo cuando")

NOMBRES = {
    "juan-pablo": "Juan Pablo",
    "iris": "Iris",
    "mario": "Mario",
    "carlos-delgado": "Carlos Delgado",
    "carlos-ramos": "Carlos Ramos",
    "yael": "Yael",
    "mauricio": "Mauricio",
}
FRENTES = {
    "Infraestructura y CI/CD": ["juan-pablo"],
    "Datos": ["iris", "mario"],
    "Agentes y modelos": ["carlos-delgado", "carlos-ramos"],
    "Frontend": ["yael", "mauricio"],
}

PARECE_TAREA = re.compile(r"^\s*- \[(.)\]")
LINEA = re.compile(r"^\s*- \[(.)\] \*\*([A-Za-z0-9-]+)\*\*\s+(.+?)\s*$")
FECHA = re.compile(r"\d{4}-\d{2}-\d{2}")


@dataclass
class Tarea:
    id: str
    estado: str
    titulo: str
    campos: dict
    rama: str
    semana: str
    archivo: str
    linea: int
    depende: list = field(default_factory=list)
    apoyo: list = field(default_factory=list)

    @property
    def hito(self) -> bool:
        return "#hito" in self.titulo

    @property
    def titulo_limpio(self) -> str:
        return re.sub(r"\s*#hito\b", "", self.titulo).strip()

    @property
    def vence(self) -> date | None:
        try:
            return date.fromisoformat(self.campos.get("vence", ""))
        except ValueError:
            return None


def ramas_integrantes() -> list[str]:
    ramas = []
    for linea in (RAIZ / ".github/integrantes.txt").read_text(encoding="utf-8").splitlines():
        partes = linea.split()
        if len(partes) == 2 and not linea.startswith("#"):
            ramas.append(partes[0])
    return ramas


def es_archivo_de_tareas(ruta: str) -> bool:
    return ruta.startswith(CARPETA) and ruta.endswith(".md") and Path(ruta).name not in ESPECIALES


def leer(texto: str, ruta: str) -> tuple[list[Tarea], list[str]]:
    """Devuelve las tareas del archivo y los errores de formato de cada línea."""
    rama = Path(ruta).stem
    tareas, errores = [], []
    semana = ""
    en_frontmatter = texto.startswith("---\n")
    for n, linea in enumerate(texto.splitlines(), start=1):
        if en_frontmatter:
            if n > 1 and linea.strip() == "---":
                en_frontmatter = False
            continue
        if linea.startswith("## "):
            semana = linea[3:].strip()
            continue
        if not PARECE_TAREA.match(linea):
            continue
        donde = f"{ruta}:{n}"
        m = LINEA.match(linea)
        if not m:
            errores.append(f"{donde}: la tarea debe empezar con '- [ ] **ID** Título'.")
            continue
        marca, id_, resto = m.groups()
        if marca not in ESTADOS:
            errores.append(f"{donde}: estado '[{marca}]' no válido; usa [ ], [/], [x] o [!].")
            continue
        partes = [p.strip() for p in resto.split(" · ")]
        titulo, campos = partes[0], {}
        for p in partes[1:]:
            if ":" not in p:
                errores.append(f"{donde}: '{p}' debe ser 'campo: valor'.")
                continue
            clave, valor = (s.strip() for s in p.split(":", 1))
            clave = clave.lower()
            if clave not in CAMPOS:
                errores.append(f"{donde}: campo '{clave}' desconocido; usa {', '.join(sorted(CAMPOS))}.")
                continue
            campos[clave] = valor
        t = Tarea(id_, ESTADOS[marca], titulo, campos, rama, semana, ruta, n)
        t.depende = [d.strip() for d in campos.get("depende", "").split(",") if d.strip()]
        t.apoyo = [a.strip() for a in campos.get("apoyo", "").split(",") if a.strip() and a.strip() != "—"]
        tareas.append(t)
    return tareas, errores


def validar_tareas(tareas: list[Tarea]) -> list[str]:
    """Errores de contenido de cada tarea y entre tareas (IDs únicos, dependencias)."""
    ramas = set(ramas_integrantes())
    errores = []
    por_id: dict[str, Tarea] = {}
    for t in tareas:
        donde = f"{t.archivo}:{t.linea} ({t.id})"
        if t.rama not in ramas:
            errores.append(f"{t.archivo}: el nombre del archivo debe ser una rama de .github/integrantes.txt.")
        if not (re.fullmatch(r"S\d+-\d{2,}", t.id) or re.fullmatch(rf"{re.escape(t.rama)}-\d+", t.id)):
            errores.append(f"{donde}: el ID debe ser S<semana>-<nn> o {t.rama}-<nn>.")
        for campo in OBLIGATORIOS:
            if not t.campos.get(campo):
                errores.append(f"{donde}: falta '· {campo}: ...'.")
        if t.campos.get("vence") and (not FECHA.fullmatch(t.campos["vence"]) or t.vence is None):
            errores.append(f"{donde}: 'vence' debe ser una fecha AAAA-MM-DD.")
        if t.estado == "bloqueado" and not t.campos.get("bloqueo"):
            errores.append(f"{donde}: una tarea bloqueada [!] necesita '· bloqueo: <motivo>'.")
        for a in t.apoyo:
            if a != "todos" and a not in ramas:
                errores.append(f"{donde}: apoyo '{a}' no es una rama del equipo (o 'todos').")
        por_id.setdefault(t.id, t)
    for id_ in sorted({t.id for t in tareas}):
        mismas = [t for t in tareas if t.id == id_]
        for t in mismas if len(mismas) > 1 else []:
            otras = ", ".join(f"{o.archivo}:{o.linea}" for o in mismas if o is not t)
            errores.append(f"{t.archivo}:{t.linea} ({t.id}): el ID {t.id} está repetido; también en {otras}.")
    for t in tareas:
        for d in t.depende:
            if d not in por_id:
                errores.append(f"{t.archivo}:{t.linea} ({t.id}): depende de {d}, que no existe.")
            elif d == t.id:
                errores.append(f"{t.archivo}:{t.linea} ({t.id}): una tarea no puede depender de sí misma.")
    return errores


def archivos_de_tareas() -> list[Path]:
    carpeta = RAIZ / CARPETA
    if not carpeta.exists():
        return []
    return sorted(p for p in carpeta.glob("*.md") if p.name not in ESPECIALES)


def cargar_todas(reemplazos: dict[str, str] | None = None) -> tuple[list[Tarea], list[str]]:
    """Lee todos los archivos de tareas. 'reemplazos' permite validar un contenido nuevo antes de escribirlo."""
    reemplazos = reemplazos or {}
    rutas = {p.relative_to(RAIZ).as_posix(): p for p in archivos_de_tareas()}
    for ruta in reemplazos:
        rutas.setdefault(ruta, RAIZ / ruta)
    tareas, errores = [], []
    for ruta in sorted(rutas):
        texto = reemplazos.get(ruta)
        if texto is None:
            texto = rutas[ruta].read_text(encoding="utf-8")
        ts, es = leer(texto, ruta)
        tareas += ts
        errores += es
    return tareas, errores + validar_tareas(tareas)


def errores_de(archivos: set[str], errores: list[str]) -> list[str]:
    """Filtra los errores que mencionan alguno de los archivos dados."""
    return [e for e in errores if any(e.startswith(a) for a in archivos)]


def main() -> int:
    _, errores = cargar_todas()
    if errores:
        print("Problemas en las tareas:\n")
        print("\n".join(f"- {e}" for e in errores))
        return 1
    print("Tareas en orden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
