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

### EP04 — Matriz IPERC

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US19 | Consulta de la matriz en campo | **Como** operario **quiero** consultar los peligros y controles de mi puesto desde el celular **para** saber cómo trabajar seguro. | **Escenario: consulta**<br>**Cuando** abro la matriz IPERC<br>**Entonces** veo los peligros con su nivel de riesgo y los controles existentes | EP04 |
| US20 | Registro de peligros | **Como** supervisor **quiero** agregar y editar entradas de la matriz **para** mantenerla actualizada. | **Escenario: cálculo del nivel**<br>**Cuando** registro una entrada con probabilidad y consecuencia<br>**Entonces** el sistema calcula el puntaje y el nivel de riesgo resultante | EP04 |
| US21 | Versionado de la matriz | **Como** responsable de SST **quiero** que la matriz se versione **para** mostrar su histórico ante una auditoría. | **Escenario: nueva versión**<br>**Cuando** creo una nueva matriz<br>**Entonces** el sistema le asigna el número de versión siguiente y conserva la anterior | EP04 |
| US22 | Trazabilidad con el hallazgo de origen | **Como** miembro del comité **quiero** saber qué entradas de la matriz nacieron de un hallazgo real **para** demostrar que la matriz se alimenta del campo. | **Escenario: origen**<br>**Cuando** una entrada proviene de un reporte<br>**Entonces** el sistema muestra el número de ese reporte y permite abrirlo | EP04 |

### EP05 — Control de EPP

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US23 | Catálogo de EPP | **Como** supervisor **quiero** registrar los EPP con su vida útil **para** controlar reposiciones. | **Escenario: alta de EPP**<br>**Cuando** registro un EPP con su vida útil en días<br>**Entonces** queda disponible para registrar entregas | EP05 |
| US24 | Registro de entrega | **Como** supervisor **quiero** registrar la entrega de un EPP a un trabajador **para** cumplir el registro obligatorio de la ley. | **Escenario: vencimiento automático**<br>**Cuando** registro una entrega<br>**Entonces** el sistema calcula la fecha de vencimiento a partir de la vida útil del EPP | EP05 |
| US25 | Conformidad del trabajador | **Como** operario **quiero** dar conformidad de la entrega desde mi celular **para** que quede constancia sin firmar papeles. | **Escenario: conformidad**<br>**Dado** que soy el trabajador de la entrega<br>**Cuando** doy conformidad<br>**Entonces** la entrega queda marcada como conforme con la fecha | EP05 |
| US26 | Alerta de EPP vencido | **Como** supervisor **quiero** identificar los EPP vencidos **para** reponerlos antes de que generen un riesgo. | **Escenario: marca de vencido**<br>**Cuando** la fecha de vencimiento es anterior a hoy<br>**Entonces** la entrega se muestra destacada como vencida | EP05 |

### EP06 — Inspecciones periódicas

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US27 | Programa de inspecciones | **Como** supervisor **quiero** definir qué se inspecciona, cada cuánto y con qué checklist **para** sistematizar el programa anual. | **Escenario: alta de programa**<br>**Cuando** creo un programa con área, frecuencia y checklist<br>**Entonces** queda disponible para generar sus ocurrencias | EP06 |
| US28 | Ejecución con checklist | **Como** inspector **quiero** realizar la inspección marcando el checklist desde el celular **para** registrarla en el lugar y no después. | **Escenario: ejecución**<br>**Cuando** marco los ítems y registro los hallazgos<br>**Entonces** la inspección queda como realizada con su fecha y responsable | EP06 |
| US29 | Inspecciones vencidas | **Como** responsable de SST **quiero** ver las inspecciones que pasaron su fecha sin realizarse **para** actuar sobre el incumplimiento. | **Escenario: vencida**<br>**Dado** que la fecha programada ya pasó y la inspección sigue pendiente<br>**Entonces** el sistema la marca como vencida | EP06 |

### EP07 — Comité de SST

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US30 | Constitución del comité | **Como** responsable de SST **quiero** registrar el comité y su periodo **para** documentar su vigencia. | **Escenario: modo supervisor**<br>**Dado** que la empresa tiene menos de 20 trabajadores<br>**Cuando** registro el comité<br>**Entonces** el sistema lo marca como modo supervisor, conforme admite la ley | EP07 |
| US31 | Miembros y paridad | **Como** responsable de SST **quiero** registrar los miembros con su cargo y representación **para** verificar que el comité sea paritario. | **Escenario: verificación de paridad**<br>**Cuando** el número de representantes del empleador difiere del de los trabajadores<br>**Entonces** el sistema advierte que el comité no es paritario | EP07 |
| US32 | Acta de reunión | **Como** secretario del comité **quiero** registrar el acta con agenda, asistentes y desarrollo **para** cumplir con el registro obligatorio. | **Escenario: numeración correlativa**<br>**Cuando** registro una nueva acta<br>**Entonces** el sistema le asigna el número consecutivo siguiente, sin aceptarlo del cliente | EP07 |
| US33 | Control de quórum | **Como** miembro del comité **quiero** saber si la reunión alcanzó quórum **para** conocer la validez del acta. | **Escenario: sin quórum**<br>**Dado** que asistieron menos de la mitad más uno de los titulares<br>**Entonces** el acta se muestra marcada como sin quórum | EP07 |
| US34 | Acuerdos con responsable y plazo | **Como** presidente del comité **quiero** registrar los acuerdos con responsable y plazo **para** hacerles seguimiento. | **Escenario: seguimiento**<br>**Cuando** actualizo el estado de un acuerdo a cumplido<br>**Entonces** el indicador de cumplimiento de acuerdos se recalcula | EP07 |

### EP08 — Métricas y evidencia

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US35 | Indicador MTTR | **Como** responsable de SST **quiero** conocer el tiempo promedio entre el reporte y el cierre **para** evaluar la capacidad de respuesta. | **Escenario: cálculo**<br>**Cuando** consulto el tablero<br>**Entonces** veo el MTTR del periodo, total y desagregado por severidad | EP08 |
| US36 | Tasa de cumplimiento de inspecciones | **Como** responsable de SST **quiero** conocer qué proporción de inspecciones programadas se realizó **para** detectar áreas que incumplen. | **Escenario: desagregación**<br>**Cuando** consulto el indicador<br>**Entonces** veo el total y el detalle por área | EP08 |
| US37 | Exportación de evidencia | **Como** responsable de SST **quiero** exportar a Excel los registros obligatorios **para** preparar el expediente de una inspección de SUNAFIL. | **Escenario: exportación**<br>**Cuando** exporto el registro de actos y condiciones inseguras<br>**Entonces** obtengo un archivo .xlsx con los campos del registro y su trazabilidad<br><br>**Escenario: permiso**<br>**Dado** que tengo rol operario<br>**Cuando** intento exportar<br>**Entonces** el sistema deniega la operación | EP08 |

### EP09 — Experimento A/B

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| US38 | Asignación de variante | **Como** equipo de producto **quiero** que cada usuario quede asignado de forma estable a una variante **para** que la comparación sea válida. | **Escenario: estabilidad**<br>**Cuando** el mismo usuario consulta su variante en distintos momentos<br>**Entonces** obtiene siempre la misma | EP09 |
| US39 | Registro de la variante en el reporte | **Como** analista **quiero** saber con qué formulario se creó cada reporte **para** atribuir correctamente los resultados. | **Escenario: atribución**<br>**Cuando** se crea un reporte<br>**Entonces** queda registrada la variante del formulario utilizado | EP09 |
| US40 | Resultados del experimento | **Como** analista **quiero** comparar los reportes por usuario de cada variante **para** contrastar la hipótesis. | **Escenario: comparación**<br>**Cuando** consulto los resultados<br>**Entonces** veo, por variante, el número de usuarios, de reportes, el promedio por usuario y la diferencia porcentual | EP09 |

### Historias técnicas

| ID | Título | Descripción | Criterios de aceptación | Épica |
|---|---|---|---|---|
| TS01 | Integración continua | **Como** equipo de desarrollo **quiero** que cada Pull Request ejecute pruebas y análisis estático **para** no integrar código roto. | **Escenario: PR con pruebas fallidas**<br>**Cuando** abro un PR cuyas pruebas fallan<br>**Entonces** el pipeline marca el PR en rojo y bloquea la integración | — |
| TS02 | Convenciones de commits | **Como** equipo **quiero** que los mensajes de commit sigan Conventional Commits **para** mantener un historial legible y auditable. | **Escenario: mensaje inválido**<br>**Cuando** intento commitear con un mensaje fuera del formato<br>**Entonces** el hook local lo rechaza y el workflow de CI también | — |
| TS03 | Documentación viva del API | **Como** desarrollador de los clientes **quiero** una especificación OpenAPI generada del código **para** que el contrato no se desactualice. | **Escenario: documentación**<br>**Cuando** accedo a la ruta de documentación<br>**Entonces** obtengo la especificación de todos los endpoints vigentes | — |
| TS04 | Datos de demostración | **Como** equipo **quiero** un comando que genere datos realistas **para** poder demostrar y probar el sistema. | **Escenario: carga**<br>**Cuando** ejecuto el comando de carga<br>**Entonces** el sistema queda con empresa, usuarios, reportes, IPERC, EPP, inspecciones y actas de ejemplo, claramente identificados como datos de demostración | — |

## 3.3. Product Backlog

Orden por prioridad de negocio. La estimación usa Story Points en escala de Fibonacci.

| # | ID | Historia | Épica | Story Points |
|---|---|---|---|---|
| 1 | US02 | Inicio de sesión | EP01 | 3 |
| 2 | US06 | Reporte rápido desde el celular | EP02 | 8 |
| 3 | US07 | Reporte sin conexión | EP02 | 13 |
| 4 | US08 | Sincronización sin duplicados | EP02 | 8 |
| 5 | US14 | Bandeja de hallazgos | EP03 | 5 |
| 6 | US16 | Cierre con acción correctiva | EP03 | 5 |
| 7 | US15 | Asignación de responsable | EP03 | 5 |
| 8 | US17 | Separación de responsabilidades | EP03 | 3 |
| 9 | US09 | Evidencia fotográfica | EP02 | 5 |
| 10 | US13 | Consulta de mis reportes | EP02 | 3 |
| 11 | US35 | Indicador MTTR | EP08 | 5 |
| 12 | US18 | Bitácora del hallazgo | EP03 | 3 |
| 13 | US10 | Geolocalización del hallazgo | EP02 | 5 |
| 14 | US11 | Fecha real de ocurrencia | EP02 | 3 |
| 15 | US38 | Asignación de variante | EP09 | 5 |
| 16 | US39 | Registro de la variante en el reporte | EP09 | 2 |
| 17 | US40 | Resultados del experimento | EP09 | 5 |
| 18 | US01 | Registro de trabajador | EP01 | 5 |
| 19 | US03 | Sesión persistente en campo | EP01 | 3 |
| 20 | US05 | Gestión de áreas | EP01 | 2 |
| 21 | US04 | Administración de usuarios | EP01 | 5 |
| 22 | US12 | Reporte desde la web | EP02 | 5 |
| 23 | US27 | Programa de inspecciones | EP06 | 5 |
| 24 | US28 | Ejecución con checklist | EP06 | 5 |
| 25 | US29 | Inspecciones vencidas | EP06 | 3 |
| 26 | US36 | Tasa de cumplimiento de inspecciones | EP08 | 5 |
| 27 | US20 | Registro de peligros | EP04 | 5 |
| 28 | US19 | Consulta de la matriz en campo | EP04 | 3 |
| 29 | US21 | Versionado de la matriz | EP04 | 3 |
| 30 | US22 | Trazabilidad con el hallazgo de origen | EP04 | 3 |
| 31 | US23 | Catálogo de EPP | EP05 | 3 |
| 32 | US24 | Registro de entrega | EP05 | 3 |
| 33 | US25 | Conformidad del trabajador | EP05 | 3 |
| 34 | US26 | Alerta de EPP vencido | EP05 | 2 |
| 35 | US30 | Constitución del comité | EP07 | 3 |
| 36 | US31 | Miembros y paridad | EP07 | 5 |
| 37 | US32 | Acta de reunión | EP07 | 5 |
| 38 | US33 | Control de quórum | EP07 | 3 |
| 39 | US34 | Acuerdos con responsable y plazo | EP07 | 3 |
| 40 | US37 | Exportación de evidencia | EP08 | 8 |
| 41 | TS02 | Convenciones de commits | — | 2 |
| 42 | TS01 | Integración continua | — | 5 |
| 43 | TS03 | Documentación viva del API | — | 2 |
| 44 | TS04 | Datos de demostración | — | 5 |

**Total estimado:** 188 Story Points.

