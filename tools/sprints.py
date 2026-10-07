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
        # Captura completa en campo, accidentes, privacidad del reporte y experimento A/B
        "US07", "US08", "US70", "US48", "US69", "US12", "US44", "US45", "US46",
        "US51", "US17", "US35", "US50", "US49", "US38", "US39", "US40", "US64",
        "US71", "US72", "US73", "US74", "US75", "US76", "US77", "US78",
        "US111", "US112", "US116", "US117", "US125", "US126",
        "TS09", "TS10", "TS12", "TS31",
    ],
    "Sprint 3": [
        # Cuentas, registros obligatorios del SGSST, capacitacion y despliegue
        "US01", "US03", "US05", "US04", "US41", "US42",
        "US19", "US20", "US21", "US22", "US52", "US53", "US54",
        "US23", "US24", "US25", "US26", "US55", "US118",
        "US27", "US28", "US29", "US56", "US57", "US119", "US120",
        "US79", "US80", "US81", "US82", "US83", "US84",
        "US85", "US86", "US87", "US88",
        "US89", "US90", "US91", "US92",
        "TS03", "TS04", "TS06", "TS07", "TS08", "TS11", "TS13",
        "TS19", "TS21", "TS22", "TS23", "TS24", "TS25", "TS28", "TS30",
    ],
    "Sprint 4": [
        # Comite, evidencia, contratistas, notificaciones, seguridad y calidad de uso
        "US30", "US31", "US32", "US33", "US34", "US58", "US59", "US60",
        "US121", "US122",
        "US36", "US37", "US61", "US62", "US63", "US123", "US124",
        "US93", "US94", "US95",
        "US96", "US97", "US98", "US99",
        "US100", "US101", "US102", "US103", "US104", "US105",
        "US106", "US107", "US108", "US109", "US110",
        "US113", "US114", "US115",
        "US65", "US66", "US67", "US68", "US127", "US128",
        "TS14", "TS15", "TS16", "TS17", "TS18", "TS20", "TS26", "TS27",
        "TS29", "TS32", "TS33", "TS34",
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
        if m:
            construidos.add(m.group(1))

    faltan = construidos - set(destino)
    sobran = set(destino) - construidos
    if faltan or sobran:
        raise SystemExit("desajuste: sin sprint %s | no construidos %s"
                         % (sorted(faltan), sorted(sobran)))

    cambios = 0
    for ident, sprint in destino.items():
        patron = re.compile(
            r"^(\|\s*%s\s*\|.*\|\s*)(?:Sprint \d|Propuesta)(\s*\|[^|]*\|)\s*$" % ident, re.M
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
