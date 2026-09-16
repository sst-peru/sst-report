"""Regenera la seccion 3.3 Product Backlog del capitulo III a partir de las tablas de US y TS."""
import re
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "chapters" / "capitulo-03-requirements-specification.md"

# Orden de prioridad de los 86 elementos ya implementados, con su estimacion.
IMPLEMENTADOS = [
    ("US02", 3), ("US06", 8), ("US07", 13), ("US08", 8), ("US13", 3), ("US43", 3),
    ("US70", 5), ("US14", 5), ("US16", 5), ("US15", 5), ("US17", 3), ("US18", 3),
    ("US09", 5), ("US35", 5), ("US50", 3), ("US49", 2), ("US10", 5), ("US11", 3),
    ("US12", 5), ("US44", 3), ("US45", 3), ("US46", 2), ("US47", 2), ("US48", 3),
    ("US51", 1), ("US38", 5), ("US39", 2), ("US40", 5), ("US64", 3), ("US01", 5),
    ("US03", 3), ("US05", 2), ("US04", 5), ("US41", 2), ("US42", 1), ("US19", 3),
    ("US20", 5), ("US21", 5), ("US22", 3), ("US52", 5), ("US53", 5), ("US54", 2),
    ("US23", 3), ("US24", 3), ("US25", 3), ("US26", 2), ("US55", 2), ("US27", 5),
    ("US28", 5), ("US29", 3), ("US56", 3), ("US36", 5), ("US57", 3), ("US30", 3),
    ("US31", 5), ("US32", 5), ("US33", 3), ("US34", 3), ("US58", 2), ("US59", 2),
    ("US60", 3), ("US37", 8), ("US61", 3), ("US62", 3), ("US63", 3), ("US65", 5),
    ("US66", 2), ("US67", 5), ("US68", 3), ("US69", 3),
    ("TS02", 2), ("TS07", 2), ("TS05", 3), ("TS06", 2), ("TS01", 5), ("TS13", 2),
    ("TS03", 2), ("TS08", 3), ("TS09", 2), ("TS10", 5), ("TS11", 5), ("TS12", 5),
    ("TS04", 5), ("TS14", 3), ("TS15", 5), ("TS16", 3),
]

# Elementos propuestos, en orden de epica.
PROPUESTOS = [
    ("US71", 8), ("US72", 5), ("US73", 5), ("US74", 8), ("US75", 5), ("US76", 3),
    ("US77", 5), ("US78", 5),
    ("US79", 5), ("US80", 5), ("US81", 5), ("US82", 3), ("US83", 3), ("US84", 3),
    ("US85", 8), ("US86", 3), ("US87", 3), ("US88", 5),
    ("US89", 3), ("US90", 3), ("US91", 5), ("US92", 5),
    ("US93", 5), ("US94", 3), ("US95", 3),
    ("US96", 5), ("US97", 5), ("US98", 5), ("US99", 8),
    ("US100", 3), ("US101", 2), ("US102", 2), ("US103", 3), ("US104", 2), ("US105", 3),
    ("US106", 8), ("US107", 3), ("US108", 5), ("US109", 5), ("US110", 5),
    ("US111", 3), ("US112", 3), ("US113", 5), ("US114", 3), ("US115", 5), ("US116", 5),
    ("US117", 8), ("US118", 5), ("US119", 3), ("US120", 3), ("US121", 3), ("US122", 5),
    ("US123", 5), ("US124", 3), ("US125", 1), ("US126", 3), ("US127", 8), ("US128", 3),
    ("TS17", 5), ("TS18", 5), ("TS19", 3), ("TS20", 5), ("TS21", 5), ("TS22", 5),
    ("TS23", 3), ("TS24", 3), ("TS25", 2), ("TS26", 8), ("TS27", 8), ("TS28", 5),
    ("TS29", 8), ("TS30", 5), ("TS31", 8), ("TS32", 3), ("TS33", 5), ("TS34", 3),
]

INTRO = """## 3.3. Product Backlog

El backlog reúne los 162 elementos del producto: las 128 historias de usuario, agrupadas en
diecinueve épicas, y las 34 historias técnicas. El orden es de prioridad de negocio, no
cronológico: primero lo que hace que el sistema capture el hallazgo, después lo que permite
gestionarlo, luego lo que sostiene la operación, y al final lo que amplía la cobertura legal del
sistema de gestión.

La columna **Estado** separa dos cosas que conviene no confundir. *Implementada* significa que la
funcionalidad está construida y verificable en el código entregado; esos 86 elementos son los
que se repartieron en los seis sprints del Capítulo V. *Propuesta* significa que la historia está
especificada y estimada, pero su construcción queda fuera del alcance de estos sprints: es el
backlog pendiente que da continuidad al producto. Un backlog sirve precisamente para eso —
contener más de lo que cabe en un sprint — y declararlo por escrito evita atribuirle al
prototipo capacidades que todavía no tiene.

La columna **Plataforma** se repite aquí para que la paridad web/móvil sea verificable sin
volver a la sección anterior. El guion (`—`) marca los elementos sin interfaz propia: trabajo de
backend o de infraestructura.

"""


def cargar_historias(texto):
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


def epica_de(identificador, historia):
    if identificador.startswith("TS"):
        return historia["epica"] if historia["epica"] != "—" else "—"
    return historia["epica"]


def main():
    texto = RUTA.read_text(encoding="utf-8")
    historias = cargar_historias(texto)

    esperados = set(historias)
    listados = set(i for i, _ in IMPLEMENTADOS + PROPUESTOS)
    if esperados != listados:
        raise SystemExit(
            "desajuste: faltan %s, sobran %s"
            % (sorted(esperados - listados), sorted(listados - esperados))
        )

    filas = []
    numero = 0
    total_puntos = 0
    for identificador, puntos in IMPLEMENTADOS + PROPUESTOS:
        historia = historias[identificador]
        numero += 1
        total_puntos += puntos
        filas.append(
            "| %d | %s | %s | %s | %s | %s | %s |"
            % (
                numero,
                identificador,
                historia["titulo"],
                epica_de(identificador, historia),
                historia["plataforma"],
                historia["estado"],
                puntos,
            )
        )

    puntos_impl = sum(p for i, p in IMPLEMENTADOS)
    puntos_prop = sum(p for i, p in PROPUESTOS)
    us_impl = len([i for i, _ in IMPLEMENTADOS if i.startswith("US")])
    ts_impl = len([i for i, _ in IMPLEMENTADOS if i.startswith("TS")])
    us_prop = len([i for i, _ in PROPUESTOS if i.startswith("US")])
    ts_prop = len([i for i, _ in PROPUESTOS if i.startswith("TS")])

    cabecera = (
        "| # | ID | Historia | Épica | Plataforma | Estado | Story Points |\n"
        "|---|---|---|---|---|---|---|"
    )
    resumen = (
        "\n**Total:** %d elementos (%d historias de usuario y %d historias técnicas), "
        "%d Story Points.\n\n"
        "| Alcance | Elementos | Historias de usuario | Historias técnicas | Story Points |\n"
        "|---|---|---|---|---|\n"
        "| Implementado en los seis sprints | %d | %d | %d | %d |\n"
        "| Propuesto (backlog pendiente) | %d | %d | %d | %d |\n"
        "| **Backlog completo** | **%d** | **%d** | **%d** | **%d** |\n\n"
        "El equipo construyó el %.0f %% de los Story Points del backlog. Lo propuesto no es "
        "relleno: cada elemento pendiente corresponde a una obligación de la Ley N° 29783 o de "
        "su Reglamento que el producto debe cubrir para reemplazar por completo el expediente "
        "en papel, y por eso queda especificado y estimado aunque no se construya en este ciclo.\n"
        % (
            numero,
            us_impl + us_prop,
            ts_impl + ts_prop,
            total_puntos,
            len(IMPLEMENTADOS),
            us_impl,
            ts_impl,
            puntos_impl,
            len(PROPUESTOS),
            us_prop,
            ts_prop,
            puntos_prop,
            numero,
            us_impl + us_prop,
            ts_impl + ts_prop,
            total_puntos,
            100.0 * puntos_impl / total_puntos,
        )
    )

    seccion = INTRO + cabecera + "\n" + "\n".join(filas) + "\n" + resumen + "\n"

    antes = texto.split("## 3.3.")[0]
    despues = "## 3.4." + texto.split("## 3.4.", 1)[1]
    RUTA.write_text(antes + seccion + despues, encoding="utf-8")
    print("backlog regenerado: %d elementos, %d SP" % (numero, total_puntos))


if __name__ == "__main__":
    main()
