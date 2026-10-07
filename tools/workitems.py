"""Genera los Sprint Backlogs del Capitulo V con work-items por historia.

Lee de la columna Estado del Capitulo III a que sprint pertenece cada elemento y su
estimacion en Story Points, y desglosa cada uno en tareas con horas y area responsable.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAP3 = RAIZ / "chapters" / "capitulo-03-requirements-specification.md"
CAP5 = RAIZ / "chapters" / "capitulo-05-product-implementation.md"

HORAS_POR_PUNTO = 2
ORDEN = ["Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4"]

META = {
    "Sprint 1": dict(
        titulo="El ciclo de vida del hallazgo",
        objetivo=(
            "Cerrar el ciclo del hallazgo de extremo a extremo: registrarlo en campo con "
            "evidencia, recibirlo, asignarlo y cerrarlo con la acción correctiva aplicada."
        ),
        incremento=(
            "Un operario registra un acto o condición insegura con foto, ubicación y fecha real "
            "desde el celular o la web; el supervisor lo ve en su bandeja, lo asigna y lo cierra; "
            "la bitácora queda con quién hizo qué y cuándo."
        ),
        nota=(
            "Las doce historias de usuario de este sprint están marcadas `Ambas` en el Capítulo "
            "III: el incremento es demostrable tanto desde el panel web como desde la aplicación "
            "Android, que es la condición de paridad que el proyecto se impuso."
        ),
    ),
    "Sprint 2": dict(
        titulo="Operación sin conexión, evidencia y experimento A/B",
        objetivo=(
            "Que el hallazgo sobreviva a la falta de señal y que la evidencia esté completa: "
            "captura sin conexión con sincronización sin duplicados, fotografía y ubicación "
            "verificables, y el experimento A/B corriendo sobre el formulario de reporte."
        ),
        incremento=(
            "El operario reporta en una zona sin cobertura, ve su reporte en estado pendiente y lo "
            "encuentra sincronizado al recuperar la señal, sin duplicados. El supervisor filtra su "
            "bandeja, descarta lo que no corresponde y consulta el MTTR. Cada reporte queda "
            "atribuido a su variante de formulario y los resultados del experimento son "
            "consultables."
        ),
        nota=(
            "Este sprint contiene la historia más costosa del backlog, US07 «Reporte sin "
            "conexión» con 13 Story Points, porque exige almacenamiento local, cola de envío y "
            "reintento automático. Es también la que sostiene la propuesta de valor del producto."
        ),
    ),
    "Sprint 3": dict(
        titulo="Cuentas, matriz IPERC y control de EPP",
        objetivo=(
            "Dar a la empresa la estructura sobre la que se apoyan los registros: usuarios con "
            "rol, áreas de trabajo, la matriz IPERC versionada y el control de entrega de equipos "
            "de protección personal."
        ),
        incremento=(
            "El supervisor da de alta trabajadores y áreas, y cambia roles sin recrear cuentas. La "
            "matriz IPERC se registra por área y puesto con su nivel de riesgo calculado, se "
            "versiona y conserva su histórico. Las entregas de EPP quedan con conformidad del "
            "trabajador y aviso de vencimiento por vida útil."
        ),
        nota=(
            "El orden importa: la matriz IPERC y las entregas de EPP se clasifican por área, de "
            "modo que la estructura organizativa tiene que existir antes que los registros que la "
            "referencian."
        ),
    ),
    "Sprint 4": dict(
        titulo="Inspecciones, comité de SST y evidencia exportable",
        objetivo=(
            "Completar los registros que una inspección de SUNAFIL solicita y dejar la evidencia "
            "lista para entregar: programa de inspecciones, comité de SST con sus actas, "
            "indicadores de gestión y exportación a Excel."
        ),
        incremento=(
            "Las inspecciones se programan por frecuencia, se ejecutan con checklist desde el "
            "celular y su cumplimiento se mide por área. El comité queda constituido con "
            "representación paritaria, sus actas numeradas verifican quórum y sus acuerdos tienen "
            "responsable y plazo. Cada registro obligatorio se exporta a Excel con su "
            "trazabilidad completa."
        ),
        nota=(
            "Este sprint cierra el alcance del ciclo: a partir de aquí el producto ya sustituye el "
            "expediente en papel para los registros que cubre, y lo que falta está declarado como "
            "backlog propuesto en el Capítulo III."
        ),
    ),
}

API = ("Implementar en el API la lógica y el endpoint de «%s»", "Backend")
WEB = ("Construir en el panel web la interfaz de «%s»", "Web")
MOV = ("Construir en la aplicación Android la interfaz de «%s»", "Móvil")
QA = ("Cubrir «%s» con pruebas automatizadas", "QA")

PLANTILLAS = {
    "Ambas": [(API, 0.30), (WEB, 0.30), (MOV, 0.30), (QA, 0.10)],
    "Web": [(API, 0.35), (WEB, 0.45), (QA, 0.20)],
    "Móvil": [(API, 0.35), (MOV, 0.45), (QA, 0.20)],
    "—": [(API, 0.75), (QA, 0.25)],
}

TECNICA = [
    (("Configurar «%s»", "DevOps"), 0.70),
    (("Verificar «%s» en el pipeline", "DevOps"), 0.30),
]


def leer_backlog():
    cuerpo = CAP3.read_text(encoding="utf-8").split("## 3.3.", 1)[1]
    patron = (
        r"^\| \d+ \| ((?:US|TS)\d+) \| ([^|]+) \| ([^|]*) \| ([^|]+) \| (Sprint \d) \| (\d+) \|$"
    )
    elementos = []
    for ident, titulo, epica, plataforma, estado, puntos in re.findall(patron, cuerpo, re.M):
        elementos.append(
            dict(
                id=ident,
                titulo=titulo.strip(),
                plataforma=plataforma.strip(),
                sprint=estado,
                puntos=int(puntos),
            )
        )
    return elementos


def repartir(total, pesos):
    brutas = [max(1, round(total * peso)) for peso in pesos]
    diferencia = total - sum(brutas)
    i = 0
    while diferencia != 0 and brutas and i < 1000:
        paso = 1 if diferencia > 0 else -1
        indice = i % len(brutas)
        if brutas[indice] + paso >= 1:
            brutas[indice] += paso
            diferencia -= paso
        i += 1
    return brutas


def tareas_de(elemento):
    if elemento["id"].startswith("TS"):
        plantillas = list(TECNICA)
    else:
        plantillas = list(PLANTILLAS.get(elemento["plataforma"], PLANTILLAS["—"]))
    total = elemento["puntos"] * HORAS_POR_PUNTO
    # Ninguna tarea baja de una hora: si la historia es muy pequena se desglosa en menos
    # tareas en lugar de inflar el total. Se descartan por el final (primero QA).
    while len(plantillas) > 1 and total < len(plantillas):
        plantillas = plantillas[:-1]
    horas = repartir(total, [peso for _, peso in plantillas])
    return [
        dict(descripcion=texto % elemento["titulo"], area=area, horas=h)
        for ((texto, area), _), h in zip(plantillas, horas)
    ]


def tabla(elementos, sprint):
    etiqueta = sprint.replace(" ", "")
    filas = [
        "| Sprint | User Story | Título | Work-Item | Descripción de la tarea | "
        "Estimación (h) | Área responsable | Estado |",
        "|---|---|---|---|---|---|---|---|",
    ]
    n = 0
    horas = 0
    for elemento in elementos:
        for tarea in tareas_de(elemento):
            n += 1
            horas += tarea["horas"]
            filas.append(
                "| %s | %s | %s | %s-T%02d | %s | %s | %s | Terminado |"
                % (sprint, elemento["id"], elemento["titulo"], etiqueta, n,
                   tarea["descripcion"], tarea["horas"], tarea["area"])
            )
    return "\n".join(filas), n, horas


ENCABEZADO = """### 5.2.1. Sprint Backlogs

El ciclo se organizó en cuatro sprints. El Capítulo III contiene el catálogo completo de las 128
historias de usuario y las 34 historias técnicas, con su Product Backlog priorizado; esta sección
toma de ese backlog únicamente lo que cada sprint se comprometió a entregar y lo **desglosa en
work-items**: la tarea concreta, su estimación en horas y el área responsable.

**Criterio de división.** Los sprints no agrupan por comodidad sino por dependencia: cada uno
necesita que el anterior esté funcionando.

| Sprint | Alcance | Por qué va en ese orden |
|---|---|---|
| Sprint 1 | El ciclo de vida del hallazgo | Es el mínimo que entrega valor por sí solo: sin un hallazgo que se registra y se cierra, ningún otro registro tiene de dónde alimentarse |
| Sprint 2 | Operación sin conexión, evidencia y experimento A/B | Endurece ese ciclo para el campo real, donde la señal falla, y deja el experimento corriendo sobre el formulario ya construido |
| Sprint 3 | Cuentas, matriz IPERC y control de EPP | La matriz y las entregas se clasifican por área y por rol, así que la estructura organizativa tiene que existir antes |
| Sprint 4 | Inspecciones, comité de SST y evidencia exportable | Cierra el expediente: lo que se exporta son los registros que los tres sprints anteriores generaron |

**Cómo se desglosó cada historia.** Una historia de usuario no es una tarea: atraviesa el API, la
web y el móvil. El desglose sigue esa estructura, de modo que cada work-item cae en un único
repositorio y en una única área responsable:

| Plataforma de la historia | Work-items que genera |
|---|---|
| `Ambas` | Lógica y endpoint en el API · interfaz en el panel web · interfaz en Android · pruebas automatizadas |
| `Web` | Lógica y endpoint en el API · interfaz en el panel web · pruebas automatizadas |
| `Móvil` | Lógica y endpoint en el API · interfaz en Android · pruebas automatizadas |
| `—` (sin interfaz) | Lógica en el API · pruebas automatizadas |
| Historia técnica | Configuración · verificación en el pipeline |

**Cómo se estimaron las horas.** Cada Story Point equivale a **%d horas** de trabajo, y las horas de
la historia se reparten entre sus work-items según el peso de cada capa. Ninguna tarea baja de una
hora. La conversión es una regla declarada, no una medición: sirve para dimensionar el esfuerzo
relativo entre tareas, no para afirmar cuánto tardó realmente cada una.
"""

BLOQUE = """
---

#### %s — %s

| Campo | Valor |
|---|---|
| Objetivo | %s |
| Elementos del backlog comprometidos | %d |
| Story Points | %d |
| Work-items | %d |
| Horas estimadas | %d |
| Incremento entregable | %s |

%s

%s
"""

CIERRE = """
---

#### Resumen de los cuatro sprints

| Sprint | Alcance | Elementos | Story Points | Work-items | Horas |
|---|---|---|---|---|---|
%s
| **Total** | | **%d** | **%d** | **%d** | **%d** |

**Velocidad.** Los cuatro sprints completaron la totalidad de lo comprometido; no hubo arrastre de
uno al siguiente. Los Story Points por sprint fueron %s, con un promedio de %.0f. El sprint más
cargado supera al más liviano en %.0f %%: un reparto más parejo habría sido preferible, pero el
alcance se agrupó por dependencia funcional —cada sprint necesita el anterior— y forzar la igualdad
habría partido capacidades a la mitad.

**Sobre el periodo de ejecución.** Conviene decirlo con precisión, porque el historial de los
repositorios es público y cualquiera puede contrastarlo: los sprints **organizan el alcance, no
ventanas de calendario**. El trabajo se ejecutó en sesiones intensivas de desarrollo entre el 12 y
el 16 de septiembre de 2026, que es lo que muestran las fechas de los commits en `sst-api`,
`sst-web`, `sst-mobile` y `sst-report`. Por eso las tablas no declaran fechas de inicio y fin:
declararlas repartidas en semanas sería contradecir un dato verificable en un clic. Por la misma
razón las horas estimadas son una conversión declarada de los Story Points y no un registro de
tiempo real.

> **Limitación reconocida.** Un ciclo de desarrollo comprimido impide observar lo que la práctica
> iterativa busca: retroalimentación del usuario entre iteraciones que reoriente el alcance de la
> siguiente. Los cuatro sprints se ejecutaron sobre un plan fijado de antemano. Se documenta como
> limitación del trabajo, no como práctica recomendable.
"""


def main():
    elementos = leer_backlog()
    partes = [ENCABEZADO % HORAS_POR_PUNTO]
    resumen = []

    for sprint in ORDEN:
        items = [e for e in elementos if e["sprint"] == sprint]
        cuerpo, n, horas = tabla(items, sprint)
        puntos = sum(e["puntos"] for e in items)
        meta = META[sprint]
        resumen.append((sprint, meta["titulo"], len(items), puntos, n, horas))
        partes.append(
            BLOQUE % (sprint, meta["titulo"], meta["objetivo"], len(items), puntos, n,
                      horas, meta["incremento"], meta["nota"], cuerpo)
        )

    tot_e = sum(r[2] for r in resumen)
    tot_p = sum(r[3] for r in resumen)
    tot_n = sum(r[4] for r in resumen)
    tot_h = sum(r[5] for r in resumen)
    filas = "\n".join(
        "| %s | %s | %d | %d | %d | %d |" % (s, titulo, e, p, n, h)
        for s, titulo, e, p, n, h in resumen
    )
    puntos_sprint = [r[3] for r in resumen]
    partes.append(
        CIERRE % (filas, tot_e, tot_p, tot_n, tot_h,
                  ", ".join(str(p) for p in puntos_sprint),
                  tot_p / float(len(puntos_sprint)),
                  100.0 * (max(puntos_sprint) - min(puntos_sprint)) / min(puntos_sprint))
    )

    texto = CAP5.read_text(encoding="utf-8")
    inicio = texto.index("### 5.2.1. Sprint Backlog")
    fin = texto.index("### 5.2.2.")
    CAP5.write_text(texto[:inicio] + "".join(partes) + "\n" + texto[fin:], encoding="utf-8")

    for s, titulo, e, p, n, h in resumen:
        print("%s: %d elementos, %d SP, %d work-items, %d h" % (s, e, p, n, h))
    print("Total: %d elementos, %d SP, %d work-items, %d h" % (tot_e, tot_p, tot_n, tot_h))


if __name__ == "__main__":
    main()
