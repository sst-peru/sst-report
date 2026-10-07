"""Regenera la seccion 3.3 Product Backlog del README.

Lee la columna Estado de las tablas de historias y arma una tabla por sprint, mas la
tabla del backlog pendiente. Los sprints se alinean con los cuatro hitos del curso,
cuyas semanas fija el enunciado del trabajo final.
"""
import datetime
import re
from pathlib import Path

from ubicaciones import ubicacion

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

RUTA = Path(__file__).resolve().parent.parent / "README.md"

INICIO_CICLO = datetime.date(2026, 8, 24)  # lunes de la semana 1 del ciclo 2026-20

# Sprint: (hito, semana inicial, semana final)
HITOS = {
    "Sprint 1": ("Primer hito — AVANCE 1 · Sprint Review", 1, 4),
    "Sprint 2": ("Segundo hito — TRABAJO PARCIAL · Stage Review", 5, 7),
    "Sprint 3": ("Tercer hito — AVANCE 2 · Sprint Review", 8, 12),
    "Sprint 4": ("Cuarto hito — TB2 · Release Review", 13, 15),
}

ALCANCE = {
    "Sprint 1": "El ciclo de vida del hallazgo",
    "Sprint 2": "Operación sin conexión, evidencia y experimento A/B",
    "Sprint 3": "Cuentas, matriz IPERC y control de EPP",
    "Sprint 4": "Inspecciones, comité de SST y evidencia exportable",
}

ORDEN = ["Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4"]

# Prioridad dentro de cada sprint, en el orden en que se construyo.
PRIORIDAD = [
    "US02", "US06", "US07", "US08", "US13", "US43", "US70", "US14", "US16", "US15",
    "US17", "US18", "US09", "US35", "US50", "US49", "US10", "US11", "US12", "US44",
    "US45", "US46", "US47", "US48", "US51", "US38", "US39", "US40", "US64", "US01",
    "US03", "US05", "US04", "US41", "US42", "US19", "US20", "US21", "US22", "US52",
    "US53", "US54", "US23", "US24", "US25", "US26", "US55", "US27", "US28", "US29",
    "US56", "US36", "US57", "US30", "US31", "US32", "US33", "US34", "US58", "US59",
    "US60", "US37", "US61", "US62", "US63", "US65", "US66", "US67", "US68", "US69",
    "TS02", "TS07", "TS05", "TS06", "TS01", "TS13", "TS03", "TS08", "TS09", "TS10",
    "TS11", "TS12", "TS04", "TS14", "TS15", "TS16",
]

PUNTOS = {
    "US01": 5, "US02": 3, "US03": 3, "US04": 5, "US05": 2, "US06": 8, "US07": 13,
    "US08": 8, "US09": 5, "US10": 5, "US11": 3, "US12": 5, "US13": 3, "US14": 5,
    "US15": 5, "US16": 5, "US17": 3, "US18": 3, "US19": 3, "US20": 5, "US21": 5,
    "US22": 3, "US23": 3, "US24": 3, "US25": 3, "US26": 2, "US27": 5, "US28": 5,
    "US29": 3, "US30": 3, "US31": 5, "US32": 5, "US33": 3, "US34": 3, "US35": 5,
    "US36": 5, "US37": 8, "US38": 5, "US39": 2, "US40": 5, "US41": 2, "US42": 1,
    "US43": 3, "US44": 3, "US45": 3, "US46": 2, "US47": 2, "US48": 3, "US49": 2,
    "US50": 3, "US51": 1, "US52": 5, "US53": 5, "US54": 2, "US55": 2, "US56": 3,
    "US57": 3, "US58": 2, "US59": 2, "US60": 3, "US61": 3, "US62": 3, "US63": 3,
    "US64": 3, "US65": 5, "US66": 2, "US67": 5, "US68": 3, "US69": 3, "US70": 5,
    "US71": 8, "US72": 5, "US73": 5, "US74": 8, "US75": 5, "US76": 3, "US77": 5,
    "US78": 5, "US79": 5, "US80": 5, "US81": 5, "US82": 3, "US83": 3, "US84": 3,
    "US85": 8, "US86": 3, "US87": 3, "US88": 5, "US89": 3, "US90": 3, "US91": 5,
    "US92": 5, "US93": 5, "US94": 3, "US95": 3, "US96": 5, "US97": 5, "US98": 5,
    "US99": 8, "US100": 3, "US101": 2, "US102": 2, "US103": 3, "US104": 2,
    "US105": 3, "US106": 8, "US107": 3, "US108": 5, "US109": 5, "US110": 5,
    "US111": 3, "US112": 3, "US113": 5, "US114": 3, "US115": 5, "US116": 5,
    "US117": 8, "US118": 5, "US119": 3, "US120": 3, "US121": 3, "US122": 5,
    "US123": 5, "US124": 3, "US125": 1, "US126": 3, "US127": 8, "US128": 3,
    "TS01": 5, "TS02": 2, "TS03": 2, "TS04": 5, "TS05": 3, "TS06": 2, "TS07": 2,
    "TS08": 3, "TS09": 2, "TS10": 5, "TS11": 5, "TS12": 5, "TS13": 2, "TS14": 3,
    "TS15": 5, "TS16": 3, "TS17": 5, "TS18": 5, "TS19": 3, "TS20": 5, "TS21": 5,
    "TS22": 5, "TS23": 3, "TS24": 3, "TS25": 2, "TS26": 8, "TS27": 8, "TS28": 5,
    "TS29": 8, "TS30": 5, "TS31": 8, "TS32": 3, "TS33": 5, "TS34": 3,
}


def fechas(sprint):
    _, desde, hasta = HITOS[sprint]
    a = INICIO_CICLO + datetime.timedelta(days=7 * (desde - 1))
    b = INICIO_CICLO + datetime.timedelta(days=7 * hasta - 1)
    return a, b


def cargar(texto):
    historias = {}
    for linea in texto.split("## 3.3.")[0].splitlines():
        if not re.match(r"^\|\s*(US|TS)\d+\s*\|", linea):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) != 7:
            raise SystemExit("fila con %d columnas: %s" % (len(celdas), celdas[0]))
        historias[celdas[0]] = dict(
            titulo=celdas[1], plataforma=celdas[4], estado=celdas[5], epica=celdas[6]
        )
    return historias


def tabla(items, historias):
    filas = [
        "| # | ID | Historia | Épica | Plataforma | Dónde encontrarlo | Story Points |",
        "|---|---|---|---|---|---|---|",
    ]
    total = 0
    for n, ident in enumerate(items, 1):
        h = historias[ident]
        puntos = PUNTOS[ident]
        total += puntos
        filas.append(
            "| %d | %s | %s | %s | %s | %s | %d |"
            % (n, ident, h["titulo"], h["epica"], h["plataforma"],
               ubicacion(ident), puntos)
        )
    return "\n".join(filas), total


INTRO = """## 3.3. Product Backlog

El backlog completo son **162 elementos**: las 128 historias de usuario, agrupadas en diecinueve
épicas, y las 34 historias técnicas. El orden es de prioridad de negocio, no cronológico: primero
lo que hace que el sistema capture el hallazgo, después lo que permite gestionarlo, luego lo que
sostiene la operación, y al final lo que amplía la cobertura legal del sistema de gestión.

El backlog se reparte en **cuatro sprints, uno por cada hito del curso**. Las fechas no las fija el
equipo: salen del calendario del trabajo final, que sitúa los hitos en las semanas 4, 7, 12 y 15
del ciclo 2026-20, iniciado el lunes 24 de agosto de 2026. Esa es también la razón de que los
sprints sean desiguales en duración: entre el primer hito y el segundo median tres semanas, y
entre el segundo y el tercero, cinco.

Dos columnas de las tablas que siguen merecen una aclaración:

- **Plataforma** nombra el cliente concreto en el que vive la historia —`Web`, `Android`, o
  `Android y Web` cuando existe en los dos para el mismo rol—, y `—` cuando no tiene interfaz
  propia porque es trabajo de backend o de infraestructura.
- **Dónde encontrarlo** indica la ruta exacta para llegar a esa funcionalidad en cada cliente: la
  opción de la barra lateral o la ruta en el panel web, y la pestaña de la barra inferior o la
  entrada de la pantalla «Más» en la aplicación Android. Permite verificar cada historia sobre el
  producto en ejecución sin tener que buscarla.

"""


def main():
    texto = RUTA.read_text(encoding="utf-8")
    historias = cargar(texto)

    faltan = set(historias) - set(PUNTOS)
    if faltan:
        raise SystemExit("sin Story Points: %s" % sorted(faltan))

    grupos = {s: [] for s in ORDEN}
    for ident in PRIORIDAD:
        estado = historias[ident]["estado"]
        if estado in grupos:
            grupos[estado].append(ident)

    pendientes = [
        i for i in sorted(historias, key=lambda x: (x[:2], int(x[2:])))
        if historias[i]["estado"] == "Propuesta"
    ]

    resumen = [
        "| Sprint | Hito | Semanas | Fechas | Alcance | Elementos | Story Points |",
        "|---|---|---|---|---|---|---|",
    ]
    tablas = []
    total_elementos = 0
    total_puntos = 0

    for sprint in ORDEN:
        items = grupos[sprint]
        cuerpo, puntos = tabla(items, historias)
        hito, desde, hasta = HITOS[sprint]
        a, b = fechas(sprint)
        total_elementos += len(items)
        total_puntos += puntos
        resumen.append(
            "| **%s** | %s | %d a %d | %s – %s | %s | %d | %d |"
            % (sprint, hito.split(" — ")[0], desde, hasta,
               a.strftime("%d/%m/%Y"), b.strftime("%d/%m/%Y"),
               ALCANCE[sprint], len(items), puntos)
        )
        tablas.append("""
### %s — %s

| Campo | Valor |
|---|---|
| Hito | %s |
| Semanas del ciclo | %d a %d |
| Fechas | %s al %s |
| Elementos | %d |
| Story Points | %d |

%s
""" % (sprint, ALCANCE[sprint], hito, desde, hasta,
       a.strftime("%d/%m/%Y"), b.strftime("%d/%m/%Y"), len(items), puntos, cuerpo))

    cuerpo_pend, puntos_pend = tabla(pendientes, historias)
    tablas.append("""
### Backlog pendiente

Elementos especificados y estimados cuya construcción no está comprometida en ninguno de los
cuatro sprints de este ciclo. No son relleno: cada uno corresponde a una obligación de la Ley
N° 29783 o de su Reglamento que el producto debe cubrir para reemplazar por completo el
expediente en papel, y por eso queda escrito y estimado aunque no entre en el alcance.

| Campo | Valor |
|---|---|
| Elementos | %d |
| Story Points | %d |

%s
""" % (len(pendientes), puntos_pend, cuerpo_pend))

    cierre = """
### Totales del backlog

| Alcance | Elementos | Story Points |
|---|---|---|
| Comprometido en los cuatro sprints | %d | %d |
| Backlog pendiente | %d | %d |
| **Backlog completo** | **%d** | **%d** |

Los cuatro sprints cubren el %.0f %% de los Story Points del backlog.

""" % (total_elementos, total_puntos, len(pendientes), puntos_pend,
       total_elementos + len(pendientes), total_puntos + puntos_pend,
       100.0 * total_puntos / (total_puntos + puntos_pend))

    seccion = INTRO + "\n".join(resumen) + "\n" + "".join(tablas) + cierre

    antes = texto.split("## 3.3.")[0]
    despues = "## 3.4." + texto.split("## 3.4.", 1)[1]
    RUTA.write_text(antes + seccion + despues, encoding="utf-8")

    for sprint in ORDEN:
        a, b = fechas(sprint)
        print("%s: %2d elementos, %s a %s" % (sprint, len(grupos[sprint]),
                                              a.strftime("%d/%m"), b.strftime("%d/%m")))
    print("Pendiente: %d elementos, %d SP" % (len(pendientes), puntos_pend))
    print("Total: %d elementos, %d SP" % (total_elementos + len(pendientes),
                                          total_puntos + puntos_pend))


if __name__ == "__main__":
    main()
