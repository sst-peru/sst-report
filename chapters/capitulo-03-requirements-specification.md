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

### Épicas

| ID | Épica | Descripción |
|---|---|---|
| EP01 | Acceso y cuentas | Registro, autenticación y administración de usuarios y roles. |
| EP02 | Reporte de actos y condiciones inseguras | Captura del hallazgo en campo, con evidencia y operación sin conexión. |
| EP03 | Gestión del hallazgo | Seguimiento desde la recepción hasta el cierre verificado. |
| EP04 | Matriz IPERC | Identificación de peligros, evaluación de riesgos y controles. |
| EP05 | Control de EPP | Catálogo, entregas, vencimientos y conformidad del trabajador. |
| EP06 | Inspecciones periódicas | Programación, ejecución con checklist y cumplimiento. |
| EP07 | Comité de SST | Constitución, miembros, actas de reunión y acuerdos. |
| EP08 | Métricas y evidencia | Indicadores de gestión y exportación para auditorías. |
| EP09 | Experimento A/B | Asignación de variantes y medición de resultados. |

### EP01 — Acceso y cuentas

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US01 | Registro de trabajador | **Como** trabajador **quiero** crear mi cuenta indicando el RUC de mi empresa **para** empezar a reportar sin depender de que alguien me la cree. | **Escenario: registro exitoso**<br>**Dado** que ingreso al formulario de registro<br>**Cuando** completo mis datos y el RUC de una empresa registrada<br>**Entonces** el sistema crea mi cuenta con rol operario y me deja dentro de la aplicación<br><br>**Escenario: RUC inexistente**<br>**Dado** que ingreso un RUC no registrado<br>**Cuando** envío el formulario<br>**Entonces** el sistema me indica que debo solicitar el RUC a mi supervisor y no crea la cuenta | EP01 |
| US02 | Inicio de sesión | **Como** usuario **quiero** iniciar sesión con usuario y contraseña **para** acceder a la información de mi empresa. | **Escenario: credenciales válidas**<br>**Dado** que tengo una cuenta activa<br>**Cuando** ingreso mis credenciales correctas<br>**Entonces** el sistema me autentica y me lleva a la pantalla inicial de mi rol<br><br>**Escenario: credenciales inválidas**<br>**Cuando** ingreso credenciales incorrectas<br>**Entonces** el sistema muestra un mensaje de error sin revelar si el usuario existe | EP01 |
| US03 | Sesión persistente en campo | **Como** operario **quiero** permanecer autenticado varios días **para** no tener que iniciar sesión cuando estoy en una zona sin señal. | **Escenario: renovación automática**<br>**Dado** que mi token de acceso expiró<br>**Cuando** la aplicación realiza una petición<br>**Entonces** el sistema renueva el token automáticamente y la petición se completa sin pedirme la contraseña | EP01 |
| US04 | Administración de usuarios | **Como** supervisor de SST **quiero** crear usuarios y asignarles rol **para** incorporar al equipo de seguridad con los permisos correctos. | **Escenario: alta de supervisor**<br>**Dado** que tengo rol de supervisor<br>**Cuando** creo un usuario con rol supervisor<br>**Entonces** el usuario queda creado en mi empresa con ese rol<br><br>**Escenario: operario sin permiso**<br>**Dado** que tengo rol operario<br>**Cuando** intento listar los usuarios<br>**Entonces** el sistema deniega el acceso | EP01 |
| US05 | Gestión de áreas | **Como** supervisor **quiero** registrar las áreas o frentes de trabajo **para** clasificar los hallazgos por ubicación organizativa. | **Escenario: alta de área**<br>**Cuando** registro un área con nombre y descripción<br>**Entonces** queda disponible para clasificar reportes, inspecciones y entradas IPERC | EP01 |

### EP02 — Reporte de actos y condiciones inseguras

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US06 | Reporte rápido desde el celular | **Como** operario **quiero** reportar un peligro en tres toques con una foto **para** no perder tiempo de trabajo. | **Escenario: reporte en tres pasos**<br>**Dado** que estoy en el frente de trabajo<br>**Cuando** elijo el tipo de hallazgo, la categoría y tomo la foto<br>**Entonces** el sistema registra el reporte y me confirma que quedó guardado<br><br>**Escenario: descripción opcional**<br>**Cuando** envío el reporte sin escribir descripción<br>**Entonces** el sistema lo acepta igualmente | EP02 |
| US07 | Reporte sin conexión | **Como** operario en obra o mina **quiero** que mi reporte se guarde aunque no haya señal **para** no perderlo. | **Escenario: sin conectividad**<br>**Dado** que el dispositivo no tiene conexión<br>**Cuando** envío el reporte<br>**Entonces** se almacena localmente y se muestra como pendiente de envío<br><br>**Escenario: recuperación de señal**<br>**Cuando** el dispositivo recupera la conexión<br>**Entonces** el sistema sincroniza los reportes pendientes sin intervención del usuario | EP02 |
| US08 | Sincronización sin duplicados | **Como** responsable de SST **quiero** que un reintento de envío no genere reportes repetidos **para** que las métricas sean confiables. | **Escenario: reintento del mismo reporte**<br>**Dado** un reporte con un identificador de cliente ya recibido<br>**Cuando** el dispositivo reintenta el envío<br>**Entonces** el sistema devuelve el reporte existente y no crea uno nuevo | EP02 |
| US09 | Evidencia fotográfica | **Como** miembro del comité **quiero** ver la foto del hallazgo **para** entender el peligro sin desplazarme al lugar. | **Escenario: foto adjunta**<br>**Cuando** abro el detalle de un reporte con foto<br>**Entonces** veo la imagen y puedo ampliarla a pantalla completa | EP02 |
| US10 | Geolocalización del hallazgo | **Como** supervisor **quiero** saber dónde ocurrió el hallazgo **para** ubicarlo dentro de la operación. | **Escenario: captura de coordenadas**<br>**Cuando** el operario autoriza la ubicación al tomar la foto<br>**Entonces** el reporte guarda latitud y longitud y el panel ofrece verlas en un mapa<br><br>**Escenario: permiso denegado**<br>**Cuando** el operario no autoriza la ubicación<br>**Entonces** el reporte se envía igualmente, sin coordenadas | EP02 |
| US11 | Fecha real de ocurrencia | **Como** analista **quiero** que el reporte conserve la fecha en que ocurrió el hecho **para** que el indicador de tiempo de respuesta no se distorsione. | **Escenario: sincronización diferida**<br>**Dado** un reporte creado sin conexión el lunes<br>**Cuando** se sincroniza el miércoles<br>**Entonces** conserva la fecha de ocurrencia del lunes y registra además su fecha de recepción | EP02 |
| US12 | Reporte desde la web | **Como** trabajador administrativo **quiero** reportar desde el navegador **para** no depender del celular. | **Escenario: paridad de canal**<br>**Cuando** reporto desde la web<br>**Entonces** el hallazgo se crea con los mismos campos y reglas que desde la aplicación móvil | EP02 |
| US13 | Consulta de mis reportes | **Como** operario **quiero** ver los reportes que hice y su estado **para** saber si se atendieron. | **Escenario: alcance por rol**<br>**Dado** que tengo rol operario<br>**Cuando** consulto la lista de reportes<br>**Entonces** veo únicamente los míos | EP02 |

### EP03 — Gestión del hallazgo

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US14 | Bandeja de hallazgos | **Como** supervisor **quiero** ver todos los hallazgos de la empresa filtrados por estado, tipo y área **para** priorizar mi trabajo. | **Escenario: filtro por estado**<br>**Cuando** filtro por estado abierto<br>**Entonces** la lista muestra solo los hallazgos sin atender | EP03 |
| US15 | Asignación de responsable | **Como** supervisor **quiero** asignar un responsable al hallazgo **para** que alguien se haga cargo de la corrección. | **Escenario: asignación**<br>**Cuando** asigno un responsable<br>**Entonces** el hallazgo pasa a estado en proceso y queda registrado en la bitácora quién asignó, a quién y cuándo | EP03 |
| US16 | Cierre con acción correctiva | **Como** supervisor **quiero** cerrar el hallazgo describiendo la acción aplicada **para** dejar evidencia de la corrección. | **Escenario: cierre**<br>**Cuando** cierro el hallazgo con la acción correctiva<br>**Entonces** el sistema registra la fecha de cierre y calcula el tiempo de resolución | EP03 |
| US17 | Separación de responsabilidades | **Como** empresa **quiero** que quien reporta no sea quien valida el cierre **para** cumplir el control que exige la normativa. | **Escenario: operario intenta cerrar**<br>**Dado** que tengo rol operario<br>**Cuando** intento cerrar un hallazgo<br>**Entonces** el sistema deniega la operación | EP03 |
| US18 | Bitácora del hallazgo | **Como** auditor interno **quiero** ver la secuencia completa de acciones sobre un hallazgo **para** verificar la trazabilidad. | **Escenario: historial**<br>**Cuando** abro el detalle de un hallazgo<br>**Entonces** veo en orden cronológico el reporte, las asignaciones, los comentarios y el cierre, cada uno con su autor y fecha | EP03 |

