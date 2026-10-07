"""Define a que sprint pertenece cada elemento y lo escribe en la columna Estado del README.

El README es la fuente de verdad: la columna Estado de cada historia dice su sprint.
Los demas generadores (backlog.py, workitems.py) leen de ahi.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INFORME = RAIZ / "README.md"

# Reparto por afinidad funcional, respetando el orden de dependencia:
# no se puede construir un registro sin el ciclo del hallazgo que lo alimenta.
SPRINTS = {
    "Sprint 1": [
        # El ciclo de vida completo de un hallazgo
        "US02", "US43", "US06", "US47", "US09", "US10", "US11", "US13",
        "US14", "US15", "US16", "US18", "TS01", "TS02", "TS05",
    ],
    "Sprint 2": [
        # Operacion sin conexion, captura completa y experimento A/B
        "US07", "US08", "US70", "US48", "US69", "US12", "US44", "US45", "US46",
        "US51", "US17", "US35", "US50", "US49", "US38", "US39", "US40", "US64",
        "TS09", "TS10", "TS12",
    ],
    "Sprint 3": [
        # Cuentas, roles, estructura organizativa, matriz IPERC y control de EPP
        "US01", "US03", "US05", "US04", "US41", "US42", "US19", "US20", "US21",
        "US22", "US52", "US53", "US54", "US23", "US24", "US25", "US26", "US55",
        "TS03", "TS04", "TS06", "TS07", "TS08", "TS11", "TS13",
    ],
    "Sprint 4": [
        # Inspecciones, comite de SST, metricas, evidencia exportable y calidad de uso
        "US27", "US28", "US29", "US56", "US36", "US57", "US30", "US31", "US32",
        "US33", "US34", "US58", "US59", "US60", "US37", "US61", "US62", "US63",
        "US65", "US66", "US67", "US68", "TS14", "TS15", "TS16",
    ],
}

ORDEN = ["Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4"]


def main():
    texto = INFORME.read_text(encoding="utf-8")
    cabecera, backlog = texto.split("## 3.3.", 1)

    destino = {}
    for sprint, ids in SPRINTS.items():
        for ident in ids:
            if ident in destino:
                raise SystemExit("%s aparece en dos sprints" % ident)
            destino[ident] = sprint

    construidos = set()
    for linea in cabecera.splitlines():
        m = re.match(r"^\|\s*((?:US|TS)\d+)\s*\|.*\|\s*(Sprint \d|Propuesta)\s*\|[^|]*\|\s*$", linea)
        if m and m.group(2) != "Propuesta":
            construidos.add(m.group(1))

    faltan = construidos - set(destino)
    sobran = set(destino) - construidos
    if faltan or sobran:
        raise SystemExit("desajuste: sin sprint %s | no construidos %s"
                         % (sorted(faltan), sorted(sobran)))

    cambios = 0
    for ident, sprint in destino.items():
        patron = re.compile(
            r"^(\|\s*%s\s*\|.*\|\s*)Sprint \d(\s*\|[^|]*\|)\s*$" % ident, re.M
        )
        cabecera, n = patron.subn(r"\g<1>%s\g<2>" % sprint, cabecera)
        if n != 1:
            raise SystemExit("%s: %d coincidencias" % (ident, n))
        cambios += n

    INFORME.write_text(cabecera + "## 3.3." + backlog, encoding="utf-8")
    print("elementos asignados:", cambios)
    for s in ORDEN:
        print("  %s: %d elementos" % (s, len(SPRINTS[s])))


if __name__ == "__main__":
    main()
