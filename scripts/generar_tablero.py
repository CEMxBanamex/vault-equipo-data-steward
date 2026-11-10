"""Genera tec/data-steward-agentico/tareas/_tablero.md a partir de los archivos de tareas.

Muestra hitos, bloqueadas, vencidas, lo que vence hoy y mañana, lo que se destrabó
y el avance por frente y por persona. Depende de la fecha (Ciudad de México), por eso
corre también en la sincronización programada. Nadie lo edita a mano.
Uso: python scripts/generar_tablero.py [--hoy AAAA-MM-DD]
"""
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
import argparse
import sys

from tareas import FRENTES, NOMBRES, PROYECTO, RAIZ, Tarea, cargar_todas

SALIDA = PROYECTO + "tareas/_tablero.md"
ZONA = ZoneInfo("America/Mexico_City")
ETIQUETA = {"pendiente": "Pendiente", "en proceso": "En proceso", "listo": "Listo", "bloqueado": "Bloqueado"}


def celda(texto: str) -> str:
    return (texto or "").replace("|", "\\|").replace("\n", " ")


def persona(rama: str) -> str:
    return f"[[{PROYECTO}tareas/{rama}\\|{NOMBRES.get(rama, rama)}]]"


def tarea(t: Tarea) -> str:
    return f"**{t.id}** {celda(t.titulo_limpio)}"


def fecha_corta(t: Tarea) -> str:
    return t.vence.strftime("%d/%m") if t.vence else "—"


def barra(listas: int, total: int) -> str:
    if total == 0:
        return "—"
    pct = round(100 * listas / total)
    llenas = round(pct / 10)
    return f"{'▓' * llenas}{'░' * (10 - llenas)} {pct} %"


def conteo(ts: list[Tarea]) -> dict:
    c = {e: 0 for e in ETIQUETA}
    for t in ts:
        c[t.estado] += 1
    return c


def tabla(encabezados: list[str], filas: list[list[str]], vacio: str) -> list[str]:
    if not filas:
        return [vacio]
    lineas = ["| " + " | ".join(encabezados) + " |", "|" + "---|" * len(encabezados)]
    lineas += ["| " + " | ".join(f) + " |" for f in filas]
    return lineas


def semana_en_curso(tareas: list[Tarea], hoy: date) -> str:
    """La semana de la tarea pendiente más próxima a hoy; si no hay, la última."""
    pendientes = sorted((t for t in tareas if t.estado != "listo" and t.vence), key=lambda t: (t.vence < hoy, t.vence))
    if pendientes:
        return pendientes[0].semana
    return tareas[-1].semana if tareas else ""


def generar(hoy: date) -> str:
    tareas, _ = cargar_todas()
    abiertas = [t for t in tareas if t.estado != "listo"]
    estado_de = {t.id: t.estado for t in tareas}
    orden = lambda t: (t.vence or date.max, t.id)
    c = conteo(tareas)
    total = len(tareas)

    lineas = [
        "---",
        "tipo: tablero",
        f"fecha: {hoy.isoformat()}",
        "autor: vault-bot",
        "resumen: Estado de las tareas del equipo (hitos, bloqueos, vencidas, lo próximo y el avance por persona). Léelo al empezar.",
        "---",
        "# Tablero de tareas",
        "",
        "_Lo genera GitHub Actions a partir de los archivos de `tareas/`. No lo edites a mano: marca tus tareas en tu archivo. "
        "Cómo funciona: [[tec/data-steward-agentico/tareas/_index|tareas]]._",
        "",
        f"**Actualizado:** {hoy.isoformat()} (Ciudad de México). **Semana en curso:** {semana_en_curso(tareas, hoy) or '—'}.",
        "",
        f"**Avance general:** {c['listo']} de {total} listas ({barra(c['listo'], total).split(' ', 1)[-1]}) · "
        f"{c['en proceso']} en proceso · {c['bloqueado']} bloqueadas · {c['pendiente']} pendientes.",
    ]

    hitos = sorted((t for t in tareas if t.hito), key=orden)
    lineas += ["", "## Hitos"]
    lineas += tabla(
        ["Hito", "Responsable", "Vence", "Estado"],
        [[tarea(t), persona(t.rama), fecha_corta(t), ETIQUETA[t.estado]] for t in hitos],
        "_Sin hitos marcados._",
    )

    bloqueadas = sorted((t for t in tareas if t.estado == "bloqueado"), key=orden)
    lineas += ["", "## Bloqueadas"]
    lineas += tabla(
        ["Tarea", "Responsable", "Motivo"],
        [[tarea(t), persona(t.rama), celda(t.campos.get("bloqueo", ""))] for t in bloqueadas],
        "_Ninguna._",
    )

    vencidas = sorted((t for t in abiertas if t.vence and t.vence < hoy), key=orden)
    lineas += ["", "## Vencidas"]
    lineas += tabla(
        ["Tarea", "Responsable", "Venció", "Estado"],
        [[tarea(t), persona(t.rama), fecha_corta(t), ETIQUETA[t.estado]] for t in vencidas],
        "_Ninguna._",
    )

    manana = hoy + timedelta(days=1)
    proximas = sorted((t for t in abiertas if t.vence in (hoy, manana)), key=orden)
    lineas += ["", "## Vencen hoy y mañana"]
    lineas += tabla(
        ["Tarea", "Responsable", "Vence", "Estado"],
        [[tarea(t), persona(t.rama), "hoy" if t.vence == hoy else "mañana", ETIQUETA[t.estado]] for t in proximas],
        "_Nada vence hoy ni mañana._",
    )

    destrabadas = sorted(
        (t for t in tareas if t.estado == "pendiente" and t.depende
         and all(estado_de.get(d) == "listo" for d in t.depende)),
        key=orden,
    )
    lineas += ["", "## Se destrabaron", "_Pendientes cuyas dependencias ya están listas: se pueden empezar._", ""]
    lineas += tabla(
        ["Tarea", "Responsable", "Vence", "Dependía de"],
        [[tarea(t), persona(t.rama), fecha_corta(t), ", ".join(t.depende)] for t in destrabadas],
        "_Ninguna por ahora._",
    )

    lineas += ["", "## Avance por frente"]
    filas = []
    for frente, ramas in FRENTES.items():
        ts = [t for t in tareas if t.rama in ramas]
        k = conteo(ts)
        filas.append([frente, str(k["listo"]), str(k["en proceso"]), str(k["bloqueado"]),
                      str(k["pendiente"]), barra(k["listo"], len(ts))])
    lineas += tabla(["Frente", "Listas", "En proceso", "Bloqueadas", "Pendientes", "Avance"], filas, "")

    lineas += ["", "## Avance por persona"]
    filas = []
    for rama in NOMBRES:
        ts = [t for t in tareas if t.rama == rama]
        k = conteo(ts)
        siguiente = min((t for t in ts if t.estado != "listo"), key=orden, default=None)
        filas.append([persona(rama), str(k["listo"]), str(k["en proceso"]), str(k["bloqueado"]),
                      str(k["pendiente"]), barra(k["listo"], len(ts)),
                      tarea(siguiente) if siguiente else "—"])
    lineas += tabla(["Persona", "Listas", "En proceso", "Bloqueadas", "Pendientes", "Avance", "Lo siguiente"], filas, "")
    return "\n".join(lineas) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hoy", help="fecha AAAA-MM-DD (por defecto, hoy en la Ciudad de México)")
    args = parser.parse_args()
    hoy = date.fromisoformat(args.hoy) if args.hoy else datetime.now(ZONA).date()
    destino = RAIZ / SALIDA
    if not destino.parent.exists():
        print("No existe la carpeta de tareas; nada que generar.")
        return 0
    nuevo = generar(hoy)
    if destino.exists() and destino.read_text(encoding="utf-8") == nuevo:
        print("Tablero al día.")
        return 0
    destino.write_text(nuevo, encoding="utf-8")
    print(f"Actualizado: {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
