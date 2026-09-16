# Capítulo III: Requirements Specification

## 3.1. To-Be Scenario Mapping

<!-- IMAGEN REQUERIDA: exportar el To-Be Scenario Map a assets/img/to-be-scenario-map.png -->

![To-Be Scenario Map](../assets/img/to-be-scenario-map.png)

| Fase | Detección | Reporte | Asignación | Corrección | Evidencia |
|---|---|---|---|---|---|
| **Acciones** | El trabajador identifica el peligro | Abre la app y reporta en tres toques con foto; si no hay señal, queda guardado y se envía solo | El supervisor ve el hallazgo en el panel y asigna responsable con un comentario | Se aplica la acción correctiva y se cierra el hallazgo describiéndola | El sistema exporta a Excel el registro completo con su trazabilidad |
| **Pensamientos** | "Esto es peligroso" | "Listo, quedó registrado" | "Esto es crítico, va primero" | "Queda documentado quién, qué y cuándo" | "Tengo cómo demostrarlo" |
| **Mejoras respecto del as-is** | — | Registro con hora exacta, foto y GPS; sin dependencia de la señal | Priorización por severidad en lugar de por quién insiste más | Responsable y plazo explícitos; bitácora automática | Expediente generado por la operación diaria, no reconstruido a mano |

## 3.2. User Stories

Las historias se agrupan en nueve épicas. Los criterios de aceptación siguen el formato Gherkin
(Dado / Cuando / Entonces). Las historias técnicas (TS) corresponden a trabajo de infraestructura
sin valor directo para el usuario final pero necesario para sostener el producto.

