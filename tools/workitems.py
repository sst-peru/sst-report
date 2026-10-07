"""Genera los Sprint Backlogs del Capitulo V con work-items por historia.

Lee del Product Backlog de la seccion 3.3 a que sprint pertenece cada elemento, su
plataforma y sus Story Points, y desglosa cada uno en tareas con estimacion en horas
y area responsable. Las fechas y los hitos salen de backlog.py.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from backlog import ALCANCE, HITOS, ORDEN, PUNTOS, fechas  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
INFORME = RAIZ / "README.md"

HORAS_POR_PUNTO = 1

API = ("Implementar en el API la lógica y el endpoint de «%s»", "Backend")
WEB = ("Construir en el panel web la interfaz de «%s»", "Web")
MOV = ("Construir en la aplicación Android la interfaz de «%s»", "Móvil")
QA = ("Cubrir «%s» con pruebas automatizadas", "QA")

PLANTILLAS = {
    "Android y Web": [(API, 0.30), (WEB, 0.30), (MOV, 0.30), (QA, 0.10)],
    "Web": [(API, 0.35), (WEB, 0.45), (QA, 0.20)],
    "Android": [(API, 0.35), (MOV, 0.45), (QA, 0.20)],
    "—": [(API, 0.75), (QA, 0.25)],
}

TECNICA = [
    (("Configurar «%s»", "DevOps"), 0.70),
    (("Verificar «%s» en el pipeline", "DevOps"), 0.30),
]

OBJETIVO = {
    "Sprint 1": (
        "Cerrar el ciclo del hallazgo de extremo a extremo: registrarlo en campo con evidencia, "
        "recibirlo, asignarlo y cerrarlo con la acción correctiva aplicada."
    ),
    "Sprint 2": (
        "Endurecer la captura para el campo real y completar el registro de lo que ocurre: "
        "operación sin conexión, evidencia verificable, accidentes e incidentes, privacidad del "
        "reporte y el experimento A/B en marcha."
    ),
    "Sprint 3": (
        "Dar al sistema su estructura y sus registros obligatorios —cuentas y áreas, matriz "
        "IPERC, control de EPP, inspecciones, capacitación, mapa de riesgos y documentación del "
        "SGSST— y dejar el producto desplegado en un entorno de pruebas."
    ),
    "Sprint 4": (
        "Cerrar el expediente y el servicio: comité de SST con sus actas, indicadores y "
        "evidencia exportable, contratistas, monitoreo de agentes, notificaciones, gestión de la "
        "cuenta, seguridad de los datos personales y calidad de uso."
    ),
}

INCREMENTO = {
    "Sprint 1": (
        "Un operario registra un acto o condición insegura con foto, ubicación y fecha real desde "
        "el celular o la web; el supervisor lo ve en su bandeja, lo asigna y lo cierra; la "
        "bitácora queda con quién hizo qué y cuándo."
    ),
    "Sprint 2": (
        "El operario reporta sin cobertura y su reporte llega solo al recuperar la señal, sin "
        "duplicados; puede hacerlo de forma anónima y negar la ubicación sin perder la "
        "funcionalidad. Los accidentes e incidentes se registran e investigan hasta su causa "
        "raíz. Cada reporte queda atribuido a su variante y los resultados del experimento son "
        "consultables con su intervalo de confianza."
    ),
    "Sprint 3": (
        "La empresa tiene usuarios con rol y áreas de trabajo; la matriz IPERC se registra, "
        "versiona y conserva su histórico; las entregas de EPP quedan con conformidad firmada y "
        "aviso de vencimiento; las inspecciones se programan y ejecutan con checklist; la "
        "capacitación, el mapa de riesgos y la documentación del SGSST están en el sistema. El "
        "producto corre en un entorno desplegado, no solo en las máquinas del equipo."
    ),
    "Sprint 4": (
        "El comité queda constituido con representación paritaria, sus actas verifican quórum y "
        "sus acuerdos tienen responsable y plazo. Los indicadores y cada registro obligatorio se "
        "exportan a Excel. El sistema avisa por notificación lo que vence o queda sin atender, "
        "gestiona contratistas y monitoreo de agentes, y protege los datos personales con "
        "auditoría de accesos, cifrado y política de retención."
    ),
}

NOTA = {
    "Sprint 1": (
        "Las doce historias de usuario de este sprint están marcadas `Android y Web`: el "
        "incremento es demostrable tanto desde el panel web como desde la aplicación Android, que "
        "es la condición de paridad que el proyecto se impuso."
    ),
    "Sprint 2": (
        "Este sprint contiene la historia más costosa del backlog, US07 «Reporte sin conexión» "
        "con 13 Story Points, porque exige almacenamiento local, cola de envío y reintento "
        "automático. Es también la que sostiene la propuesta de valor del producto."
    ),
    "Sprint 3": (
        "El orden importa: la matriz IPERC, las entregas de EPP y las inspecciones se clasifican "
        "por área y por rol, de modo que la estructura organizativa tiene que existir antes que "
        "los registros que la referencian. El despliegue se incluye aquí y no antes porque "
        "desplegar un producto cuyo alcance todavía cambia obliga a rehacer la configuración en "
        "cada iteración."
    ),
    "Sprint 4": (
        "Este sprint cierra el alcance del producto: a partir de aquí Resguardo sustituye el "
        "expediente en papel para los registros que la Ley N° 29783 exige, y lo que quede fuera "
        "tendría que salir del alcance, no quedar pendiente."
    ),
}


def leer_backlog():
    """Lee las filas del Product Backlog de la seccion 3.3."""
    texto = INFORME.read_text(encoding="utf-8")
    cuerpo = texto.split("## 3.3.")[1].split("## 3.4.")[0]
    elementos = []
    sprint = None
    for linea in cuerpo.splitlines():
        m = re.match(r"^### (Sprint \d) —", linea)
        if m:
            sprint = m.group(1)
            continue
        f = re.match(r"^\| \d+ \| ((?:US|TS)\d+) \| ([^|]+) \| ([^|]*) \| ([^|]+) \|", linea)
        if f and sprint:
            elementos.append(
                dict(id=f.group(1), titulo=f.group(2).strip(),
                     plataforma=f.group(4).strip(), sprint=sprint)
            )
    return elementos


def repartir(total, pesos):
    """Reparte en unidades de media hora, para que ninguna tarea desaparezca."""
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
    # Se trabaja en medias horas para que una historia pequena no pierda sus tareas.
    medias = int(round(PUNTOS[elemento["id"]] * HORAS_POR_PUNTO * 2))
    while len(plantillas) > 1 and medias < len(plantillas):
        plantillas = plantillas[:-1]
    reparto = repartir(medias, [peso for _, peso in plantillas])
    return [
        dict(descripcion=texto % elemento["titulo"], area=area, horas=u / 2.0)
        for ((texto, area), _), u in zip(plantillas, reparto)
    ]


def formato_horas(h):
    """1.0 -> «1»; 2.5 -> «2,5» (coma decimal, como el resto del informe)."""
    return str(int(h)) if h == int(h) else ("%.1f" % h).replace(".", ",")


def tabla(elementos, sprint):
    etiqueta = sprint.replace(" ", "")
    filas = [
        "| Sprint | User Story | Título | Work-Item | Descripción de la tarea | "
        "Estimación (h) | Área responsable |",
        "|---|---|---|---|---|---|---|",
    ]
    n = 0
    horas = 0
    for elemento in elementos:
        for tarea in tareas_de(elemento):
            n += 1
            horas += tarea["horas"]
            filas.append(
                "| %s | %s | %s | %s-T%03d | %s | %s | %s |"
                % (sprint, elemento["id"], elemento["titulo"], etiqueta, n,
                   tarea["descripcion"], formato_horas(tarea["horas"]), tarea["area"])
            )
    return "\n".join(filas), n, horas


ENCABEZADO = """### 5.2.1. Sprint Backlogs

El ciclo se organizó en cuatro sprints, uno por cada hito del curso. La sección 3.3 del Capítulo
III contiene el Product Backlog completo con los 162 elementos repartidos entre ellos; esta
sección toma el alcance de cada sprint y lo **desglosa en work-items**: la tarea concreta, su
estimación en horas y el área responsable.

**Cómo se desglosó cada historia.** Una historia de usuario no es una tarea: atraviesa el API, la
web y el móvil. El desglose sigue esa estructura, de modo que cada work-item cae en un único
repositorio y en una única área responsable:

| Plataforma de la historia | Work-items que genera |
|---|---|
| `Android y Web` | Lógica y endpoint en el API · interfaz en el panel web · interfaz en Android · pruebas automatizadas |
| `Web` | Lógica y endpoint en el API · interfaz en el panel web · pruebas automatizadas |
| `Android` | Lógica y endpoint en el API · interfaz en Android · pruebas automatizadas |
| `—` (sin interfaz) | Lógica en el API · pruebas automatizadas |
| Historia técnica | Configuración · verificación en el pipeline |

**Cómo se estimaron las horas.** Cada Story Point equivale a **%d hora** de trabajo, y las horas de
la historia se reparten entre sus work-items según el peso de cada capa, en unidades de media
hora. La conversión es una regla declarada, no una medición: sirve para dimensionar el esfuerzo
relativo entre tareas, no para afirmar cuánto tardó realmente cada una.
"""

BLOQUE = """
---

#### %s — %s

| Campo | Valor |
|---|---|
| Hito | %s |
| Semanas del ciclo | %d a %d |
| Fechas | %s al %s |
| Objetivo | %s |
| Elementos del backlog | %d |
| Story Points | %d |
| Work-items | %d |
| Horas estimadas | %s |
| Incremento entregable | %s |

%s

%s
"""

CIERRE = """
---

#### Resumen de los cuatro sprints

| Sprint | Alcance | Fechas | Elementos | Story Points | Work-items | Horas |
|---|---|---|---|---|---|---|
%s
| **Total** | | | **%d** | **%d** | **%d** | **%s** |

**Sobre la carga por sprint.** Los Story Points por sprint son %s. La diferencia no es un
descuido de planificación: los sprints duran lo que el calendario del curso marca entre hitos
—cuatro semanas el primero, tres el segundo, cinco el tercero y tres el cuarto— y el alcance se
agrupó por dependencia funcional, porque cada sprint necesita que el anterior esté funcionando.
Forzar una carga pareja habría obligado a partir capacidades a la mitad y a desplegar antes de
que el alcance estuviera estable.

> **Limitación reconocida.** Las horas estimadas son una conversión declarada de los Story
> Points, no un registro de tiempo real, y la velocidad de un sprint no se ha medido contra una
> capacidad observada del equipo. Mientras no haya sprints cerrados con su esfuerzo registrado,
> estas cifras sirven para dimensionar el trabajo, no para predecirlo.
"""


def main():
    elementos = leer_backlog()
    if len(elementos) != 162:
        raise SystemExit("se leyeron %d elementos, se esperaban 162" % len(elementos))

    partes = [ENCABEZADO % HORAS_POR_PUNTO]
    resumen = []

    for sprint in ORDEN:
        items = [e for e in elementos if e["sprint"] == sprint]
        cuerpo, n, horas = tabla(items, sprint)
        puntos = sum(PUNTOS[e["id"]] for e in items)
        hito, desde, hasta = HITOS[sprint]
        a, b = fechas(sprint)
        resumen.append((sprint, len(items), puntos, n, horas,
                        a.strftime("%d/%m/%Y"), b.strftime("%d/%m/%Y")))
        partes.append(
            BLOQUE % (sprint, ALCANCE[sprint], hito, desde, hasta,
                      a.strftime("%d/%m/%Y"), b.strftime("%d/%m/%Y"),
                      OBJETIVO[sprint], len(items), puntos, n, formato_horas(horas),
                      INCREMENTO[sprint], NOTA[sprint], cuerpo)
        )

    tot_e = sum(r[1] for r in resumen)
    tot_p = sum(r[2] for r in resumen)
    tot_n = sum(r[3] for r in resumen)
    tot_h = sum(r[4] for r in resumen)
    filas = "\n".join(
        "| %s | %s | %s – %s | %d | %d | %d | %s |"
        % (s, ALCANCE[s], d1, d2, e, p, n, formato_horas(h))
        for s, e, p, n, h, d1, d2 in resumen
    )
    partes.append(
        CIERRE % (filas, tot_e, tot_p, tot_n, formato_horas(tot_h),
                  ", ".join(str(r[2]) for r in resumen))
    )

    texto = INFORME.read_text(encoding="utf-8")
    inicio = texto.index("### 5.2.1. Sprint Backlog")
    fin = texto.index("### 5.2.2.")
    INFORME.write_text(texto[:inicio] + "".join(partes) + "\n" + texto[fin:], encoding="utf-8")

    for s, e, p, n, h, _, _ in resumen:
        print("%s: %2d elementos, %3d SP, %3d work-items, %s h" % (s, e, p, n, formato_horas(h)))
    print("Total: %d elementos, %d SP, %d work-items, %s h" % (tot_e, tot_p, tot_n, formato_horas(tot_h)))


if __name__ == "__main__":
    main()
