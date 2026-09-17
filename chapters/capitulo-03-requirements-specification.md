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

El catálogo completo son **128 historias de usuario** agrupadas en **diecinueve épicas**, más
**34 historias técnicas**. Los criterios de aceptación siguen el formato Gherkin
(Dado / Cuando / Entonces).

Dos columnas ordenan la lectura:

- **Plataforma** indica dónde vive cada historia: `Web`, `Móvil`, `Ambas` o `—` cuando no tiene
  interfaz propia. Esa columna es la evidencia de la paridad exigida: para un mismo rol, ninguna
  capacidad existe en una plataforma y falta en la otra. Las historias marcadas con una sola
  plataforma lo están por una razón de dominio que se explica en la propia fila, no por una
  funcionalidad faltante. El reparto no es arbitrario: lo que ocurre en campo y con las manos
  ocupadas —reportar, consultar la matriz, ejecutar la inspección, firmar la entrega de EPP— es
  del operario y vive en el móvil; lo que exige pantalla grande y decisión —configurar el IPERC,
  redactar un acta, administrar usuarios, leer el tablero— es del supervisor y del comité, y vive
  en la web. Ambas plataformas comparten todo lo que un mismo rol necesita en los dos sitios.
- **Estado** separa tres situaciones. *Sprint 1* marca los quince elementos comprometidos y
  entregados en el sprint de este ciclo, que son los que detalla el Sprint Backlog del Capítulo V.
  *Implementada* marca lo que existe y es verificable en el código entregado pero no formó parte
  de ese compromiso: es avance sobre los siguientes sprints. *Propuesta* marca lo que está escrito
  y estimado pero todavía no se construye. Un backlog contiene siempre más de lo que cabe en un
  sprint; declarar por escrito cuál es cuál evita atribuirle al prototipo capacidades que no
  tiene, y evita también inflar la velocidad del sprint con trabajo que no se prometió.

Las historias técnicas (TS) corresponden a trabajo de infraestructura
sin valor directo para el usuario final pero necesario para sostener el producto.

### Épicas

| ID | Épica | Descripción | Historias | Alcance |
|---|---|---|---|---|
| EP01 | Acceso y cuentas | Registro, autenticación y administración de usuarios y roles. | 8 | Implementada |
| EP02 | Reporte de actos y condiciones inseguras | Captura del hallazgo en campo, con evidencia y operación sin conexión. | 14 | 13 implementadas, 1 propuestas |
| EP03 | Gestión del hallazgo | Seguimiento desde la recepción hasta el cierre verificado. | 8 | Implementada |
| EP04 | Matriz IPERC | Identificación de peligros, evaluación de riesgos y controles. | 7 | Implementada |
| EP05 | Control de EPP | Catálogo, entregas, vencimientos y conformidad del trabajador. | 6 | 5 implementadas, 1 propuestas |
| EP06 | Inspecciones periódicas | Programación, ejecución con checklist y cumplimiento. | 7 | 5 implementadas, 2 propuestas |
| EP07 | Comité de SST | Constitución, miembros, actas de reunión y acuerdos. | 10 | 8 implementadas, 2 propuestas |
| EP08 | Métricas y evidencia | Indicadores de gestión y exportación para auditorías. | 8 | 6 implementadas, 2 propuestas |
| EP09 | Experimento A/B | Asignación de variantes y medición de resultados. | 6 | 4 implementadas, 2 propuestas |
| EP10 | Calidad de uso y operación | Atributos transversales: consistencia visual, uso en campo, manejo de errores y respuesta ante fallos de red. | 8 | 6 implementadas, 2 propuestas |
| EP11 | Accidentes e incidentes | Registro e investigación de accidentes de trabajo, incidentes peligrosos y enfermedades ocupacionales, con notificación a la autoridad. | 8 | Propuesta |
| EP12 | Capacitación e inducción | Registro de inducción, capacitación, entrenamiento y simulacros de emergencia. | 6 | Propuesta |
| EP13 | Mapa de riesgos y señalización | Representación gráfica de los riesgos por área y control de la señalización obligatoria. | 4 | Propuesta |
| EP14 | Documentación del SGSST | Política de SST, Reglamento Interno, plan y programa anual, y su control de versiones. | 4 | Propuesta |
| EP15 | Monitoreo de agentes ocupacionales | Mediciones de agentes físicos, químicos, biológicos, ergonómicos y psicosociales. | 3 | Propuesta |
| EP16 | Contratistas y terceros | Gestión de empresas contratistas, sus trabajadores y su documentación de seguridad. | 4 | Propuesta |
| EP17 | Notificaciones y alertas | Avisos automáticos sobre hallazgos críticos, vencimientos y compromisos del comité. | 6 | Propuesta |
| EP18 | Cuenta y servicio | Alta de empresas, suscripción, respaldo y continuidad del servicio. | 5 | Propuesta |
| EP19 | Seguridad y privacidad de datos | Protección de datos personales, trazabilidad de accesos y control de sesiones. | 6 | Propuesta |

Las épicas EP01 a EP10 son las que el equipo construyó en este ciclo. Las épicas EP11 a EP19 cubren las obligaciones de la Ley N° 29783 y su Reglamento que el producto todavía no atiende —registro e investigación de accidentes, capacitación, mapa de riesgos, documentación del sistema de gestión, monitoreo de agentes, contratistas, notificaciones, gestión de la cuenta y protección de datos personales— y quedan especificadas para los siguientes ciclos.

### EP01 — Acceso y cuentas

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US01 | Registro de trabajador | **Como** trabajador **quiero** crear mi cuenta indicando el RUC de mi empresa **para** empezar a reportar sin depender de que alguien me la cree. | **Escenario: registro exitoso**<br>**Dado** que ingreso al formulario de registro<br>**Cuando** completo mis datos y el RUC de una empresa registrada<br>**Entonces** el sistema crea mi cuenta con rol operario y me deja dentro de la aplicación<br><br>**Escenario: RUC inexistente**<br>**Dado** que ingreso un RUC no registrado<br>**Cuando** envío el formulario<br>**Entonces** el sistema me indica que debo solicitar el RUC a mi supervisor y no crea la cuenta | Ambas | Implementada | EP01|
| US02 | Inicio de sesión | **Como** usuario **quiero** iniciar sesión con usuario y contraseña **para** acceder a la información de mi empresa. | **Escenario: credenciales válidas**<br>**Dado** que tengo una cuenta activa<br>**Cuando** ingreso mis credenciales correctas<br>**Entonces** el sistema me autentica y me lleva a la pantalla inicial de mi rol<br><br>**Escenario: credenciales inválidas**<br>**Cuando** ingreso credenciales incorrectas<br>**Entonces** el sistema muestra un mensaje de error sin revelar si el usuario existe | Ambas | Sprint 1 | EP01|
| US03 | Sesión persistente en campo | **Como** operario **quiero** permanecer autenticado varios días **para** no tener que iniciar sesión cuando estoy en una zona sin señal. | **Escenario: renovación automática**<br>**Dado** que mi token de acceso expiró<br>**Cuando** la aplicación realiza una petición<br>**Entonces** el sistema renueva el token automáticamente y la petición se completa sin pedirme la contraseña | Ambas | Implementada | EP01|
| US04 | Administración de usuarios | **Como** supervisor de SST **quiero** crear usuarios y asignarles rol **para** incorporar al equipo de seguridad con los permisos correctos. | **Escenario: alta de supervisor**<br>**Dado** que tengo rol de supervisor<br>**Cuando** creo un usuario con rol supervisor<br>**Entonces** el usuario queda creado en mi empresa con ese rol<br><br>**Escenario: operario sin permiso**<br>**Dado** que tengo rol operario<br>**Cuando** intento listar los usuarios<br>**Entonces** el sistema deniega el acceso | Web | Implementada | EP01|
| US05 | Gestión de áreas | **Como** supervisor **quiero** registrar las áreas o frentes de trabajo **para** clasificar los hallazgos por ubicación organizativa. | **Escenario: alta de área**<br>**Cuando** registro un área con nombre y descripción<br>**Entonces** queda disponible para clasificar reportes, inspecciones y entradas IPERC | Web | Implementada | EP01|
| US41 | Cambio de rol de un usuario | **Como** supervisor **quiero** cambiar el rol de un usuario existente **para** incorporarlo al comité sin crearle una cuenta nueva. | **Cuando** cambio el rol desde la pantalla de usuarios<br>**Entonces** el usuario pasa a tener los permisos de ese rol en web y en móvil | Web | Implementada | EP01|
| US42 | Cierre de sesión | **Como** usuario **quiero** cerrar sesión **para** que nadie use mi cuenta en un equipo compartido. | **Cuando** cierro sesión<br>**Entonces** el sistema descarta mis credenciales y me devuelve a la pantalla de acceso | Ambas | Implementada | EP01|
| US43 | Menú según mi rol | **Como** operario **quiero** ver solo las opciones que me corresponden **para** no perderme entre funciones que no puedo usar. | **Dado** que tengo rol operario<br>**Entonces** el menú muestra únicamente reportar, mis reportes, mis EPP y las consultas, y no las opciones de gestión | Ambas | Sprint 1 | EP01|
### EP02 — Reporte de actos y condiciones inseguras

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US06 | Reporte rápido desde el celular | **Como** operario **quiero** reportar un peligro en tres toques con una foto **para** no perder tiempo de trabajo. | **Escenario: reporte en tres pasos**<br>**Dado** que estoy en el frente de trabajo<br>**Cuando** elijo el tipo de hallazgo, la categoría y tomo la foto<br>**Entonces** el sistema registra el reporte y me confirma que quedó guardado<br><br>**Escenario: descripción opcional**<br>**Cuando** envío el reporte sin escribir descripción<br>**Entonces** el sistema lo acepta igualmente | Ambas | Sprint 1 | EP02|
| US07 | Reporte sin conexión | **Como** operario en obra o mina **quiero** que mi reporte se guarde aunque no haya señal **para** no perderlo. | **Escenario: sin conectividad**<br>**Dado** que el dispositivo no tiene conexión<br>**Cuando** envío el reporte<br>**Entonces** se almacena localmente y se muestra como pendiente de envío<br><br>**Escenario: recuperación de señal**<br>**Cuando** el dispositivo recupera la conexión<br>**Entonces** el sistema sincroniza los reportes pendientes sin intervención del usuario | Móvil | Implementada | EP02|
| US08 | Sincronización sin duplicados | **Como** responsable de SST **quiero** que un reintento de envío no genere reportes repetidos **para** que las métricas sean confiables. | **Escenario: reintento del mismo reporte**<br>**Dado** un reporte con un identificador de cliente ya recibido<br>**Cuando** el dispositivo reintenta el envío<br>**Entonces** el sistema devuelve el reporte existente y no crea uno nuevo | Ambas | Implementada | EP02|
| US09 | Evidencia fotográfica | **Como** miembro del comité **quiero** ver la foto del hallazgo **para** entender el peligro sin desplazarme al lugar. | **Escenario: foto adjunta**<br>**Cuando** abro el detalle de un reporte con foto<br>**Entonces** veo la imagen y puedo ampliarla a pantalla completa | Ambas | Sprint 1 | EP02|
| US10 | Geolocalización del hallazgo | **Como** supervisor **quiero** saber dónde ocurrió el hallazgo **para** ubicarlo dentro de la operación. | **Escenario: captura de coordenadas**<br>**Cuando** el operario autoriza la ubicación al tomar la foto<br>**Entonces** el reporte guarda latitud y longitud y el panel ofrece verlas en un mapa<br><br>**Escenario: permiso denegado**<br>**Cuando** el operario no autoriza la ubicación<br>**Entonces** el reporte se envía igualmente, sin coordenadas | Ambas | Sprint 1 | EP02|
| US11 | Fecha real de ocurrencia | **Como** analista **quiero** que el reporte conserve la fecha en que ocurrió el hecho **para** que el indicador de tiempo de respuesta no se distorsione. | **Escenario: sincronización diferida**<br>**Dado** un reporte creado sin conexión el lunes<br>**Cuando** se sincroniza el miércoles<br>**Entonces** conserva la fecha de ocurrencia del lunes y registra además su fecha de recepción | Ambas | Sprint 1 | EP02|
| US12 | Reporte desde la web | **Como** trabajador administrativo **quiero** reportar desde el navegador **para** no depender del celular. | **Escenario: paridad de canal**<br>**Cuando** reporto desde la web<br>**Entonces** el hallazgo se crea con los mismos campos y reglas que desde la aplicación móvil | Web | Implementada | EP02|
| US13 | Consulta de mis reportes | **Como** operario **quiero** ver los reportes que hice y su estado **para** saber si se atendieron. | **Escenario: alcance por rol**<br>**Dado** que tengo rol operario<br>**Cuando** consulto la lista de reportes<br>**Entonces** veo únicamente los míos | Ambas | Sprint 1 | EP02|
| US44 | Vista previa de la evidencia | **Como** quien reporta **quiero** ver en pequeño la foto que elegí **para** confirmar que subí la correcta antes de enviar. | **Cuando** elijo una imagen<br>**Entonces** se muestra una miniatura con el nombre y el peso del archivo | Web | Implementada | EP02|
| US45 | Ampliar la evidencia | **Como** miembro del comité **quiero** ampliar la foto a pantalla completa **para** distinguir el detalle del peligro. | **Cuando** toco la imagen<br>**Entonces** se abre a pantalla completa y se cierra con Escape o tocando fuera | Web | Implementada | EP02|
| US46 | Reemplazar la foto elegida | **Como** quien reporta **quiero** quitar la foto y elegir otra **para** corregirme sin perder lo ya escrito. | **Cuando** quito la foto<br>**Entonces** el formulario conserva el resto de los datos y admite elegir una imagen nueva, incluso la misma | Web | Implementada | EP02|
| US47 | Categorías según el tipo de hallazgo | **Como** quien reporta **quiero** ver solo las categorías que aplican **para** no equivocarme entre actos y condiciones. | **Dado** que elegí condición insegura<br>**Entonces** solo se ofrecen categorías de condición | Ambas | Sprint 1 | EP02|
| US48 | Estado de envío de mis reportes | **Como** operario **quiero** saber cuántos reportes tengo sin enviar **para** confiar en que no se perdieron. | **Dado** que hay reportes en la cola local<br>**Entonces** la pantalla muestra cuántos esperan señal, y cada uno indica si ya se envió | Móvil | Implementada | EP02|

### EP03 — Gestión del hallazgo

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US14 | Bandeja de hallazgos | **Como** supervisor **quiero** ver todos los hallazgos de la empresa filtrados por estado, tipo y área **para** priorizar mi trabajo. | **Escenario: filtro por estado**<br>**Cuando** filtro por estado abierto<br>**Entonces** la lista muestra solo los hallazgos sin atender | Ambas | Sprint 1 | EP03|
| US15 | Asignación de responsable | **Como** supervisor **quiero** asignar un responsable al hallazgo **para** que alguien se haga cargo de la corrección. | **Escenario: asignación**<br>**Cuando** asigno un responsable<br>**Entonces** el hallazgo pasa a estado en proceso y queda registrado en la bitácora quién asignó, a quién y cuándo | Ambas | Sprint 1 | EP03|
| US16 | Cierre con acción correctiva | **Como** supervisor **quiero** cerrar el hallazgo describiendo la acción aplicada **para** dejar evidencia de la corrección. | **Escenario: cierre**<br>**Cuando** cierro el hallazgo con la acción correctiva<br>**Entonces** el sistema registra la fecha de cierre y calcula el tiempo de resolución | Ambas | Sprint 1 | EP03|
| US17 | Separación de responsabilidades | **Como** empresa **quiero** que quien reporta no sea quien valida el cierre **para** cumplir el control que exige la normativa. | **Escenario: operario intenta cerrar**<br>**Dado** que tengo rol operario<br>**Cuando** intento cerrar un hallazgo<br>**Entonces** el sistema deniega la operación | Ambas | Implementada | EP03|
| US18 | Bitácora del hallazgo | **Como** auditor interno **quiero** ver la secuencia completa de acciones sobre un hallazgo **para** verificar la trazabilidad. | **Escenario: historial**<br>**Cuando** abro el detalle de un hallazgo<br>**Entonces** veo en orden cronológico el reporte, las asignaciones, los comentarios y el cierre, cada uno con su autor y fecha | Ambas | Sprint 1 | EP03|
| US49 | Descartar un reporte | **Como** supervisor **quiero** descartar un reporte que no corresponde a un hallazgo de SST **para** que no distorsione los indicadores. | **Cuando** descarto un reporte<br>**Entonces** pasa a estado descartado, queda registrado en la bitácora y deja de contarse como hallazgo abierto | Web | Implementada | EP03|
| US50 | Filtrar la bandeja | **Como** supervisor **quiero** filtrar por estado, tipo y área **para** trabajar por lotes en lugar de revisar todo. | **Cuando** aplico un filtro<br>**Entonces** la lista se reduce a los hallazgos que lo cumplen y el total se actualiza | Ambas | Implementada | EP03|
| US51 | Ubicar el hallazgo en el mapa | **Como** supervisor **quiero** abrir la ubicación del hallazgo en un mapa **para** llegar al punto exacto. | **Dado** que el reporte tiene coordenadas<br>**Entonces** el detalle ofrece un enlace que abre esa posición en un mapa | Web | Implementada | EP03|

### EP04 — Matriz IPERC

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US19 | Consulta de la matriz en campo | **Como** operario **quiero** consultar los peligros y controles de mi puesto desde el celular **para** saber cómo trabajar seguro. | **Escenario: consulta**<br>**Cuando** abro la matriz IPERC<br>**Entonces** veo los peligros con su nivel de riesgo y los controles existentes | Ambas | Implementada | EP04|
| US20 | Registro de peligros | **Como** supervisor **quiero** agregar y editar entradas de la matriz **para** mantenerla actualizada. | **Escenario: cálculo del nivel**<br>**Cuando** registro una entrada con probabilidad y consecuencia<br>**Entonces** el sistema calcula el puntaje y el nivel de riesgo resultante | Web | Implementada | EP04|
| US21 | Versionado de la matriz | **Como** responsable de SST **quiero** que la matriz se versione **para** mostrar su histórico ante una auditoría. | **Escenario: nueva versión**<br>**Cuando** creo una nueva matriz<br>**Entonces** el sistema le asigna el número de versión siguiente y conserva la anterior | Web | Implementada | EP04|
| US22 | Trazabilidad con el hallazgo de origen | **Como** miembro del comité **quiero** saber qué entradas de la matriz nacieron de un hallazgo real **para** demostrar que la matriz se alimenta del campo. | **Escenario: origen**<br>**Cuando** una entrada proviene de un reporte<br>**Entonces** el sistema muestra el número de ese reporte y permite abrirlo | Ambas | Implementada | EP04|
| US52 | Consultar versiones anteriores de la matriz | **Como** auditor interno **quiero** consultar versiones anteriores de la IPERC **para** verificar cómo evolucionaron los controles. | **Cuando** elijo una versión en el selector<br>**Entonces** la tabla muestra las entradas de esa versión y advierte que es histórica | Web | Implementada | EP04|
| US53 | Publicar una nueva versión de la matriz | **Como** responsable de SST **quiero** crear una versión nueva y ponerla vigente **para** actualizar la matriz sin borrar la anterior. | **Cuando** pongo vigente una versión<br>**Entonces** la anterior pasa a histórica y solo queda una vigente<br><br>**Escenario: versión histórica**<br>**Dado** que consulto una versión histórica<br>**Entonces** el sistema no permite editarla | Web | Implementada | EP04|
| US54 | Retirar un peligro de la matriz | **Como** responsable de SST **quiero** quitar una entrada que ya no aplica **para** que la matriz refleje la operación actual. | **Cuando** quito una entrada de la versión vigente<br>**Entonces** desaparece de la matriz y las versiones históricas la conservan | Web | Implementada | EP04|

### EP05 — Control de EPP

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US23 | Catálogo de EPP | **Como** supervisor **quiero** registrar los EPP con su vida útil **para** controlar reposiciones. | **Escenario: alta de EPP**<br>**Cuando** registro un EPP con su vida útil en días<br>**Entonces** queda disponible para registrar entregas | Web | Implementada | EP05|
| US24 | Registro de entrega | **Como** supervisor **quiero** registrar la entrega de un EPP a un trabajador **para** cumplir el registro obligatorio de la ley. | **Escenario: vencimiento automático**<br>**Cuando** registro una entrega<br>**Entonces** el sistema calcula la fecha de vencimiento a partir de la vida útil del EPP | Web | Implementada | EP05|
| US25 | Conformidad del trabajador | **Como** operario **quiero** dar conformidad de la entrega desde mi celular **para** que quede constancia sin firmar papeles. | **Escenario: conformidad**<br>**Dado** que soy el trabajador de la entrega<br>**Cuando** doy conformidad<br>**Entonces** la entrega queda marcada como conforme con la fecha | Ambas | Implementada | EP05|
| US26 | Alerta de EPP vencido | **Como** supervisor **quiero** identificar los EPP vencidos **para** reponerlos antes de que generen un riesgo. | **Escenario: marca de vencido**<br>**Cuando** la fecha de vencimiento es anterior a hoy<br>**Entonces** la entrega se muestra destacada como vencida | Ambas | Implementada | EP05|
| US55 | Control de stock del catálogo | **Como** supervisor **quiero** ver el stock y la vida útil de cada EPP **para** anticipar reposiciones. | **Cuando** abro el catálogo<br>**Entonces** veo por cada EPP su vida útil, su stock y cuántas entregas acumula | Web | Implementada | EP05|

### EP06 — Inspecciones periódicas

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US27 | Programa de inspecciones | **Como** supervisor **quiero** definir qué se inspecciona, cada cuánto y con qué checklist **para** sistematizar el programa anual. | **Escenario: alta de programa**<br>**Cuando** creo un programa con área, frecuencia y checklist<br>**Entonces** queda disponible para generar sus ocurrencias | Web | Implementada | EP06|
| US28 | Ejecución con checklist | **Como** inspector **quiero** realizar la inspección marcando el checklist desde el celular **para** registrarla en el lugar y no después. | **Escenario: ejecución**<br>**Cuando** marco los ítems y registro los hallazgos<br>**Entonces** la inspección queda como realizada con su fecha y responsable | Ambas | Implementada | EP06|
| US29 | Inspecciones vencidas | **Como** responsable de SST **quiero** ver las inspecciones que pasaron su fecha sin realizarse **para** actuar sobre el incumplimiento. | **Escenario: vencida**<br>**Dado** que la fecha programada ya pasó y la inspección sigue pendiente<br>**Entonces** el sistema la marca como vencida | Ambas | Implementada | EP06|
| US56 | Programar la siguiente inspección | **Como** supervisor **quiero** generar la siguiente ocurrencia según la frecuencia **para** no calcular fechas a mano. | **Cuando** genero la siguiente<br>**Entonces** el sistema crea la ocurrencia con la fecha que corresponde a la frecuencia del programa | Web | Implementada | EP06|
| US57 | Cumplimiento por área | **Como** responsable de SST **quiero** ver el cumplimiento desagregado por área **para** actuar sobre la que incumple. | **Cuando** consulto el indicador<br>**Entonces** veo programadas, realizadas y porcentaje por cada área | Web | Implementada | EP06|

### EP07 — Comité de SST

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US30 | Constitución del comité | **Como** responsable de SST **quiero** registrar el comité y su periodo **para** documentar su vigencia. | **Escenario: modo supervisor**<br>**Dado** que la empresa tiene menos de 20 trabajadores<br>**Cuando** registro el comité<br>**Entonces** el sistema lo marca como modo supervisor, conforme admite la ley | Web | Implementada | EP07|
| US31 | Miembros y paridad | **Como** responsable de SST **quiero** registrar los miembros con su cargo y representación **para** verificar que el comité sea paritario. | **Escenario: verificación de paridad**<br>**Cuando** el número de representantes del empleador difiere del de los trabajadores<br>**Entonces** el sistema advierte que el comité no es paritario | Web | Implementada | EP07|
| US32 | Acta de reunión | **Como** secretario del comité **quiero** registrar el acta con agenda, asistentes y desarrollo **para** cumplir con el registro obligatorio. | **Escenario: numeración correlativa**<br>**Cuando** registro una nueva acta<br>**Entonces** el sistema le asigna el número consecutivo siguiente, sin aceptarlo del cliente | Web | Implementada | EP07|
| US33 | Control de quórum | **Como** miembro del comité **quiero** saber si la reunión alcanzó quórum **para** conocer la validez del acta. | **Escenario: sin quórum**<br>**Dado** que asistieron menos de la mitad más uno de los titulares<br>**Entonces** el acta se muestra marcada como sin quórum | Ambas | Implementada | EP07|
| US34 | Acuerdos con responsable y plazo | **Como** presidente del comité **quiero** registrar los acuerdos con responsable y plazo **para** hacerles seguimiento. | **Escenario: seguimiento**<br>**Cuando** actualizo el estado de un acuerdo a cumplido<br>**Entonces** el indicador de cumplimiento de acuerdos se recalcula | Web | Implementada | EP07|
| US58 | Advertencia de comité no paritario | **Como** responsable de SST **quiero** que el sistema me advierta si el comité no es paritario **para** corregirlo antes de una fiscalización. | **Dado** que los representantes del empleador y de los trabajadores no son iguales en número<br>**Entonces** la pantalla muestra una advertencia explicando qué exige la ley | Web | Implementada | EP07|
| US59 | Seguimiento del estado de los acuerdos | **Como** presidente del comité **quiero** actualizar el estado de cada acuerdo **para** reflejar su avance real. | **Cuando** cambio el estado de un acuerdo<br>**Entonces** el indicador de cumplimiento del comité se recalcula | Web | Implementada | EP07|
| US60 | Consultar las actas desde el celular | **Como** trabajador **quiero** leer las actas y acuerdos del comité desde mi celular **para** enterarme de lo que se decidió. | **Cuando** abro la sección del comité<br>**Entonces** veo las actas con su fecha, quórum y acuerdos | Móvil | Implementada | EP07|

### EP08 — Métricas y evidencia

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US35 | Indicador MTTR | **Como** responsable de SST **quiero** conocer el tiempo promedio entre el reporte y el cierre **para** evaluar la capacidad de respuesta. | **Escenario: cálculo**<br>**Cuando** consulto el tablero<br>**Entonces** veo el MTTR del periodo, total y desagregado por severidad | Ambas | Implementada | EP08|
| US36 | Tasa de cumplimiento de inspecciones | **Como** responsable de SST **quiero** conocer qué proporción de inspecciones programadas se realizó **para** detectar áreas que incumplen. | **Escenario: desagregación**<br>**Cuando** consulto el indicador<br>**Entonces** veo el total y el detalle por área | Ambas | Implementada | EP08|
| US37 | Exportación de evidencia | **Como** responsable de SST **quiero** exportar a Excel los registros obligatorios **para** preparar el expediente de una inspección de SUNAFIL. | **Escenario: exportación**<br>**Cuando** exporto el registro de actos y condiciones inseguras<br>**Entonces** obtengo un archivo .xlsx con los campos del registro y su trazabilidad<br><br>**Escenario: permiso**<br>**Dado** que tengo rol operario<br>**Cuando** intento exportar<br>**Entonces** el sistema deniega la operación | Web | Implementada | EP08|
| US61 | MTTR por severidad | **Como** responsable de SST **quiero** ver el MTTR desagregado por severidad **para** distinguir si los críticos se atienden rápido. | **Cuando** consulto el tablero<br>**Entonces** veo el MTTR total y una fila por severidad con su promedio y cantidad de cerrados | Ambas | Implementada | EP08|
| US62 | Exportar cada registro obligatorio | **Como** responsable de SST **quiero** exportar por separado reportes, IPERC, EPP, inspecciones y actas **para** armar el expediente por tipo de registro. | **Cuando** exporto cualquiera de los cinco<br>**Entonces** obtengo un archivo .xlsx con la cabecera y los datos de ese registro | Web | Implementada | EP08|
| US63 | Resumen de hallazgos | **Como** responsable de SST **quiero** un resumen por estado, tipo, severidad y área **para** ver la distribución del riesgo de un vistazo. | **Cuando** consulto el resumen<br>**Entonces** obtengo los conteos por cada dimensión y el total de críticos sin atender | Ambas | Implementada | EP08|

### EP09 — Experimento A/B

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US38 | Asignación de variante | **Como** equipo de producto **quiero** que cada usuario quede asignado de forma estable a una variante **para** que la comparación sea válida. | **Escenario: estabilidad**<br>**Cuando** el mismo usuario consulta su variante en distintos momentos<br>**Entonces** obtiene siempre la misma | Ambas | Implementada | EP09|
| US39 | Registro de la variante en el reporte | **Como** analista **quiero** saber con qué formulario se creó cada reporte **para** atribuir correctamente los resultados. | **Escenario: atribución**<br>**Cuando** se crea un reporte<br>**Entonces** queda registrada la variante del formulario utilizado | Ambas | Implementada | EP09|
| US40 | Resultados del experimento | **Como** analista **quiero** comparar los reportes por usuario de cada variante **para** contrastar la hipótesis. | **Escenario: comparación**<br>**Cuando** consulto los resultados<br>**Entonces** veo, por variante, el número de usuarios, de reportes, el promedio por usuario y la diferencia porcentual | Web | Implementada | EP09|
| US64 | Variante disponible sin conexión | **Como** operario **quiero** que la aplicación sepa qué formulario mostrarme aunque no tenga señal **para** poder reportar igual. | **Dado** que la variante se guardó al iniciar sesión<br>**Cuando** abro el formulario sin conexión<br>**Entonces** se muestra la variante que me corresponde | Móvil | Implementada | EP09|

### EP10 — Calidad de uso y operación

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US65 | Identidad visual consistente | **Como** usuario **quiero** una interfaz sobria y uniforme **para** confiar en que es un sistema de gestión formal y no un prototipo. | **Cuando** navego entre pantallas<br>**Entonces** encuentro la misma paleta, tipografía y tratamiento de estados en todas | Ambas | Implementada | EP10|
| US66 | Navegación siempre accesible | **Como** supervisor **quiero** que el menú permanezca visible al desplazarme **para** cambiar de sección sin volver arriba. | **Cuando** bajo por una tabla larga<br>**Entonces** la navegación sigue en pantalla | Ambas | Implementada | EP10|
| US67 | Uso desde pantallas pequeñas | **Como** supervisor en obra **quiero** usar el panel desde una pantalla angosta **para** no depender de la laptop. | **Cuando** reduzco el ancho de la ventana<br>**Entonces** la navegación pasa a barra superior y las tablas se desplazan sin romper el diseño | Web | Implementada | EP10|
| US68 | Errores comprensibles | **Como** usuario **quiero** entender qué salió mal **para** poder corregirlo yo mismo. | **Cuando** el servidor rechaza una operación<br>**Entonces** la pantalla muestra el motivo en lenguaje claro, indicando el campo cuando corresponde | Ambas | Implementada | EP10|
| US69 | Reintento ante fallo de red | **Como** operario **quiero** reintentar una consulta que falló **para** no tener que reiniciar la aplicación. | **Dado** que una pantalla no pudo cargar<br>**Entonces** muestra el motivo y un botón para reintentar | Móvil | Implementada | EP10|
| US70 | Sesión que no expira en campo | **Como** operario **quiero** seguir trabajando sin volver a iniciar sesión **para** no quedarme fuera en una zona sin señal. | **Cuando** mi token de acceso caduca<br>**Entonces** el sistema lo renueva automáticamente y la operación continúa | Ambas | Implementada | EP10|

### EP11 — Accidentes e incidentes

La Ley N° 29783 obliga a registrar e investigar los accidentes de trabajo, los incidentes
peligrosos y las enfermedades ocupacionales, y a notificar los mortales a la autoridad. Es el
registro obligatorio que el producto aún no cubre y el primero del backlog futuro.

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US71 | Registro de accidente de trabajo | **Como** supervisor de SST **quiero** registrar un accidente con fecha, hora, lugar, trabajadores involucrados y descripción **para** cumplir el registro obligatorio. | **Cuando** registro un accidente<br>**Entonces** queda con su número correlativo, su gravedad y los días de descanso médico asociados | Web | Propuesta | EP11 |
| US72 | Registro de incidente peligroso | **Como** supervisor **quiero** registrar un incidente peligroso que no causó lesión **para** actuar antes de que se repita con consecuencias. | **Cuando** registro un incidente peligroso<br>**Entonces** se clasifica como tal y entra al mismo ciclo de investigación | Ambas | Propuesta | EP11 |
| US73 | Reportar un accidente desde el celular | **Como** operario **quiero** dar aviso de un accidente desde el celular **para** que la ayuda y el registro empiecen de inmediato. | **Cuando** reporto un accidente<br>**Entonces** el supervisor recibe el aviso y el registro queda abierto para completarse | Móvil | Propuesta | EP11 |
| US74 | Investigación de causa raíz | **Como** miembro del comité **quiero** documentar la investigación con el método de los cinco porqués **para** llegar a la causa real y no a la aparente. | **Cuando** completo la investigación<br>**Entonces** el accidente queda con sus causas inmediatas, básicas y de gestión, y sus medidas correctivas | Web | Propuesta | EP11 |
| US75 | Medidas correctivas con responsable y plazo | **Como** supervisor **quiero** que cada medida correctiva tenga responsable y plazo **para** poder hacerles seguimiento. | **Cuando** registro una medida correctiva<br>**Entonces** aparece en el seguimiento con su estado hasta que se cierra | Web | Propuesta | EP11 |
| US76 | Aviso de accidente mortal dentro del plazo legal | **Como** empresa **quiero** que el sistema me alerte del plazo de notificación de un accidente mortal **para** no incurrir en infracción. | **Dado** que registro un accidente mortal<br>**Entonces** el sistema advierte el plazo de 24 horas para notificar a la autoridad y deja constancia de la fecha de aviso | Web | Propuesta | EP11 |
| US77 | Indicadores de accidentabilidad | **Como** responsable de SST **quiero** los índices de frecuencia, gravedad y accidentabilidad **para** reportarlos como exige la norma. | **Cuando** consulto las estadísticas del periodo<br>**Entonces** obtengo los tres índices calculados sobre las horas-hombre trabajadas | Ambas | Propuesta | EP11 |
| US78 | Registro de enfermedad ocupacional | **Como** responsable de SST **quiero** registrar una enfermedad ocupacional diagnosticada **para** completar el registro que la ley exige. | **Cuando** registro una enfermedad ocupacional<br>**Entonces** queda asociada al puesto y al agente que la origina, sin exponer el diagnóstico a usuarios sin autorización | Web | Propuesta | EP11 |

### EP12 — Capacitación e inducción

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US79 | Programa anual de capacitación | **Como** responsable de SST **quiero** planificar las capacitaciones del año **para** cumplir las cuatro anuales que exige la ley. | **Cuando** registro el programa<br>**Entonces** cada capacitación queda con su tema, fecha prevista, responsable y público objetivo | Web | Propuesta | EP12 |
| US80 | Registro de asistencia a capacitación | **Como** capacitador **quiero** registrar la asistencia desde el celular **para** no transcribir una hoja de firmas después. | **Cuando** marco a los asistentes<br>**Entonces** cada trabajador queda con su registro de capacitación y la sesión con su lista | Móvil | Propuesta | EP12 |
| US81 | Inducción del personal nuevo | **Como** supervisor **quiero** registrar la inducción de un trabajador que ingresa **para** evidenciar que no empezó a trabajar sin ella. | **Cuando** completo la inducción<br>**Entonces** el trabajador queda habilitado y la fecha se conserva como evidencia | Web | Propuesta | EP12 |
| US82 | Alerta de capacitación vencida | **Como** responsable de SST **quiero** saber qué trabajadores tienen capacitación vencida **para** reprogramarla antes de una fiscalización. | **Dado** que pasó la vigencia de una capacitación<br>**Entonces** el trabajador aparece en la lista de pendientes | Web | Propuesta | EP12 |
| US83 | Consultar mis capacitaciones | **Como** trabajador **quiero** ver qué capacitaciones tengo y cuáles me faltan **para** saber si estoy habilitado. | **Cuando** abro mi perfil<br>**Entonces** veo mis capacitaciones con su fecha y vigencia | Móvil | Propuesta | EP12 |
| US84 | Registro de simulacros | **Como** responsable de SST **quiero** registrar los simulacros de emergencia con sus resultados **para** cumplir el registro obligatorio. | **Cuando** registro un simulacro<br>**Entonces** queda con su tipo, fecha, participantes, tiempo de evacuación y observaciones | Web | Propuesta | EP12 |

### EP13 — Mapa de riesgos y señalización

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US85 | Mapa de riesgos por área | **Como** responsable de SST **quiero** publicar el mapa de riesgos de cada área **para** cumplir la obligación de exhibirlo. | **Cuando** subo el plano y ubico los riesgos<br>**Entonces** el mapa queda disponible para consulta y descarga | Web | Propuesta | EP13 |
| US86 | Consultar el mapa de riesgos en campo | **Como** operario **quiero** ver el mapa de riesgos de mi área desde el celular **para** conocer los peligros antes de empezar. | **Cuando** abro mi área<br>**Entonces** veo su mapa de riesgos y los peligros señalados | Móvil | Propuesta | EP13 |
| US87 | Inventario de señalización | **Como** supervisor **quiero** registrar la señalización instalada y su estado **para** detectar la que falta o está deteriorada. | **Cuando** reviso el inventario<br>**Entonces** veo por área qué señales debería haber, cuáles hay y cuáles están observadas | Web | Propuesta | EP13 |
| US88 | Ubicar el área por código QR | **Como** operario **quiero** escanear un código en el área **para** reportar sin tener que buscarla en una lista. | **Cuando** escaneo el código del área<br>**Entonces** el formulario de reporte queda precargado con esa área | Móvil | Propuesta | EP13 |

### EP14 — Documentación del SGSST

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US89 | Política de SST publicada | **Como** empresa **quiero** publicar la política de SST firmada por la alta dirección **para** exhibirla como exige la ley. | **Cuando** publico la política<br>**Entonces** queda visible para todos los trabajadores con su fecha de aprobación | Ambas | Propuesta | EP14 |
| US90 | Reglamento Interno de SST | **Como** responsable de SST **quiero** publicar el RISST y registrar su entrega a cada trabajador **para** evidenciar que lo conocen. | **Cuando** un trabajador confirma la recepción<br>**Entonces** queda registrada la fecha y la versión del reglamento entregada | Ambas | Propuesta | EP14 |
| US91 | Plan y programa anual de SST | **Como** responsable de SST **quiero** registrar el plan anual con sus objetivos y actividades **para** hacerle seguimiento durante el año. | **Cuando** consulto el plan<br>**Entonces** veo el avance de cada actividad programada frente a lo ejecutado | Web | Propuesta | EP14 |
| US92 | Control de versiones de documentos | **Como** auditor interno **quiero** ver el histórico de versiones de cada documento del sistema **para** verificar su evolución. | **Cuando** abro un documento<br>**Entonces** veo su versión vigente y las anteriores con su fecha de vigencia | Web | Propuesta | EP14 |

### EP15 — Monitoreo de agentes ocupacionales

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US93 | Registro de monitoreo de agentes | **Como** responsable de SST **quiero** registrar las mediciones de agentes físicos, químicos, biológicos, ergonómicos y psicosociales **para** completar el registro obligatorio. | **Cuando** registro una medición<br>**Entonces** queda con su agente, área, valor medido, límite permisible y si lo excede | Web | Propuesta | EP15 |
| US94 | Alerta por exceder el límite permisible | **Como** responsable de SST **quiero** que el sistema señale las mediciones fuera de límite **para** priorizar la intervención. | **Dado** que el valor medido supera el límite<br>**Entonces** la medición se destaca y sugiere generar una entrada en la matriz IPERC | Web | Propuesta | EP15 |
| US95 | Programa de monitoreo | **Como** responsable de SST **quiero** programar los monitoreos periódicos **para** que no se venzan sin aviso. | **Cuando** vence un monitoreo programado<br>**Entonces** aparece como pendiente junto a las inspecciones vencidas | Web | Propuesta | EP15 |

### EP16 — Contratistas y terceros

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US96 | Registro de empresa contratista | **Como** responsable de SST **quiero** registrar a las contratistas que operan en mis instalaciones **para** exigirles el mismo estándar. | **Cuando** registro una contratista<br>**Entonces** queda con su RUC, actividad, vigencia del contrato y responsable de SST | Web | Propuesta | EP16 |
| US97 | Documentación de seguridad de la contratista | **Como** responsable de SST **quiero** controlar la vigencia de los documentos de cada contratista **para** no permitir el ingreso de quien no cumple. | **Dado** que un documento está vencido<br>**Entonces** la contratista aparece observada y el sistema lo advierte | Web | Propuesta | EP16 |
| US98 | Trabajadores de contratista reportando | **Como** trabajador de una contratista **quiero** reportar hallazgos con mi propia cuenta **para** que la empresa principal también los vea. | **Cuando** reporto un hallazgo<br>**Entonces** queda asociado a mi contratista y visible para el comité de la empresa principal | Móvil | Propuesta | EP16 |
| US99 | Permiso de trabajo de alto riesgo | **Como** supervisor **quiero** emitir y controlar permisos para trabajos de alto riesgo **para** que no se ejecuten sin autorización. | **Cuando** emito un permiso<br>**Entonces** queda con su vigencia, responsables y las condiciones verificadas antes de autorizar | Ambas | Propuesta | EP16 |

### EP17 — Notificaciones y alertas

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US100 | Aviso de hallazgo crítico sin asignar | **Como** supervisor **quiero** recibir aviso de un hallazgo crítico que lleva horas sin responsable **para** que no se quede esperando en la bandeja. | **Dado** que un hallazgo crítico lleva más de 24 horas abierto<br>**Entonces** el sistema me notifica y registra el envío | Ambas | Propuesta | EP17 |
| US101 | Aviso de cierre al reportante | **Como** operario **quiero** enterarme cuando mi hallazgo se cierra **para** saber que sirvió de algo. | **Cuando** se cierra un hallazgo que reporté<br>**Entonces** recibo la notificación con la acción correctiva aplicada | Móvil | Propuesta | EP17 |
| US102 | Aviso de asignación | **Como** responsable asignado **quiero** que me avisen cuando me asignan un hallazgo **para** no depender de que alguien me lo diga. | **Cuando** me asignan un hallazgo<br>**Entonces** recibo la notificación con su severidad y plazo | Ambas | Propuesta | EP17 |
| US103 | Resumen diario para el comité | **Como** miembro del comité **quiero** un resumen diario de lo abierto y lo vencido **para** empezar el día sabiendo qué priorizar. | **Cuando** llega la hora configurada<br>**Entonces** recibo por correo el resumen de hallazgos abiertos, inspecciones vencidas y acuerdos por vencer | Web | Propuesta | EP17 |
| US104 | Aviso de acuerdo del comité por vencer | **Como** responsable de un acuerdo **quiero** que me avisen antes del plazo **para** cumplirlo a tiempo. | **Dado** que faltan tres días para el plazo<br>**Entonces** recibo el aviso con el acuerdo y su fecha límite | Ambas | Propuesta | EP17 |
| US105 | Preferencias de notificación | **Como** usuario **quiero** elegir qué avisos recibir y por qué canal **para** que el sistema no se vuelva ruido. | **Cuando** cambio mis preferencias<br>**Entonces** solo recibo los avisos que habilité | Ambas | Propuesta | EP17 |

### EP18 — Cuenta y servicio

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US106 | Alta de empresa desde la landing | **Como** responsable de SST de una empresa nueva **quiero** registrar mi empresa por mi cuenta **para** empezar a usar el sistema sin depender de una demostración. | **Cuando** completo el registro con el RUC y los datos de la empresa<br>**Entonces** la empresa queda creada y yo como su primer administrador | Web | Propuesta | EP18 |
| US107 | Datos y configuración de la empresa | **Como** administrador **quiero** editar la razón social, el RUC y el número de trabajadores **para** que el sistema aplique las reglas que me corresponden. | **Cuando** cambio el número de trabajadores a menos de veinte<br>**Entonces** el sistema pasa a admitir supervisor de SST en lugar de comité paritario | Web | Propuesta | EP18 |
| US108 | Planes y suscripción | **Como** administrador **quiero** conocer y cambiar mi plan **para** ajustar el servicio al tamaño de la empresa. | **Cuando** consulto la suscripción<br>**Entonces** veo el plan vigente, el número de trabajadores cubiertos y la fecha de renovación | Web | Propuesta | EP18 |
| US109 | Exportación completa de mis datos | **Como** administrador **quiero** poder llevarme toda la información de mi empresa **para** no quedar atado al proveedor. | **Cuando** solicito la exportación completa<br>**Entonces** recibo todos los registros en formato abierto | Web | Propuesta | EP18 |
| US110 | Respaldo y continuidad | **Como** empresa cliente **quiero** que mis registros estén respaldados **para** no perder la evidencia de años de gestión. | **Cuando** ocurre una falla del servicio<br>**Entonces** la información se restablece desde el último respaldo dentro del tiempo comprometido en el acuerdo de servicio | — | Propuesta | EP18 |

### EP19 — Seguridad y privacidad de datos

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US111 | Consentimiento informado de datos personales | **Como** trabajador **quiero** saber qué datos míos guarda el sistema y para qué **para** dar mi consentimiento con información. | **Cuando** creo mi cuenta<br>**Entonces** se me informa qué datos se tratan, con qué finalidad y por cuánto tiempo, conforme a la Ley N° 29733 | Ambas | Propuesta | EP19 |
| US112 | Ubicación opcional y revocable | **Como** trabajador **quiero** poder negar o revocar el permiso de ubicación **para** que no se registre dónde estoy. | **Cuando** niego el permiso<br>**Entonces** el reporte se envía igual, sin coordenadas, y nada se degrada salvo la ubicación | Ambas | Propuesta | EP19 |
| US113 | Registro de auditoría de accesos | **Como** responsable de datos personales **quiero** saber quién consultó o exportó información **para** rendir cuentas de su tratamiento. | **Cuando** un usuario exporta evidencia o consulta datos sensibles<br>**Entonces** queda registrado el usuario, la acción y la fecha | Web | Propuesta | EP19 |
| US114 | Cierre de sesión remoto | **Como** usuario **quiero** cerrar la sesión de un dispositivo que perdí **para** que nadie use mi cuenta. | **Cuando** cierro las sesiones activas<br>**Entonces** los tokens de ese dispositivo dejan de ser válidos | Web | Propuesta | EP19 |
| US115 | Política de retención de evidencia | **Como** responsable de datos **quiero** que las fotografías se eliminen al vencer el plazo legal de conservación **para** no almacenar datos personales más de lo necesario. | **Dado** que un hallazgo cerrado superó el plazo de retención<br>**Entonces** su fotografía se elimina y el registro documental se conserva | — | Propuesta | EP19 |
| US116 | Reporte anónimo de actos inseguros | **Como** trabajador **quiero** poder reportar el acto inseguro de un compañero sin dar mi nombre **para** no exponerme a represalias. | **Cuando** elijo reportar de forma anónima<br>**Entonces** el hallazgo se registra sin identificar al reportante, conservando área, tipo y evidencia | Ambas | Propuesta | EP19 |

### Ampliaciones propuestas sobre épicas existentes

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Estado | Épica |
|---|---|---|---|---|---|---|
| US117 | Reporte por voz | **Como** operario con guantes **quiero** dictar la descripción en lugar de escribirla **para** reportar sin quitarme el equipo. | **Cuando** uso el dictado<br>**Entonces** el texto queda en la descripción y puedo corregirlo antes de enviar | Móvil | Propuesta | EP02 |
| US118 | Firma del trabajador en la entrega de EPP | **Como** supervisor **quiero** capturar la firma del trabajador en pantalla **para** que la conformidad tenga el mismo valor que la del papel. | **Cuando** el trabajador firma en pantalla<br>**Entonces** la firma queda adjunta a la entrega y aparece en la exportación | Móvil | Propuesta | EP05 |
| US119 | Adjuntar evidencia en inspecciones | **Como** inspector **quiero** adjuntar fotos a los ítems observados del checklist **para** sustentar el hallazgo. | **Cuando** marco un ítem como observado<br>**Entonces** puedo adjuntarle una fotografía que queda en el registro | Móvil | Propuesta | EP06 |
| US120 | Generar hallazgo desde una inspección | **Como** inspector **quiero** convertir una observación de la inspección en un hallazgo **para** que entre al ciclo de corrección. | **Cuando** genero el hallazgo desde la observación<br>**Entonces** queda enlazado a la inspección que lo originó | Ambas | Propuesta | EP06 |
| US121 | Convocatoria y asistencia del comité | **Como** secretario del comité **quiero** convocar la reunión y registrar la asistencia efectiva **para** sustentar el quórum. | **Cuando** registro quién asistió<br>**Entonces** el quórum se calcula sobre los asistentes reales y no sobre los miembros activos | Web | Propuesta | EP07 |
| US122 | Elección de representantes de los trabajadores | **Como** empresa **quiero** registrar el proceso de elección de los representantes **para** evidenciar que el comité se constituyó como manda la ley. | **Cuando** registro la elección<br>**Entonces** quedan el acta, los candidatos y los elegidos con su periodo | Web | Propuesta | EP07 |
| US123 | Exportar el tablero a PDF | **Como** responsable de SST **quiero** exportar el tablero de indicadores a PDF **para** adjuntarlo al informe mensual a la gerencia. | **Cuando** exporto el tablero<br>**Entonces** obtengo un PDF con los indicadores del periodo y la fecha de generación | Web | Propuesta | EP08 |
| US124 | Comparar periodos | **Como** responsable de SST **quiero** comparar el MTTR y el cumplimiento con el periodo anterior **para** saber si mejoramos. | **Cuando** elijo comparar<br>**Entonces** veo la variación de cada indicador frente al periodo previo | Web | Propuesta | EP08 |
| US125 | Aviso de datos de demostración | **Como** evaluador **quiero** distinguir los datos de demostración de los reales **para** no interpretar resultados simulados como evidencia. | **Dado** que los datos provienen de la carga de demostración<br>**Entonces** el panel del experimento muestra un aviso visible que lo declara | Web | Propuesta | EP09 |
| US126 | Intervalo de confianza en los resultados | **Como** analista **quiero** ver el intervalo de confianza de la diferencia entre variantes **para** comunicar la precisión y no solo el promedio. | **Cuando** consulto los resultados<br>**Entonces** veo la diferencia estimada con su intervalo al 95 % y el tamaño de cada grupo | Web | Propuesta | EP09 |
| US127 | Interfaz accesible para lectores de pantalla | **Como** trabajador con discapacidad visual **quiero** usar la aplicación con el lector de pantalla **para** poder reportar como cualquiera. | **Cuando** navego con TalkBack<br>**Entonces** cada control tiene una descripción comprensible y el orden de lectura sigue el flujo de la tarea | Ambas | Propuesta | EP10 |
| US128 | Modo de alto contraste | **Como** trabajador que opera bajo el sol **quiero** un modo de alto contraste **para** leer la pantalla en exteriores. | **Cuando** activo el alto contraste<br>**Entonces** la interfaz aumenta el contraste conservando el significado de los colores de estado | Ambas | Propuesta | EP10 |

### Historias técnicas

Trabajo de infraestructura sin valor directo para el usuario final, pero necesario para sostener
el producto y exigido por el curso. La columna **Repositorio** indica dónde vive cada una, y la
columna **Épica** la vincula con la capacidad de negocio que habilita. Las dieciséis primeras
(TS01–TS16) están implementadas; las dieciocho restantes (TS17–TS34) sostienen las épicas
propuestas y quedan en el backlog.

| ID | Título | Descripción | Criterios de aceptación | Repositorio | Estado | Épica |
|---|---|---|---|---|---|---|
| TS01 | Integración continua | **Como** equipo de desarrollo **quiero** que cada Pull Request ejecute pruebas y análisis estático **para** no integrar código roto. | **Escenario: PR con pruebas fallidas**<br>**Cuando** abro un PR cuyas pruebas fallan<br>**Entonces** el pipeline marca el PR en rojo y bloquea la integración | Los cuatro | Sprint 1 | —|
| TS02 | Convenciones de commits | **Como** equipo **quiero** que los mensajes de commit sigan Conventional Commits **para** mantener un historial legible y auditable. | **Escenario: mensaje inválido**<br>**Cuando** intento commitear con un mensaje fuera del formato<br>**Entonces** el hook local lo rechaza y el workflow de CI también | Los cuatro | Sprint 1 | —|
| TS03 | Documentación viva del API | **Como** desarrollador de los clientes **quiero** una especificación OpenAPI generada del código **para** que el contrato no se desactualice. | **Escenario: documentación**<br>**Cuando** accedo a la ruta de documentación<br>**Entonces** obtengo la especificación de todos los endpoints vigentes | sst-api | Implementada | —|
| TS04 | Datos de demostración | **Como** equipo **quiero** un comando que genere datos realistas **para** poder demostrar y probar el sistema. | **Escenario: carga**<br>**Cuando** ejecuto el comando de carga<br>**Entonces** el sistema queda con empresa, usuarios, reportes, IPERC, EPP, inspecciones y actas de ejemplo, claramente identificados como datos de demostración | sst-api | Implementada | —|
| TS05 | Flujo de ramas GitFlow | **Como** equipo **quiero** un flujo de ramas definido y protegido **para** que nada llegue a la línea principal sin revisión. | **Dado** que intento empujar directamente a main o develop<br>**Entonces** la protección de rama lo rechaza y obliga a pasar por Pull Request | Los cuatro | Sprint 1 | —|
| TS06 | Fin de línea normalizado | **Como** equipo que trabaja en Windows **quiero** que el repositorio guarde siempre LF **para** que no aparezcan diferencias falsas en cada archivo. | **Cuando** edito un archivo en Windows y lo commiteo<br>**Entonces** el repositorio lo guarda con LF y el diff muestra solo lo que cambié de verdad | Los cuatro | Implementada | —|
| TS07 | Validación local del mensaje de commit | **Como** desarrollador **quiero** que el formato del commit se valide antes de crearlo **para** enterarme al momento y no en el Pull Request. | **Cuando** intento commitear con un mensaje fuera de formato<br>**Entonces** el hook lo rechaza mostrando los tipos válidos y un ejemplo | Los cuatro | Implementada | —|
| TS08 | Configuración por variables de entorno | **Como** responsable del despliegue **quiero** que la configuración viva fuera del código **para** usar el mismo artefacto en desarrollo y en producción. | **Cuando** cambio la base de datos o el origen permitido<br>**Entonces** basta modificar el archivo de entorno, sin tocar ni reconstruir el código | sst-api | Implementada | —|
| TS09 | Proxy de desarrollo | **Como** desarrollador de la web **quiero** que las peticiones al API pasen por el servidor de desarrollo **para** no lidiar con CORS en local. | **Cuando** levanto la web en desarrollo<br>**Entonces** las llamadas a /api llegan al backend sin error de origen cruzado | sst-web | Implementada | —|
| TS10 | Renovación transparente del token | **Como** usuario **quiero** no perder lo que estoy haciendo cuando expira mi sesión **para** no repetir el trabajo. | **Dado** que varias peticiones fallan a la vez por token expirado<br>**Entonces** el cliente renueva una sola vez y reintenta todas, sin pedir la contraseña | sst-web, sst-mobile | Implementada | —|
| TS11 | Aislamiento entre empresas | **Como** empresa cliente **quiero** que mis datos sean invisibles para otras empresas **para** poder usar un servicio compartido. | **Cuando** un usuario consulta cualquier recurso<br>**Entonces** la consulta se restringe a su empresa en el backend, no en la interfaz | sst-api | Implementada | —|
| TS12 | Idempotencia en la creación de reportes | **Como** equipo de datos **quiero** que un reintento no genere un hallazgo duplicado **para** que las métricas sean confiables. | **Cuando** llega dos veces el mismo identificador de cliente<br>**Entonces** el API devuelve el reporte existente y no crea otro | sst-api | Implementada | —|
| TS13 | Migraciones verificadas en integración | **Como** equipo **quiero** que un modelo cambiado sin migración rompa la construcción **para** no descubrirlo en el despliegue. | **Cuando** abro un Pull Request con un modelo modificado y sin migración<br>**Entonces** el pipeline falla indicando que faltan migraciones | sst-api | Implementada | —|
| TS14 | APK publicado por el pipeline | **Como** equipo **quiero** que cada construcción publique el APK **para** poder instalarlo y probarlo sin compilar. | **Cuando** el pipeline móvil termina correctamente<br>**Entonces** el APK de depuración queda disponible como artefacto de la ejecución | sst-mobile | Implementada | —|
| TS15 | Generación de evidencia en Excel | **Como** responsable de SST **quiero** que la evidencia se genere en el formato que la auditoría espera **para** entregarla sin retrabajo. | **Cuando** solicito una exportación<br>**Entonces** el sistema genera un .xlsx con cabecera formateada, anchos ajustados y los datos del registro | sst-api | Implementada | —|
| TS16 | Informe compilable y con índice verificado | **Como** equipo **quiero** que el informe se arme solo y su índice no se desactualice **para** exportar el PDF sin revisiones manuales. | **Cuando** abro un Pull Request con el índice desfasado<br>**Entonces** el pipeline del informe falla e indica cómo regenerarlo | sst-report | Implementada | —|
| TS17 | Servicio de notificaciones push | **Como** equipo **quiero** un servicio de notificaciones push integrado **para** que el móvil reciba avisos aunque la aplicación esté cerrada. | **Cuando** el backend emite un aviso dirigido a un usuario<br>**Entonces** el dispositivo registrado lo recibe aunque la aplicación no esté en primer plano | sst-api, sst-mobile | Propuesta | EP17 |
| TS18 | Tareas programadas en el servidor | **Como** equipo **quiero** un ejecutor de tareas periódicas **para** calcular vencimientos y enviar recordatorios sin intervención manual. | **Cuando** llega la hora programada<br>**Entonces** la tarea se ejecuta, deja registro de su resultado y reintenta si falla | sst-api | Propuesta | EP17 |
| TS19 | Correo transaccional | **Como** equipo **quiero** un proveedor de correo configurado **para** enviar recuperaciones de contraseña y resúmenes sin depender del cliente. | **Cuando** el sistema necesita enviar un correo<br>**Entonces** sale por el proveedor configurado y el envío queda registrado con su estado | sst-api | Propuesta | EP18 |
| TS20 | Registro de auditoría | **Como** auditor **quiero** que toda operación que modifica datos quede registrada **para** poder reconstruir quién hizo qué y cuándo. | **Cuando** un usuario crea, modifica o elimina un registro<br>**Entonces** se guarda una entrada con usuario, acción, recurso, valores anteriores y fecha, y esa entrada no puede editarse | sst-api | Propuesta | EP19 |
| TS21 | Respaldo automático y restauración probada | **Como** empresa cliente **quiero** respaldos automáticos verificados **para** no perder el expediente de SST ante una falla. | **Cuando** se cumple la ventana de respaldo<br>**Entonces** se genera una copia cifrada y, en la prueba periódica, se restaura en un entorno aparte con éxito verificado | sst-api | Propuesta | EP19 |
| TS22 | Almacenamiento de archivos en servicio de objetos | **Como** equipo **quiero** que las fotos vivan en un servicio de objetos y no en el disco del servidor **para** poder escalar y respaldar la evidencia. | **Cuando** se sube una fotografía<br>**Entonces** queda en el servicio de objetos y el API entrega un enlace temporal firmado | sst-api | Propuesta | EP19 |
| TS23 | Observabilidad del backend | **Como** responsable de operación **quiero** registros estructurados y trazas **para** diagnosticar un problema sin reproducirlo a ciegas. | **Cuando** una petición falla<br>**Entonces** el registro incluye identificador de correlación, usuario, recurso y tiempo de respuesta | sst-api | Propuesta | EP10 |
| TS24 | Reporte de errores del cliente | **Como** equipo **quiero** que los errores no controlados de los clientes lleguen a un panel **para** enterarme antes de que el usuario reclame. | **Cuando** ocurre un error no controlado en la web o en el móvil<br>**Entonces** se reporta con versión, plataforma y traza, sin datos personales del reporte | sst-web, sst-mobile | Propuesta | EP10 |
| TS25 | Limitación de tasa de peticiones | **Como** responsable del servicio **quiero** limitar la tasa por usuario y por IP **para** que un cliente defectuoso no degrade el servicio de los demás. | **Cuando** un origen supera el límite configurado<br>**Entonces** el API responde 429 indicando cuándo reintentar | sst-api | Propuesta | EP19 |
| TS26 | Pruebas de extremo a extremo de la web | **Como** equipo **quiero** pruebas automatizadas que recorran los flujos críticos en un navegador real **para** detectar regresiones de integración. | **Cuando** se ejecuta el pipeline<br>**Entonces** se recorren los flujos de inicio de sesión, reporte, asignación y cierre, y el fallo de cualquiera bloquea la integración | sst-web | Propuesta | EP10 |
| TS27 | Pruebas instrumentadas del cliente móvil | **Como** equipo **quiero** pruebas instrumentadas sobre el flujo de reporte y sincronización **para** verificar el comportamiento sin conexión de forma automática. | **Cuando** se ejecuta el pipeline móvil<br>**Entonces** se ejecutan las pruebas instrumentadas en un emulador, incluido el caso sin conexión y su posterior sincronización | sst-mobile | Propuesta | EP10 |
| TS28 | Despliegue automatizado al entorno de pruebas | **Como** equipo **quiero** que cada integración en develop despliegue sola **para** que el cliente valide sobre la versión vigente. | **Cuando** un Pull Request se integra a develop<br>**Entonces** el pipeline despliega el API y la web al entorno de pruebas y publica la URL en la ejecución | sst-api, sst-web | Propuesta | EP10 |
| TS29 | Cifrado de datos personales en reposo | **Como** empresa cliente **quiero** que los datos personales estén cifrados en reposo **para** cumplir la Ley 29733 de protección de datos personales. | **Cuando** se almacenan documento de identidad, teléfono o fotografía de una persona<br>**Entonces** quedan cifrados en reposo y solo se descifran para el usuario autorizado | sst-api | Propuesta | EP19 |
| TS30 | Versionado del API | **Como** equipo de los clientes **quiero** que el API esté versionado **para** que una versión antigua del móvil siga funcionando tras un cambio. | **Cuando** se publica un cambio incompatible<br>**Entonces** convive bajo una nueva versión de ruta y la anterior sigue respondiendo durante el periodo de transición | sst-api | Propuesta | EP19 |
| TS31 | Resolución de conflictos de sincronización | **Como** equipo de datos **quiero** una regla explícita de resolución de conflictos **para** que dos ediciones simultáneas no se pisen en silencio. | **Cuando** llega una actualización sobre un registro modificado después de la copia local<br>**Entonces** el API rechaza el cambio indicando el conflicto y el cliente muestra ambas versiones | sst-api, sst-mobile | Propuesta | EP02 |
| TS32 | Accesibilidad verificada en el pipeline | **Como** equipo **quiero** que el pipeline revise contraste y etiquetas accesibles **para** que la accesibilidad no dependa de acordarse. | **Cuando** se ejecuta el pipeline de la web<br>**Entonces** falla si aparecen violaciones de contraste o controles sin nombre accesible | sst-web, sst-mobile | Propuesta | EP10 |
| TS33 | Textos externalizados para traducción | **Como** empresa con personal quechuahablante **quiero** que los textos estén externalizados **para** poder ofrecer la aplicación en otro idioma sin recompilar la lógica. | **Cuando** se agrega un idioma<br>**Entonces** basta añadir el archivo de textos y la interfaz cambia según la preferencia del usuario | sst-web, sst-mobile | Propuesta | EP18 |
| TS34 | Entorno reproducible con contenedores | **Como** nuevo integrante del equipo **quiero** levantar todo el entorno con un comando **para** empezar a trabajar el primer día. | **Cuando** ejecuto el comando de composición<br>**Entonces** quedan corriendo el API, la base de datos y la web, con datos de demostración cargados | sst-api, sst-web | Propuesta | EP10 |

## 3.3. Product Backlog

El backlog reúne los 162 elementos del producto: las 128 historias de usuario, agrupadas en
diecinueve épicas, y las 34 historias técnicas. El orden es de prioridad de negocio, no
cronológico: primero lo que hace que el sistema capture el hallazgo, después lo que permite
gestionarlo, luego lo que sostiene la operación, y al final lo que amplía la cobertura legal del
sistema de gestión.

La columna **Estado** distingue tres situaciones que conviene no confundir:

| Estado | Significado |
|---|---|
| **Sprint 1** | Elemento comprometido en el Sprint 1 y entregado. Es el alcance que el equipo se obligó a presentar en este ciclo, y el que se detalla en el Sprint Backlog del Capítulo V |
| **Implementada** | Elemento construido y verificable en el código entregado, pero **no comprometido** en el Sprint 1: es avance sobre los siguientes sprints, no parte del compromiso de este |
| **Propuesta** | Elemento especificado y estimado cuya construcción no ha empezado |

Esa separación es deliberada. Un Sprint Backlog es un compromiso, y un compromiso se mide por lo
que se prometió, no por todo lo que terminó habiendo en el repositorio. Declarar como alcance del
sprint únicamente aquello a lo que el equipo se obligó —y dejar el resto identificado como avance
o como backlog— es lo que permite que la velocidad signifique algo.

La columna **Plataforma** se repite aquí para que la paridad web/móvil sea verificable sin
volver a la sección anterior. El guion (`—`) marca los elementos sin interfaz propia: trabajo de
backend o de infraestructura.

| # | ID | Historia | Épica | Plataforma | Estado | Story Points |
|---|---|---|---|---|---|---|
| 1 | US02 | Inicio de sesión | EP01 | Ambas | Sprint 1 | 3 |
| 2 | US06 | Reporte rápido desde el celular | EP02 | Ambas | Sprint 1 | 8 |
| 3 | US07 | Reporte sin conexión | EP02 | Móvil | Implementada | 13 |
| 4 | US08 | Sincronización sin duplicados | EP02 | Ambas | Implementada | 8 |
| 5 | US13 | Consulta de mis reportes | EP02 | Ambas | Sprint 1 | 3 |
| 6 | US43 | Menú según mi rol | EP01 | Ambas | Sprint 1 | 3 |
| 7 | US70 | Sesión que no expira en campo | EP10 | Ambas | Implementada | 5 |
| 8 | US14 | Bandeja de hallazgos | EP03 | Ambas | Sprint 1 | 5 |
| 9 | US16 | Cierre con acción correctiva | EP03 | Ambas | Sprint 1 | 5 |
| 10 | US15 | Asignación de responsable | EP03 | Ambas | Sprint 1 | 5 |
| 11 | US17 | Separación de responsabilidades | EP03 | Ambas | Implementada | 3 |
| 12 | US18 | Bitácora del hallazgo | EP03 | Ambas | Sprint 1 | 3 |
| 13 | US09 | Evidencia fotográfica | EP02 | Ambas | Sprint 1 | 5 |
| 14 | US35 | Indicador MTTR | EP08 | Ambas | Implementada | 5 |
| 15 | US50 | Filtrar la bandeja | EP03 | Ambas | Implementada | 3 |
| 16 | US49 | Descartar un reporte | EP03 | Web | Implementada | 2 |
| 17 | US10 | Geolocalización del hallazgo | EP02 | Ambas | Sprint 1 | 5 |
| 18 | US11 | Fecha real de ocurrencia | EP02 | Ambas | Sprint 1 | 3 |
| 19 | US12 | Reporte desde la web | EP02 | Web | Implementada | 5 |
| 20 | US44 | Vista previa de la evidencia | EP02 | Web | Implementada | 3 |
| 21 | US45 | Ampliar la evidencia | EP02 | Web | Implementada | 3 |
| 22 | US46 | Reemplazar la foto elegida | EP02 | Web | Implementada | 2 |
| 23 | US47 | Categorías según el tipo de hallazgo | EP02 | Ambas | Sprint 1 | 2 |
| 24 | US48 | Estado de envío de mis reportes | EP02 | Móvil | Implementada | 3 |
| 25 | US51 | Ubicar el hallazgo en el mapa | EP03 | Web | Implementada | 1 |
| 26 | US38 | Asignación de variante | EP09 | Ambas | Implementada | 5 |
| 27 | US39 | Registro de la variante en el reporte | EP09 | Ambas | Implementada | 2 |
| 28 | US40 | Resultados del experimento | EP09 | Web | Implementada | 5 |
| 29 | US64 | Variante disponible sin conexión | EP09 | Móvil | Implementada | 3 |
| 30 | US01 | Registro de trabajador | EP01 | Ambas | Implementada | 5 |
| 31 | US03 | Sesión persistente en campo | EP01 | Ambas | Implementada | 3 |
| 32 | US05 | Gestión de áreas | EP01 | Web | Implementada | 2 |
| 33 | US04 | Administración de usuarios | EP01 | Web | Implementada | 5 |
| 34 | US41 | Cambio de rol de un usuario | EP01 | Web | Implementada | 2 |
| 35 | US42 | Cierre de sesión | EP01 | Ambas | Implementada | 1 |
| 36 | US19 | Consulta de la matriz en campo | EP04 | Ambas | Implementada | 3 |
| 37 | US20 | Registro de peligros | EP04 | Web | Implementada | 5 |
| 38 | US21 | Versionado de la matriz | EP04 | Web | Implementada | 5 |
| 39 | US22 | Trazabilidad con el hallazgo de origen | EP04 | Ambas | Implementada | 3 |
| 40 | US52 | Consultar versiones anteriores de la matriz | EP04 | Web | Implementada | 5 |
| 41 | US53 | Publicar una nueva versión de la matriz | EP04 | Web | Implementada | 5 |
| 42 | US54 | Retirar un peligro de la matriz | EP04 | Web | Implementada | 2 |
| 43 | US23 | Catálogo de EPP | EP05 | Web | Implementada | 3 |
| 44 | US24 | Registro de entrega | EP05 | Web | Implementada | 3 |
| 45 | US25 | Conformidad del trabajador | EP05 | Ambas | Implementada | 3 |
| 46 | US26 | Alerta de EPP vencido | EP05 | Ambas | Implementada | 2 |
| 47 | US55 | Control de stock del catálogo | EP05 | Web | Implementada | 2 |
| 48 | US27 | Programa de inspecciones | EP06 | Web | Implementada | 5 |
| 49 | US28 | Ejecución con checklist | EP06 | Ambas | Implementada | 5 |
| 50 | US29 | Inspecciones vencidas | EP06 | Ambas | Implementada | 3 |
| 51 | US56 | Programar la siguiente inspección | EP06 | Web | Implementada | 3 |
| 52 | US36 | Tasa de cumplimiento de inspecciones | EP08 | Ambas | Implementada | 5 |
| 53 | US57 | Cumplimiento por área | EP06 | Web | Implementada | 3 |
| 54 | US30 | Constitución del comité | EP07 | Web | Implementada | 3 |
| 55 | US31 | Miembros y paridad | EP07 | Web | Implementada | 5 |
| 56 | US32 | Acta de reunión | EP07 | Web | Implementada | 5 |
| 57 | US33 | Control de quórum | EP07 | Ambas | Implementada | 3 |
| 58 | US34 | Acuerdos con responsable y plazo | EP07 | Web | Implementada | 3 |
| 59 | US58 | Advertencia de comité no paritario | EP07 | Web | Implementada | 2 |
| 60 | US59 | Seguimiento del estado de los acuerdos | EP07 | Web | Implementada | 2 |
| 61 | US60 | Consultar las actas desde el celular | EP07 | Móvil | Implementada | 3 |
| 62 | US37 | Exportación de evidencia | EP08 | Web | Implementada | 8 |
| 63 | US61 | MTTR por severidad | EP08 | Ambas | Implementada | 3 |
| 64 | US62 | Exportar cada registro obligatorio | EP08 | Web | Implementada | 3 |
| 65 | US63 | Resumen de hallazgos | EP08 | Ambas | Implementada | 3 |
| 66 | US65 | Identidad visual consistente | EP10 | Ambas | Implementada | 5 |
| 67 | US66 | Navegación siempre accesible | EP10 | Ambas | Implementada | 2 |
| 68 | US67 | Uso desde pantallas pequeñas | EP10 | Web | Implementada | 5 |
| 69 | US68 | Errores comprensibles | EP10 | Ambas | Implementada | 3 |
| 70 | US69 | Reintento ante fallo de red | EP10 | Móvil | Implementada | 3 |
| 71 | TS02 | Convenciones de commits | — | Los cuatro | Sprint 1 | 2 |
| 72 | TS07 | Validación local del mensaje de commit | — | Los cuatro | Implementada | 2 |
| 73 | TS05 | Flujo de ramas GitFlow | — | Los cuatro | Sprint 1 | 3 |
| 74 | TS06 | Fin de línea normalizado | — | Los cuatro | Implementada | 2 |
| 75 | TS01 | Integración continua | — | Los cuatro | Sprint 1 | 5 |
| 76 | TS13 | Migraciones verificadas en integración | — | sst-api | Implementada | 2 |
| 77 | TS03 | Documentación viva del API | — | sst-api | Implementada | 2 |
| 78 | TS08 | Configuración por variables de entorno | — | sst-api | Implementada | 3 |
| 79 | TS09 | Proxy de desarrollo | — | sst-web | Implementada | 2 |
| 80 | TS10 | Renovación transparente del token | — | sst-web, sst-mobile | Implementada | 5 |
| 81 | TS11 | Aislamiento entre empresas | — | sst-api | Implementada | 5 |
| 82 | TS12 | Idempotencia en la creación de reportes | — | sst-api | Implementada | 5 |
| 83 | TS04 | Datos de demostración | — | sst-api | Implementada | 5 |
| 84 | TS14 | APK publicado por el pipeline | — | sst-mobile | Implementada | 3 |
| 85 | TS15 | Generación de evidencia en Excel | — | sst-api | Implementada | 5 |
| 86 | TS16 | Informe compilable y con índice verificado | — | sst-report | Implementada | 3 |
| 87 | US71 | Registro de accidente de trabajo | EP11 | Web | Propuesta | 8 |
| 88 | US72 | Registro de incidente peligroso | EP11 | Ambas | Propuesta | 5 |
| 89 | US73 | Reportar un accidente desde el celular | EP11 | Móvil | Propuesta | 5 |
| 90 | US74 | Investigación de causa raíz | EP11 | Web | Propuesta | 8 |
| 91 | US75 | Medidas correctivas con responsable y plazo | EP11 | Web | Propuesta | 5 |
| 92 | US76 | Aviso de accidente mortal dentro del plazo legal | EP11 | Web | Propuesta | 3 |
| 93 | US77 | Indicadores de accidentabilidad | EP11 | Ambas | Propuesta | 5 |
| 94 | US78 | Registro de enfermedad ocupacional | EP11 | Web | Propuesta | 5 |
| 95 | US79 | Programa anual de capacitación | EP12 | Web | Propuesta | 5 |
| 96 | US80 | Registro de asistencia a capacitación | EP12 | Móvil | Propuesta | 5 |
| 97 | US81 | Inducción del personal nuevo | EP12 | Web | Propuesta | 5 |
| 98 | US82 | Alerta de capacitación vencida | EP12 | Web | Propuesta | 3 |
| 99 | US83 | Consultar mis capacitaciones | EP12 | Móvil | Propuesta | 3 |
| 100 | US84 | Registro de simulacros | EP12 | Web | Propuesta | 3 |
| 101 | US85 | Mapa de riesgos por área | EP13 | Web | Propuesta | 8 |
| 102 | US86 | Consultar el mapa de riesgos en campo | EP13 | Móvil | Propuesta | 3 |
| 103 | US87 | Inventario de señalización | EP13 | Web | Propuesta | 3 |
| 104 | US88 | Ubicar el área por código QR | EP13 | Móvil | Propuesta | 5 |
| 105 | US89 | Política de SST publicada | EP14 | Ambas | Propuesta | 3 |
| 106 | US90 | Reglamento Interno de SST | EP14 | Ambas | Propuesta | 3 |
| 107 | US91 | Plan y programa anual de SST | EP14 | Web | Propuesta | 5 |
| 108 | US92 | Control de versiones de documentos | EP14 | Web | Propuesta | 5 |
| 109 | US93 | Registro de monitoreo de agentes | EP15 | Web | Propuesta | 5 |
| 110 | US94 | Alerta por exceder el límite permisible | EP15 | Web | Propuesta | 3 |
| 111 | US95 | Programa de monitoreo | EP15 | Web | Propuesta | 3 |
| 112 | US96 | Registro de empresa contratista | EP16 | Web | Propuesta | 5 |
| 113 | US97 | Documentación de seguridad de la contratista | EP16 | Web | Propuesta | 5 |
| 114 | US98 | Trabajadores de contratista reportando | EP16 | Móvil | Propuesta | 5 |
| 115 | US99 | Permiso de trabajo de alto riesgo | EP16 | Ambas | Propuesta | 8 |
| 116 | US100 | Aviso de hallazgo crítico sin asignar | EP17 | Ambas | Propuesta | 3 |
| 117 | US101 | Aviso de cierre al reportante | EP17 | Móvil | Propuesta | 2 |
| 118 | US102 | Aviso de asignación | EP17 | Ambas | Propuesta | 2 |
| 119 | US103 | Resumen diario para el comité | EP17 | Web | Propuesta | 3 |
| 120 | US104 | Aviso de acuerdo del comité por vencer | EP17 | Ambas | Propuesta | 2 |
| 121 | US105 | Preferencias de notificación | EP17 | Ambas | Propuesta | 3 |
| 122 | US106 | Alta de empresa desde la landing | EP18 | Web | Propuesta | 8 |
| 123 | US107 | Datos y configuración de la empresa | EP18 | Web | Propuesta | 3 |
| 124 | US108 | Planes y suscripción | EP18 | Web | Propuesta | 5 |
| 125 | US109 | Exportación completa de mis datos | EP18 | Web | Propuesta | 5 |
| 126 | US110 | Respaldo y continuidad | EP18 | — | Propuesta | 5 |
| 127 | US111 | Consentimiento informado de datos personales | EP19 | Ambas | Propuesta | 3 |
| 128 | US112 | Ubicación opcional y revocable | EP19 | Ambas | Propuesta | 3 |
| 129 | US113 | Registro de auditoría de accesos | EP19 | Web | Propuesta | 5 |
| 130 | US114 | Cierre de sesión remoto | EP19 | Web | Propuesta | 3 |
| 131 | US115 | Política de retención de evidencia | EP19 | — | Propuesta | 5 |
| 132 | US116 | Reporte anónimo de actos inseguros | EP19 | Ambas | Propuesta | 5 |
| 133 | US117 | Reporte por voz | EP02 | Móvil | Propuesta | 8 |
| 134 | US118 | Firma del trabajador en la entrega de EPP | EP05 | Móvil | Propuesta | 5 |
| 135 | US119 | Adjuntar evidencia en inspecciones | EP06 | Móvil | Propuesta | 3 |
| 136 | US120 | Generar hallazgo desde una inspección | EP06 | Ambas | Propuesta | 3 |
| 137 | US121 | Convocatoria y asistencia del comité | EP07 | Web | Propuesta | 3 |
| 138 | US122 | Elección de representantes de los trabajadores | EP07 | Web | Propuesta | 5 |
| 139 | US123 | Exportar el tablero a PDF | EP08 | Web | Propuesta | 5 |
| 140 | US124 | Comparar periodos | EP08 | Web | Propuesta | 3 |
| 141 | US125 | Aviso de datos de demostración | EP09 | Web | Propuesta | 1 |
| 142 | US126 | Intervalo de confianza en los resultados | EP09 | Web | Propuesta | 3 |
| 143 | US127 | Interfaz accesible para lectores de pantalla | EP10 | Ambas | Propuesta | 8 |
| 144 | US128 | Modo de alto contraste | EP10 | Ambas | Propuesta | 3 |
| 145 | TS17 | Servicio de notificaciones push | EP17 | sst-api, sst-mobile | Propuesta | 5 |
| 146 | TS18 | Tareas programadas en el servidor | EP17 | sst-api | Propuesta | 5 |
| 147 | TS19 | Correo transaccional | EP18 | sst-api | Propuesta | 3 |
| 148 | TS20 | Registro de auditoría | EP19 | sst-api | Propuesta | 5 |
| 149 | TS21 | Respaldo automático y restauración probada | EP19 | sst-api | Propuesta | 5 |
| 150 | TS22 | Almacenamiento de archivos en servicio de objetos | EP19 | sst-api | Propuesta | 5 |
| 151 | TS23 | Observabilidad del backend | EP10 | sst-api | Propuesta | 3 |
| 152 | TS24 | Reporte de errores del cliente | EP10 | sst-web, sst-mobile | Propuesta | 3 |
| 153 | TS25 | Limitación de tasa de peticiones | EP19 | sst-api | Propuesta | 2 |
| 154 | TS26 | Pruebas de extremo a extremo de la web | EP10 | sst-web | Propuesta | 8 |
| 155 | TS27 | Pruebas instrumentadas del cliente móvil | EP10 | sst-mobile | Propuesta | 8 |
| 156 | TS28 | Despliegue automatizado al entorno de pruebas | EP10 | sst-api, sst-web | Propuesta | 5 |
| 157 | TS29 | Cifrado de datos personales en reposo | EP19 | sst-api | Propuesta | 8 |
| 158 | TS30 | Versionado del API | EP19 | sst-api | Propuesta | 5 |
| 159 | TS31 | Resolución de conflictos de sincronización | EP02 | sst-api, sst-mobile | Propuesta | 8 |
| 160 | TS32 | Accesibilidad verificada en el pipeline | EP10 | sst-web, sst-mobile | Propuesta | 3 |
| 161 | TS33 | Textos externalizados para traducción | EP18 | sst-web, sst-mobile | Propuesta | 5 |
| 162 | TS34 | Entorno reproducible con contenedores | EP10 | sst-api, sst-web | Propuesta | 3 |

**Total:** 162 elementos (128 historias de usuario y 34 historias técnicas), 660 Story Points.

| Alcance | Elementos | Historias de usuario | Historias técnicas | Story Points |
|---|---|---|---|---|
| Comprometido y entregado en el Sprint 1 | 15 | 12 | 3 | 60 |
| Construido, fuera del compromiso del Sprint 1 | 71 | 58 | 13 | 259 |
| Propuesto (sin construir) | 76 | 58 | 18 | 341 |
| **Backlog completo** | **162** | **128** | **34** | **660** |

El Sprint 1 comprometió 60 Story Points, el 9 % del backlog. La diferencia entre ese compromiso y lo que ya está construido es intencional: el equipo prefirió un compromiso que pudiera sostener con el producto funcionando delante, y dejar el avance restante identificado como tal en lugar de inflar el alcance del sprint.

Lo propuesto no es relleno: cada elemento pendiente corresponde a una obligación de la Ley N° 29783 o de su Reglamento que el producto debe cubrir para reemplazar por completo el expediente en papel, y por eso queda especificado y estimado aunque no se construya en este ciclo.

## 3.4. Impact Mapping

<!-- IMAGEN REQUERIDA: exportar el Impact Map a assets/img/impact-map.png -->

![Impact Map](../assets/img/impact-map.png)

| Goal (¿Por qué?) | Actor (¿Quién?) | Impact (¿Cómo?) | Deliverable (¿Qué?) |
|---|---|---|---|
| **Reducir el tiempo entre la detección de un peligro y su corrección, evidenciando la gestión ante la autoridad** | Operario de campo | Reporta más seguido porque le cuesta poco | Formulario de tres pasos con foto (US06) |
| | | No pierde reportes por falta de señal | Cola local y sincronización automática (US07, US08) |
| | | Sostiene el hábito porque ve resultados | Consulta del estado de sus reportes (US13) |
| | Supervisor de SST | Se entera de inmediato y prioriza por severidad | Bandeja de hallazgos filtrable (US14) |
| | | Hace responsable a alguien con plazo | Asignación y cierre con acción correctiva (US15, US16) |
| | | Mide en lugar de suponer | Indicadores MTTR y cumplimiento (US35, US36) |
| | Comité de SST | Documenta sus decisiones y les da seguimiento | Actas con quórum y acuerdos (US32, US33, US34) |
| | | Mantiene viva la matriz IPERC | Entradas con origen en hallazgos reales (US20, US22) |
| | Empresa ante SUNAFIL | Demuestra gestión en lugar de solo documentación | Exportación de los registros obligatorios (US37) |
