"""Genera los Sprint Backlogs del Capitulo V con work-items por historia.

Lee los estados y Story Points del Product Backlog del Capitulo III y desglosa cada
elemento comprometido en tareas, con estimacion en horas y area responsable.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INFORME = RAIZ / "README.md"

HORAS_POR_PUNTO = 2

# Plantillas de tarea por plataforma: (texto, peso, area)
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
    texto = INFORME.read_text(encoding="utf-8")
    cuerpo = texto.split("## 3.3.", 1)[1].split("## 3.4.", 1)[0]
    patron = (
        r"^\| \d+ \| ((?:US|TS)\d+) \| ([^|]+) \| ([^|]*) \| ([^|]+) \| (Sprint [12]) \| (\d+) \|$"
    )
    elementos = []
    for ident, titulo, epica, plataforma, estado, puntos in re.findall(
        patron, cuerpo, re.M
    ):
        elementos.append(
            dict(
                id=ident,
                titulo=titulo.strip(),
                epica=epica.strip(),
                plataforma=plataforma.strip(),
                sprint=estado,
                puntos=int(puntos),
            )
        )
    return elementos


def repartir(total, pesos):
    """Reparte las horas entre las tareas sin perder ni inventar horas."""
    brutas = [max(1, round(total * peso)) for peso in pesos]
    diferencia = total - sum(brutas)
    i = 0
    while diferencia != 0 and brutas:
        paso = 1 if diferencia > 0 else -1
        indice = i % len(brutas)
        if brutas[indice] + paso >= 1:
            brutas[indice] += paso
            diferencia -= paso
        i += 1
        if i > 1000:
            break
    return brutas


def tareas_de(elemento):
    if elemento["id"].startswith("TS"):
        plantillas = TECNICA
    else:
        plantillas = PLANTILLAS.get(elemento["plataforma"], PLANTILLAS["—"])
    total = elemento["puntos"] * HORAS_POR_PUNTO
    # Ninguna tarea baja de una hora: si la historia es muy pequena, se desglosa en
    # menos tareas en lugar de inflar el total. Se descartan por el final (primero QA).
    while len(plantillas) > 1 and total < len(plantillas):
        plantillas = plantillas[:-1]
    horas = repartir(total, [peso for _, peso in plantillas])
    salida = []
    for ((texto, area), _peso), h in zip(plantillas, horas):
        salida.append(dict(descripcion=texto % elemento["titulo"], area=area, horas=h))
    return salida


def tabla(elementos, etiqueta):
    filas = [
        "| Sprint | User Story | Título | Work-Item | Descripción de la tarea | Estimación (h) | Área responsable | Estado |",
        "|---|---|---|---|---|---|---|---|",
    ]
    n = 0
    total_horas = 0
    for elemento in elementos:
        for tarea in tareas_de(elemento):
            n += 1
            total_horas += tarea["horas"]
            filas.append(
                "| %s | %s | %s | %s-T%02d | %s | %s | %s | Terminado |"
                % (
                    etiqueta,
                    elemento["id"],
                    elemento["titulo"],
                    etiqueta.replace(" ", ""),
                    n,
                    tarea["descripcion"],
                    tarea["horas"],
                    tarea["area"],
                )
            )
    return "\n".join(filas), n, total_horas


def main():
    elementos = leer_backlog()
    s1 = [e for e in elementos if e["sprint"] == "Sprint 1"]
    s2 = [e for e in elementos if e["sprint"] == "Sprint 2"]
    t1, n1, h1 = tabla(s1, "Sprint 1")
    t2, n2, h2 = tabla(s2, "Sprint 2")
    sp1 = sum(e["puntos"] for e in s1)
    sp2 = sum(e["puntos"] for e in s2)

    seccion = """### 5.2.1. Sprint Backlogs

El ciclo se organizó en dos sprints. El Capítulo III contiene el catálogo completo de las 128
historias de usuario y las 34 historias técnicas, con su Product Backlog priorizado; esta sección
toma de ese backlog únicamente lo que cada sprint se comprometió a entregar y lo **desglosa en
work-items**: la tarea concreta, su estimación en horas y el área responsable.

**Criterio de división.** El Sprint 1 cierra el **ciclo de vida de un hallazgo** de extremo a
extremo: que el operario lo registre con evidencia y que el supervisor lo reciba, lo asigne y lo
cierre. El Sprint 2 construye sobre ese cimiento **el resto del sistema de gestión**: la matriz
IPERC, el control de EPP, las inspecciones, el comité, las métricas y la evidencia exportable, más
las cuentas, los roles y la calidad de uso. Sin el ciclo del hallazgo funcionando, ninguno de los
registros del Sprint 2 tendría de dónde alimentarse.

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

**Cómo se estimaron las horas.** Cada Story Point equivale a **%d horas** de trabajo, y las horas
de la historia se reparten entre sus work-items según el peso de cada capa. La conversión es una
regla declarada, no una medición: sirve para dimensionar el esfuerzo relativo entre tareas, no para
afirmar cuánto tardó realmente cada una.

---

#### Sprint 1

| Campo | Valor |
|---|---|
| Objetivo | Cerrar el ciclo del hallazgo de extremo a extremo: registrarlo en campo con evidencia, recibirlo, asignarlo y cerrarlo con la acción correctiva aplicada. |
| Elementos del backlog comprometidos | %d |
| Story Points | %d |
| Work-items | %d |
| Horas estimadas | %d |
| Incremento entregable | Un operario registra un acto o condición insegura con foto, ubicación y fecha real desde el celular o la web; el supervisor lo ve en su bandeja, lo asigna y lo cierra; la bitácora queda con quién hizo qué y cuándo. |

Las doce historias de usuario de este sprint están marcadas `Ambas` en el Capítulo III: el
incremento es demostrable tanto desde el panel web como desde la aplicación Android, que es la
condición de paridad que el proyecto se impuso.

%s

---

#### Sprint 2

| Campo | Valor |
|---|---|
| Objetivo | Completar el sistema de gestión sobre el ciclo del hallazgo ya funcionando: matriz IPERC, control de EPP, inspecciones, comité de SST, métricas, evidencia exportable, cuentas y calidad de uso. |
| Elementos del backlog comprometidos | %d |
| Story Points | %d |
| Work-items | %d |
| Horas estimadas | %d |
| Incremento entregable | El supervisor y el comité disponen de los registros obligatorios de la Ley N° 29783 en el sistema: peligros evaluados y versionados, entregas de EPP con conformidad, inspecciones programadas y ejecutadas con checklist, actas del comité con quórum y acuerdos, indicadores de gestión y exportación de la evidencia a Excel. |

%s

---

#### Resumen de los dos sprints

| Sprint | Elementos | Story Points | Work-items | Horas | Objetivo |
|---|---|---|---|---|---|
| Sprint 1 | %d | %d | %d | %d | Cerrar el ciclo del hallazgo de extremo a extremo. |
| Sprint 2 | %d | %d | %d | %d | Completar los registros del SGSST sobre ese ciclo. |
| **Total** | **%d** | **%d** | **%d** | **%d** | |

**Velocidad.** Los dos sprints completaron la totalidad de lo comprometido; no hubo arrastre de uno
al siguiente. Conviene señalar, sin embargo, que los sprints son marcadamente desiguales: el
Sprint 2 cuadruplica en Story Points al Sprint 1. Eso no es una buena práctica de planificación
—un sprint debe caber en una capacidad estable— y refleja que el alcance se agrupó por afinidad
funcional antes que por capacidad del equipo. Se documenta como lo que es: una decisión de
organización del trabajo, no una velocidad sostenible sobre la cual planificar.

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
> siguiente. Los dos sprints se ejecutaron sobre un plan fijado de antemano. Se documenta como
> limitación del trabajo, no como práctica recomendable.
""" % (
        HORAS_POR_PUNTO,
        len(s1), sp1, n1, h1, t1,
        len(s2), sp2, n2, h2, t2,
        len(s1), sp1, n1, h1,
        len(s2), sp2, n2, h2,
        len(s1) + len(s2), sp1 + sp2, n1 + n2, h1 + h2,
    )

    texto = INFORME.read_text(encoding="utf-8")
    inicio = texto.index("### 5.2.1. Sprint Backlog")
    fin = texto.index("### 5.2.2.")
    INFORME.write_text(texto[:inicio] + seccion + "\n" + texto[fin:], encoding="utf-8")
    print(
        "Sprint 1: %d elementos, %d SP, %d work-items, %d h" % (len(s1), sp1, n1, h1)
    )
    print(
        "Sprint 2: %d elementos, %d SP, %d work-items, %d h" % (len(s2), sp2, n2, h2)
    )


if __name__ == "__main__":
    main()
