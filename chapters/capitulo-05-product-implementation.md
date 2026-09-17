# Capítulo V: Product Implementation

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

| Propósito | Herramienta | Versión | Justificación |
|---|---|---|---|
| Control de versiones | Git | 2.45 | Estándar del curso; requerido para GitFlow y Conventional Commits |
| Alojamiento y colaboración | GitHub (organización pública `sst-peru`) | — | Exigido por el enunciado: organización pública con evidencia de commits |
| Automatización | GitHub Actions | — | Integrado al repositorio, sin infraestructura adicional |
| Backend | Python | 3.13 | Soportado por Django 5.1 |
| Framework backend | Django + Django REST Framework | 5.1.4 / 3.15.2 | Django aporta ORM, migraciones, autenticación y panel de administración; DRF añade el API REST |
| Documentación del API | drf-spectacular | 0.28.0 | Genera OpenAPI desde el código, evitando que el contrato se desactualice |
| Autenticación | djangorestframework-simplejwt | 5.3.1 | JWT consumido igual por web y móvil |
| Exportación de evidencia | openpyxl | 3.1.5 | Generación de .xlsx sin dependencias externas |
| Base de datos | PostgreSQL / SQLite | 16 / 3 | PostgreSQL en despliegue; SQLite en desarrollo local |
| Frontend web | React + TypeScript + Vite | 18.3 / 5.7 / 6.0 | TypeScript da verificación estática del contrato del API; Vite acelera el ciclo de desarrollo |
| Estado del servidor en la web | TanStack Query | 5.62 | Manejo de caché e invalidación sin escribir un reducer por pantalla |
| Cliente HTTP web | Axios | 1.7 | Interceptores para JWT y renovación de token |
| Móvil | Kotlin + Jetpack Compose | 2.0.21 / BOM 2024.12 | Android nativo con interfaz declarativa |
| Persistencia local móvil | Room | 2.6.1 | Cola de reportes pendientes de envío |
| Sincronización móvil | WorkManager | 2.10.0 | Reintento con backoff al recuperar la conectividad |
| Red móvil | Retrofit + OkHttp | 2.11 / 4.12 | Cliente HTTP con interceptor de autenticación |
| Entorno de desarrollo | Visual Studio Code / Android Studio | — | Edición del backend y la web; compilación y emulación Android |
| Pruebas backend | pytest + pytest-django | 8.3 / 4.9 | Suite de pruebas del API |
| Análisis estático | ruff / ESLint / TypeScript | 0.8 / 9.17 / 5.7 | Verificación sin ejecutar el código |

### 5.1.2. Source Code Management

**Repositorios.** El producto se organiza en tres repositorios independientes más el del informe,
todos dentro de la organización pública `sst-peru`:

| Repositorio | Contenido |
|---|---|
| `sst-api` | API REST en Django; concentra el modelo de dominio y las reglas de negocio |
| `sst-web` | Panel web en React |
| `sst-mobile` | Aplicación Android nativa |
| `sst-report` | Este informe |

La separación responde a que cada uno tiene su propio ciclo de construcción, su propio pipeline
y su propio lenguaje; un monorepo habría obligado a ejecutar los tres pipelines ante cualquier
cambio.

**Modelo de ramas.**

| Rama | Propósito | Sale de | Vuelve a |
|---|---|---|---|
| `main` | Solo versiones entregables, etiquetadas | — | — |
| `develop` | Integración del trabajo en curso | main | — |
| `feature/*` | Nueva funcionalidad | develop | develop |
| `fix/*` | Corrección de defecto | develop | develop |
| `docs/*` | Redacción del informe | develop | develop |
| `chore/*` | Infraestructura y configuración | develop | develop |

Reglas de protección aplicadas en GitHub: `main` y `develop` no aceptan push directo ni
force push; la integración ocurre exclusivamente por Pull Request; `develop` es la rama por
defecto, de modo que los PR apuntan ahí sin intervención.

**Conventional Commits.** Todos los mensajes siguen `tipo(alcance): descripción`. Ejemplos
reales del historial del proyecto:

```
feat(auth): agregar empresa, areas, usuario con roles y endpoints de registro y login
feat(reports): agregar reportes de actos y condiciones inseguras con cierre y bitacora
feat(sync): subir reportes pendientes con workmanager cuando vuelve la red
fix(reports): redondear la latitud y longitud del gps antes de validar
fix(auth)!: impedir que el registro publico elija su propio rol y agregar endpoint de usuarios
test(reports): cubrir creacion offline, permisos por rol y calculo de mttr
ci: agregar workflows de tests, lint y validacion de conventional commits
```

El signo `!` marca un cambio que rompe el contrato del API, como ocurrió al retirar el campo
`role` del registro público.

La convención se verifica en dos momentos: un hook `commit-msg` local la rechaza antes de crear
el commit, y un workflow de GitHub Actions la valida sobre todos los commits del Pull Request.
Tener ambas capas importa porque el hook local puede no estar instalado en una máquina nueva.

### 5.1.3. Source Code Style Guide & Conventions

| Ámbito | Convención | Verificación |
|---|---|---|
| Python | PEP 8 con línea de 100 caracteres; `ruff` con las reglas E, F, I, UP, B y DJ | `ruff check .` en CI |
| Nombres en Python | `snake_case` para funciones y variables, `PascalCase` para clases, español para el vocabulario de dominio y inglés para los nombres del framework | Revisión en PR |
| TypeScript | ESLint con reglas recomendadas más `react-hooks`; modo estricto de TypeScript con `noUnusedLocals` y `noUnusedParameters` | `npm run lint` y `npm run typecheck` en CI |
| Nombres en TypeScript | `camelCase` para variables y funciones, `PascalCase` para componentes y tipos | Revisión en PR |
| Kotlin | Estilo oficial de Kotlin (`kotlin.code.style=official`); composables en `PascalCase` | Compilación en CI |
| CSS | Propiedades personalizadas para toda la paleta; sin valores de color literales fuera de `:root` | Revisión en PR |
| Comentarios | Se comenta el **porqué**, no el qué. Un comentario que repite el código se elimina en revisión | Revisión en PR |
| Fin de línea | LF en el repositorio, forzado por `.gitattributes`; CRLF solo en `.bat`, `.cmd` y `.ps1` | `.gitattributes` |
| Idioma | Código y mensajes de commit sin tildes ni eñes; interfaz y documentación en español correcto | Revisión en PR |

### 5.1.4. Software Deployment Configuration

| Componente | Configuración |
|---|---|
| API | Variables de entorno mediante archivo `.env` (`DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, `DATABASE_URL`, `CORS_ALLOWED_ORIGINS`). `DATABASE_URL` vacío usa SQLite; con valor, PostgreSQL |
| Web | `VITE_API_URL` define el API consumido. En desarrollo, Vite hace proxy de `/api` al backend, evitando CORS |
| Móvil | `API_BASE_URL` se inyecta como `buildConfigField` en Gradle. En emulador, `http://10.0.2.2:8000/api/v1/`, que es la dirección con la que el emulador alcanza el `localhost` del anfitrión |
| Tráfico en claro | `network_security_config.xml` permite HTTP sin cifrar únicamente contra direcciones de desarrollo; en producción el API va por HTTPS |
| Secretos | Ningún secreto se versiona: `.env` está en `.gitignore` y se distribuye `.env.example` con los nombres de variable |

## 5.2. Product Implementation & Deployment

### 5.2.1. Sprint Backlogs

El ciclo se organizó en dos sprints. El Product Backlog del Capítulo III contiene los 162
elementos del producto; los dos Sprint Backlogs que siguen contienen exactamente aquello a lo que
el equipo se comprometió y entregó: 86 elementos y 319 Story Points. Los elementos marcados
*Propuesta* en el Capítulo III no figuran en ningún sprint, precisamente porque no se
construyeron.

**Criterio de división.** El Sprint 1 cierra el **ciclo de vida de un hallazgo** de extremo a
extremo: que el operario lo registre con evidencia y que el supervisor lo reciba, lo asigne y lo
cierre. El Sprint 2 construye sobre ese cimiento **el resto del sistema de gestión**: la matriz
IPERC, el control de EPP, las inspecciones, el comité, las métricas y la evidencia exportable, más
las cuentas, los roles y la calidad de uso. El orden no es arbitrario: sin el ciclo del hallazgo
funcionando, ninguno de los registros del Sprint 2 tendría de dónde alimentarse.

**Sprint 1**

| Campo | Valor |
|---|---|
| Objetivo | Cerrar el ciclo del hallazgo de extremo a extremo: registrarlo en campo con evidencia, recibirlo, asignarlo y cerrarlo con la acción correctiva aplicada. |
| Elementos comprometidos | 15 |
| Story Points planificados | 60 |
| Story Points completados | 60 |
| Incremento entregable | Un operario registra un acto o condición insegura con foto, ubicación y fecha real desde el celular o la web; el supervisor lo ve en su bandeja, lo asigna y lo cierra; la bitácora queda con quién hizo qué y cuándo. |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US02 | Inicio de sesión | Ambas | 3 | Completado |
| US06 | Reporte rápido desde el celular | Ambas | 8 | Completado |
| US13 | Consulta de mis reportes | Ambas | 3 | Completado |
| US43 | Menú según mi rol | Ambas | 3 | Completado |
| US14 | Bandeja de hallazgos | Ambas | 5 | Completado |
| US16 | Cierre con acción correctiva | Ambas | 5 | Completado |
| US15 | Asignación de responsable | Ambas | 5 | Completado |
| US18 | Bitácora del hallazgo | Ambas | 3 | Completado |
| US09 | Evidencia fotográfica | Ambas | 5 | Completado |
| US10 | Geolocalización del hallazgo | Ambas | 5 | Completado |
| US11 | Fecha real de ocurrencia | Ambas | 3 | Completado |
| US47 | Categorías según el tipo de hallazgo | Ambas | 2 | Completado |
| TS02 | Convenciones de commits | Los cuatro | 2 | Completado |
| TS05 | Flujo de ramas GitFlow | Los cuatro | 3 | Completado |
| TS01 | Integración continua | Los cuatro | 5 | Completado |

Las doce historias de usuario de este sprint están marcadas `Ambas` en el Capítulo III: el
incremento es demostrable tanto desde el panel web como desde la aplicación Android, que es la
condición de paridad que el proyecto se impuso.

**Sprint 2**

| Campo | Valor |
|---|---|
| Objetivo | Completar el sistema de gestión sobre el ciclo del hallazgo ya funcionando: matriz IPERC, control de EPP, inspecciones, comité de SST, métricas, evidencia exportable, cuentas y calidad de uso. |
| Elementos comprometidos | 71 |
| Story Points planificados | 259 |
| Story Points completados | 259 |
| Incremento entregable | El supervisor y el comité disponen de los registros obligatorios de la Ley N° 29783 en el sistema: peligros evaluados y versionados, entregas de EPP con conformidad, inspecciones programadas y ejecutadas con checklist, actas del comité con quórum y acuerdos, indicadores de gestión y exportación de la evidencia a Excel. |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US07 | Reporte sin conexión | Móvil | 13 | Completado |
| US08 | Sincronización sin duplicados | Ambas | 8 | Completado |
| US70 | Sesión que no expira en campo | Ambas | 5 | Completado |
| US17 | Separación de responsabilidades | Ambas | 3 | Completado |
| US35 | Indicador MTTR | Ambas | 5 | Completado |
| US50 | Filtrar la bandeja | Ambas | 3 | Completado |
| US49 | Descartar un reporte | Web | 2 | Completado |
| US12 | Reporte desde la web | Web | 5 | Completado |
| US44 | Vista previa de la evidencia | Web | 3 | Completado |
| US45 | Ampliar la evidencia | Web | 3 | Completado |
| US46 | Reemplazar la foto elegida | Web | 2 | Completado |
| US48 | Estado de envío de mis reportes | Móvil | 3 | Completado |
| US51 | Ubicar el hallazgo en el mapa | Web | 1 | Completado |
| US38 | Asignación de variante | Ambas | 5 | Completado |
| US39 | Registro de la variante en el reporte | Ambas | 2 | Completado |
| US40 | Resultados del experimento | Web | 5 | Completado |
| US64 | Variante disponible sin conexión | Móvil | 3 | Completado |
| US01 | Registro de trabajador | Ambas | 5 | Completado |
| US03 | Sesión persistente en campo | Ambas | 3 | Completado |
| US05 | Gestión de áreas | Web | 2 | Completado |
| US04 | Administración de usuarios | Web | 5 | Completado |
| US41 | Cambio de rol de un usuario | Web | 2 | Completado |
| US42 | Cierre de sesión | Ambas | 1 | Completado |
| US19 | Consulta de la matriz en campo | Ambas | 3 | Completado |
| US20 | Registro de peligros | Web | 5 | Completado |
| US21 | Versionado de la matriz | Web | 5 | Completado |
| US22 | Trazabilidad con el hallazgo de origen | Ambas | 3 | Completado |
| US52 | Consultar versiones anteriores de la matriz | Web | 5 | Completado |
| US53 | Publicar una nueva versión de la matriz | Web | 5 | Completado |
| US54 | Retirar un peligro de la matriz | Web | 2 | Completado |
| US23 | Catálogo de EPP | Web | 3 | Completado |
| US24 | Registro de entrega | Web | 3 | Completado |
| US25 | Conformidad del trabajador | Ambas | 3 | Completado |
| US26 | Alerta de EPP vencido | Ambas | 2 | Completado |
| US55 | Control de stock del catálogo | Web | 2 | Completado |
| US27 | Programa de inspecciones | Web | 5 | Completado |
| US28 | Ejecución con checklist | Ambas | 5 | Completado |
| US29 | Inspecciones vencidas | Ambas | 3 | Completado |
| US56 | Programar la siguiente inspección | Web | 3 | Completado |
| US36 | Tasa de cumplimiento de inspecciones | Ambas | 5 | Completado |
| US57 | Cumplimiento por área | Web | 3 | Completado |
| US30 | Constitución del comité | Web | 3 | Completado |
| US31 | Miembros y paridad | Web | 5 | Completado |
| US32 | Acta de reunión | Web | 5 | Completado |
| US33 | Control de quórum | Ambas | 3 | Completado |
| US34 | Acuerdos con responsable y plazo | Web | 3 | Completado |
| US58 | Advertencia de comité no paritario | Web | 2 | Completado |
| US59 | Seguimiento del estado de los acuerdos | Web | 2 | Completado |
| US60 | Consultar las actas desde el celular | Móvil | 3 | Completado |
| US37 | Exportación de evidencia | Web | 8 | Completado |
| US61 | MTTR por severidad | Ambas | 3 | Completado |
| US62 | Exportar cada registro obligatorio | Web | 3 | Completado |
| US63 | Resumen de hallazgos | Ambas | 3 | Completado |
| US65 | Identidad visual consistente | Ambas | 5 | Completado |
| US66 | Navegación siempre accesible | Ambas | 2 | Completado |
| US67 | Uso desde pantallas pequeñas | Web | 5 | Completado |
| US68 | Errores comprensibles | Ambas | 3 | Completado |
| US69 | Reintento ante fallo de red | Móvil | 3 | Completado |
| TS07 | Validación local del mensaje de commit | Los cuatro | 2 | Completado |
| TS06 | Fin de línea normalizado | Los cuatro | 2 | Completado |
| TS13 | Migraciones verificadas en integración | sst-api | 2 | Completado |
| TS03 | Documentación viva del API | sst-api | 2 | Completado |
| TS08 | Configuración por variables de entorno | sst-api | 3 | Completado |
| TS09 | Proxy de desarrollo | sst-web | 2 | Completado |
| TS10 | Renovación transparente del token | sst-web, sst-mobile | 5 | Completado |
| TS11 | Aislamiento entre empresas | sst-api | 5 | Completado |
| TS12 | Idempotencia en la creación de reportes | sst-api | 5 | Completado |
| TS04 | Datos de demostración | sst-api | 5 | Completado |
| TS14 | APK publicado por el pipeline | sst-mobile | 3 | Completado |
| TS15 | Generación de evidencia en Excel | sst-api | 5 | Completado |
| TS16 | Informe compilable y con índice verificado | sst-report | 3 | Completado |

**Resumen de los dos sprints**

| Sprint | Elementos | Story Points | Objetivo |
|---|---|---|---|
| Sprint 1 | 15 | 60 | Cerrar el ciclo del hallazgo de extremo a extremo. |
| Sprint 2 | 71 | 259 | Completar los registros del SGSST sobre ese ciclo. |
| **Total** | **86** | **319** | |

**Velocidad.** Los dos sprints completaron la totalidad de lo comprometido; no hubo arrastre de
uno al siguiente. Conviene señalar, sin embargo, que los sprints son marcadamente desiguales: el
Sprint 2 cuadruplica en Story Points al Sprint 1. Eso no es una buena práctica de planificación
—un sprint debe caber en una capacidad estable— y refleja que el alcance se agrupó por afinidad
funcional antes que por capacidad del equipo. Se documenta como lo que es: una decisión de
organización del trabajo, no una velocidad sostenible sobre la cual planificar.

**Sobre el periodo de ejecución.** Conviene decirlo con precisión, porque el historial de los
repositorios es público y cualquiera puede contrastarlo: los sprints **organizan el alcance, no
ventanas de calendario**. El trabajo se ejecutó en sesiones intensivas de desarrollo entre el 12 y
el 16 de septiembre de 2026, que es lo que muestran las fechas de los commits en `sst-api`,
`sst-web`, `sst-mobile` y `sst-report`. Por eso las tablas no declaran fechas de inicio y fin:
declararlas repartidas en semanas sería contradecir un dato verificable en un clic.

> **Limitación reconocida.** Un ciclo de desarrollo comprimido impide observar lo que la práctica
> iterativa busca: retroalimentación del usuario entre iteraciones que reoriente el alcance de la
> siguiente. Los dos sprints se ejecutaron sobre un plan fijado de antemano. Se documenta como
> limitación del trabajo, no como práctica recomendable.

### 5.2.2. Implemented Landing Page Evidence

<!-- IMAGEN REQUERIDA: capturas de la landing page desplegada en
     assets/img/evidencia-landing-*.png, más su URL pública, una vez construida. -->

### 5.2.3. Implemented Frontend-Web Application Evidence

<!-- IMAGEN REQUERIDA: capturas del panel web en ejecución, una por pantalla, en
     assets/img/evidencia-web-<pantalla>.png. Lista sugerida:
     acceso, registro, tablero, bandeja de hallazgos, detalle con bitácora, matriz IPERC,
     inspecciones con checklist, EPP, comité con actas, usuarios, experimento A/B. -->

La aplicación web está implementada en React con TypeScript y cubre la totalidad de las
funcionalidades disponibles para los roles de supervisor y comité, además del reporte para
cualquier rol.

| Pantalla | Ruta | Funcionalidad implementada |
|---|---|---|
| Acceso | `/login` | Autenticación con JWT |
| Registro | `/registro` | Alta de trabajador por RUC de empresa |
| Tablero | `/` | MTTR, hallazgos abiertos, cumplimiento de inspecciones, vencidas, acuerdos y actas del comité |
| Reportes | `/reportes` | Bandeja filtrable por estado, tipo y área |
| Nuevo reporte | `/reportes/nuevo` | Formulario en sus dos variantes del experimento, con foto, vista previa ampliable y captura de ubicación |
| Detalle | `/reportes/:id` | Datos completos, bitácora, asignación de responsable y cierre con acción correctiva |
| Matriz IPERC | `/iperc` | Consulta y edición de entradas con cálculo del nivel de riesgo |
| Inspecciones | `/inspecciones` | Programas, generación de ocurrencias, ejecución con checklist e indicadores |
| EPP | `/epp` | Catálogo, registro de entregas y conformidad del trabajador |
| Comité | `/comite` | Constitución, miembros, paridad, actas con quórum y acuerdos |
| Usuarios y áreas | `/usuarios` | Alta de usuarios con rol y gestión de áreas |
| Experimento | `/experimento` | Resultados comparados por variante |

### 5.2.4. Acuerdo de Servicio - SaaS

Resguardo se ofrece como servicio en la nube: la empresa cliente no instala ni administra
servidores. Eso traslada al proveedor obligaciones que conviene fijar por escrito, sobre todo
tratándose de información que la empresa debe poder exhibir ante una fiscalización de SUNAFIL y
que incluye datos personales de sus trabajadores.

El acuerdo siguiente es el **nivel de servicio propuesto** para el producto. No está en vigor
—el sistema todavía no opera en producción con clientes reales— y se documenta aquí como parte
del diseño del servicio, no como un contrato suscrito.

**1. Alcance del servicio**

| Componente | Qué cubre |
|---|---|
| API y base de datos | Disponibilidad, respaldo y conservación de todos los registros del SGSST |
| Panel web | Acceso desde navegador para supervisor, comité y administrador |
| Aplicación Android | Distribución de la aplicación y compatibilidad con las dos últimas versiones mayores de Android |
| Evidencia documental | Generación de las exportaciones de los registros obligatorios |

**2. Disponibilidad**

| Parámetro | Compromiso |
|---|---|
| Disponibilidad mensual del API y del panel web | 99,5 % |
| Equivalente en indisponibilidad | Hasta 3 h 39 min por mes |
| Medición | Sobre el total de minutos del mes calendario, excluyendo la ventana de mantenimiento programada |
| Ventana de mantenimiento | Domingos de 02:00 a 05:00 (hora de Perú), avisada con 72 horas de anticipación |

La aplicación móvil queda fuera de este cómputo por diseño: opera sin conexión y sincroniza
cuando hay red, de modo que una caída del servicio no impide que el trabajador registre un
hallazgo. Ese es precisamente el motivo de la arquitectura sin conexión.

**3. Atención de incidencias**

| Severidad | Definición | Primera respuesta | Objetivo de solución |
|---|---|---|---|
| **Crítica** | El servicio no está disponible o no se pueden registrar hallazgos | 1 hora | 4 horas |
| **Alta** | Una funcionalidad de un registro obligatorio no opera y no hay forma de sortearla | 4 horas | 1 día hábil |
| **Media** | Funcionalidad degradada con alternativa disponible | 1 día hábil | 5 días hábiles |
| **Baja** | Consulta, mejora o defecto cosmético | 2 días hábiles | Según planificación |

Horario de atención: lunes a viernes de 08:00 a 18:00 (hora de Perú) para severidades media y
baja; veinticuatro horas para severidad crítica.

**4. Respaldo, retención y continuidad**

| Parámetro | Compromiso |
|---|---|
| Frecuencia de respaldo | Diaria, con copia cifrada fuera del servidor principal |
| Retención de respaldos | 30 días de copias diarias y 12 copias mensuales |
| RPO (pérdida máxima de datos) | 24 horas |
| RTO (tiempo máximo de restablecimiento) | 8 horas |
| Prueba de restauración | Trimestral, en entorno separado, con constancia del resultado |
| Conservación de registros del SGSST | Mientras dure el contrato y por el plazo que exige la normativa peruana de conservación de registros de seguridad y salud en el trabajo |

**5. Tratamiento de datos personales**

El sistema almacena DNI, teléfono, fotografías tomadas en campo y coordenadas de geolocalización
de trabajadores. Todo ello es dato personal bajo la **Ley N° 29733, Ley de Protección de Datos
Personales**, y su tratamiento se sujeta a las siguientes condiciones:

| Condición | Compromiso |
|---|---|
| Titularidad | Los datos son de la empresa cliente; el proveedor actúa como encargado del tratamiento, nunca como titular |
| Finalidad | Exclusivamente la gestión del sistema de seguridad y salud en el trabajo; no se usan para ningún otro fin ni se ceden a terceros |
| Aislamiento | Cada empresa accede únicamente a sus propios datos, restricción aplicada en el backend y no en la interfaz |
| Geolocalización | Es opcional y revocable por el trabajador; negarla no impide reportar |
| Subencargados | Se informa a la empresa cliente qué proveedores de infraestructura intervienen y dónde se alojan los datos |
| Incidentes de seguridad | Notificación a la empresa cliente dentro de las 48 horas de detectado un acceso no autorizado a datos personales |

**6. Terminación y devolución de la información**

| Situación | Compromiso |
|---|---|
| Terminación por cualquier causa | La empresa dispone de 60 días para descargar la totalidad de su información |
| Formato de devolución | Formatos abiertos y legibles sin el sistema: hojas de cálculo para los registros y archivos originales para las fotografías |
| Eliminación posterior | Cumplido el plazo, los datos se eliminan de los sistemas activos y de los respaldos en el siguiente ciclo de rotación |
| Sin retención como palanca comercial | La devolución no se condiciona al pago de conceptos distintos de los ya vencidos por el servicio prestado |

**7. Exclusiones**

No quedan cubiertos por los compromisos de disponibilidad: las interrupciones causadas por fallas
de la conexión a internet de la empresa cliente, los eventos de fuerza mayor, las suspensiones por
falta de pago previamente notificadas, y el uso del servicio fuera de las condiciones acordadas.

**8. Reporte de cumplimiento**

El proveedor publica mensualmente la disponibilidad alcanzada y el detalle de las incidencias de
severidad crítica y alta del periodo, con su tiempo de respuesta y de solución. Sin esa
publicación, el compromiso del punto 2 no sería verificable por el cliente y, por tanto, no sería
un compromiso.

### 5.2.5. Implemented Native-Mobile Application Evidence

<!-- IMAGEN REQUERIDA: capturas de la aplicación Android en ejecución en
     assets/img/evidencia-movil-<pantalla>.png. Lista sugerida: acceso, registro, formulario
     rápido en sus tres pasos, formulario largo, lista de reportes con pendientes de envío,
     detalle del hallazgo, IPERC, mis EPP, inspecciones con checklist, tablero. -->

| Pantalla | Funcionalidad implementada |
|---|---|
| Acceso y registro | Autenticación JWT y alta de trabajador por RUC |
| Reportar | Formulario rápido de tres pasos y formulario largo, según la variante asignada |
| Mis reportes | Cola local con estado de envío y listado del servidor con filtros |
| Detalle del hallazgo | Bitácora, foto, tiempo de resolución; asignación y cierre para supervisor y comité |
| Matriz IPERC | Consulta de peligros y controles por puesto |
| Mis EPP | Entregas, vencimientos y conformidad del trabajador |
| Inspecciones | Listado y ejecución con checklist |
| Tablero | MTTR, cumplimiento de inspecciones y acuerdos del comité |

### 5.2.6. Implemented RESTful API and/or Serverless Backend Evidence

El API expone 8 módulos de dominio bajo el prefijo `/api/v1/`.

| Módulo | Endpoints principales |
|---|---|
| Autenticación | `POST auth/register/`, `POST auth/login/`, `POST auth/refresh/`, `GET auth/me/`, CRUD `auth/users/`, CRUD `auth/areas/` |
| Reportes | CRUD `reports/`, `POST reports/{id}/assign/`, `POST reports/{id}/close/`, `POST reports/{id}/change-status/`, CRUD `categories/` |
| IPERC | CRUD `iperc/matrices/`, CRUD `iperc/entries/` |
| EPP | CRUD `epp/items/`, CRUD `epp/deliveries/` |
| Inspecciones | CRUD `inspections/schedules/`, `POST inspections/schedules/{id}/generate-next/`, CRUD `inspections/`, `POST inspections/{id}/complete/` |
| Comité | CRUD `committee/`, `committee/members/`, `committee/meetings/`, `committee/agreements/`, `GET committee-compliance/` |
| Métricas | `GET metrics/mttr/`, `GET metrics/inspection-compliance/`, `GET metrics/reports-summary/` |
| Experimento | `GET experiments/my-variant/`, `GET experiments/{key}/results/` |
| Exportación | `GET exports/reports.xlsx`, `iperc.xlsx`, `epp.xlsx`, `inspections.xlsx`, `committee.xlsx` |

**Dos decisiones de implementación que conviene destacar en la sustentación:**

*Idempotencia en la creación de reportes.* `POST reports/` recibe un `client_uuid` generado por
el dispositivo antes del envío. Si el reporte con ese identificador ya existe, el API responde
`200` con el reporte existente en lugar de crear uno nuevo y responder `201`. Sin esta decisión,
un reintento tras una conexión interrumpida —el caso normal en obra— duplicaría el hallazgo y
distorsionaría todas las métricas.

*El rol no se acepta del cliente.* El registro público fuerza el rol `OPERARIO`. Si se aceptara
del cliente, cualquiera podría registrarse como supervisor y cerrar sus propios hallazgos,
rompiendo la separación de responsabilidades que la normativa exige. Los usuarios con otros
roles se crean desde `auth/users/`, que requiere ser supervisor o miembro del comité.

<!-- IMAGEN REQUERIDA: captura de la interfaz Swagger en /api/docs/ mostrando los módulos
     desplegados, en assets/img/evidencia-api-swagger.png -->

### 5.2.7. RESTful API documentation

La documentación se genera automáticamente desde el código con drf-spectacular, de modo que el
contrato publicado no puede divergir de la implementación.

| Recurso | Ruta |
|---|---|
| Interfaz interactiva (Swagger UI) | `/api/docs/` |
| Especificación OpenAPI 3 | `/api/schema/` |

Todos los endpoints requieren autenticación JWT mediante la cabecera `Authorization: Bearer
<token>`, con la excepción de `auth/register/`, `auth/login/` y `auth/refresh/`.

### 5.2.8. Team Collaboration Insights

<!-- IMAGEN REQUERIDA: capturas de GitHub → Insights → Contributors y Commits de cada uno de
     los cuatro repositorios, en assets/img/insights-<repo>.png -->

## 5.3. Video About-the-Product

