# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

La estrategia de pruebas concentra el esfuerzo en el backend, y la razón es deliberada: en esta
arquitectura toda la lógica de negocio vive en el API, y ambos clientes la consumen. Probar el
API es probar la regla de negocio una vez para las dos plataformas; probarla en cada cliente
sería duplicar el esfuerzo sin aumentar la cobertura real del dominio.

**Herramientas.** pytest 8.3 con pytest-django 4.9 en el backend; el cliente de pruebas de
Django REST Framework (`APIClient`) para ejercitar los endpoints; verificación estática con
TypeScript y ESLint en la web, y compilación de Gradle en móvil.

### 6.1.1. Core Entities Unit Tests

Pruebas sobre las reglas de negocio de las entidades del dominio, sin pasar por HTTP.

| # | Prueba | Entidad | Qué verifica |
|---|---|---|---|
| 1 | `test_variante_es_estable_por_usuario` | `Experiment` | Que la variante asignada a un usuario sea la misma en llamadas sucesivas. Es la condición que hace válido el experimento: con asignación aleatoria, el mismo usuario podría ver un formulario distinto cada día y la comparación dejaría de medir el formulario |
| 2 | `test_occurred_at_puede_ser_anterior_al_registro` | `Report` | Que un reporte creado sin conexión conserve su fecha de ocurrencia, anterior a la de recepción |
| 3 | `test_comite_paritario_y_quorum` | `Committee` | Que `is_paritario()` detecte la igualdad de representaciones y que `quorum_required()` devuelva la mitad más uno de los titulares |
| 4 | `test_acta_sin_quorum_queda_marcada` | `Meeting` | Que un acta sin el quórum requerido quede marcada como inválida, y que al registrar los asistentes suficientes pase a válida |

<!-- COMPLETAR: agregar pruebas unitarias del cálculo de nivel de riesgo de IpercEntry y del
     cálculo de vencimiento de EppDelivery, que hoy están cubiertos indirectamente. -->

### 6.1.2. Core Integration Tests

Pruebas que ejercitan el API completo: enrutamiento, permisos, serialización y persistencia.

| # | Prueba | Módulo | Qué verifica |
|---|---|---|---|
| 1 | `test_operario_crea_reporte_minimo` | Reportes | Que el flujo rápido pueda crear un reporte enviando solo tipo y área, sin descripción |
| 2 | `test_sincronizacion_offline_no_duplica` | Reportes | Que reenviar el mismo `client_uuid` devuelva `200` con el reporte existente y que la base quede con un solo registro |
| 3 | `test_operario_no_ve_reportes_de_otros` | Reportes | Que el filtrado por rol se aplique en la consulta y no en la interfaz |
| 4 | `test_operario_no_puede_cerrar` | Reportes | Que el cierre esté restringido a supervisor y comité, devolviendo `403` |
| 5 | `test_supervisor_cierra_y_calcula_mttr` | Reportes / Métricas | Que al cerrar se selle la fecha y que el endpoint de MTTR refleje el hallazgo cerrado |
| 6 | `test_asignar_pasa_a_en_proceso` | Reportes | Que la asignación cambie el estado y agregue la entrada correspondiente a la bitácora |
| 7 | `test_supervisor_registra_el_comite` | Comité | Que el comité se cree en modo comité cuando la empresa supera los 20 trabajadores |
| 8 | `test_operario_no_registra_el_comite` | Comité | Que un operario no pueda constituir el comité |
| 9 | `test_no_se_puede_registrar_dos_comites` | Comité | Que una empresa no pueda tener dos comités simultáneos |
| 10 | `test_numero_de_acta_es_consecutivo_y_lo_pone_el_servidor` | Comité | Que el número de acta lo asigne el servidor de forma correlativa e ignore el valor enviado por el cliente |
| 11 | `test_cumplimiento_del_comite` | Comité | Que el indicador de cumplimiento de acuerdos se calcule correctamente |
| 12 | `test_sin_comite_el_endpoint_lo_dice` | Comité | Que el endpoint responda explícitamente cuando no hay comité, en lugar de fallar |
| 13 | `test_registro_publico_con_ruc` | Autenticación | Que el registro asocie al usuario a la empresa del RUC indicado |
| 14 | `test_el_registro_publico_no_permite_elegir_rol` | Autenticación | Que enviar `role=ADMIN` en el registro público se ignore y el usuario quede como operario. Es la prueba de una vulnerabilidad de escalada de privilegios detectada y corregida durante el desarrollo |
| 15 | `test_registro_con_ruc_inexistente_falla` | Autenticación | Que el registro con un RUC no registrado devuelva `400` con el mensaje correspondiente |
| 16 | `test_registro_rechaza_area_de_otra_empresa` | Autenticación | Que no se pueda asociar un área ajena a la empresa indicada |
| 17 | `test_contrasenas_distintas_fallan` | Autenticación | Que la confirmación de contraseña se valide |
| 18 | `test_operario_no_lista_usuarios` | Autenticación | Que el directorio de usuarios esté restringido a los roles de gestión |
| 19 | `test_supervisor_solo_ve_usuarios_de_su_empresa` | Autenticación | Que el aislamiento entre empresas se cumpla |
| 20 | `test_manager_puede_crear_un_supervisor` | Autenticación | Que la creación de usuarios con rol funcione para quien sí está autorizado |
| 21 | `test_supervisor_exporta_reportes` | Exportación | Que la exportación devuelva un `.xlsx` válido, que abra correctamente y contenga los datos |
| 22 | `test_operario_no_exporta_evidencia` | Exportación | Que la exportación esté restringida a los roles de gestión |
| 23 | `test_exportaciones_vacias_no_fallan` | Exportación | Que una empresa sin datos obtenga el formato con su cabecera en lugar de un error |
| 24 | `test_filtro_por_estado_en_la_exportacion` | Exportación | Que el filtro por estado se aplique al archivo generado |

<!-- IMAGEN REQUERIDA: captura de la ejecución de pytest mostrando el resumen de pruebas
     aprobadas, en assets/img/evidencia-pytest.png -->

### 6.1.3. Core Behavior-Driven Development

Los criterios de aceptación de las historias de usuario del Capítulo III están redactados en
formato Gherkin y constituyen la especificación del comportamiento esperado. La tabla siguiente
relaciona cada escenario con la prueba automatizada que lo verifica.

| Historia | Escenario Gherkin | Prueba que lo cubre |
|---|---|---|
| US06 | Reporte en tres pasos / descripción opcional | `test_operario_crea_reporte_minimo` |
| US08 | Reintento del mismo reporte | `test_sincronizacion_offline_no_duplica` |
| US11 | Sincronización diferida conserva la fecha | `test_occurred_at_puede_ser_anterior_al_registro` |
| US13 | Alcance por rol en la consulta | `test_operario_no_ve_reportes_de_otros` |
| US15 | Asignación pasa a en proceso | `test_asignar_pasa_a_en_proceso` |
| US16 | Cierre registra fecha y tiempo de resolución | `test_supervisor_cierra_y_calcula_mttr` |
| US17 | Operario intenta cerrar | `test_operario_no_puede_cerrar` |
| US30 | Constitución del comité según tamaño | `test_supervisor_registra_el_comite` |
| US31 | Verificación de paridad | `test_comite_paritario_y_quorum` |
| US32 | Numeración correlativa del acta | `test_numero_de_acta_es_consecutivo_y_lo_pone_el_servidor` |
| US33 | Acta sin quórum | `test_acta_sin_quorum_queda_marcada` |
| US34 | Recálculo del cumplimiento de acuerdos | `test_cumplimiento_del_comite` |
| US37 | Exportación y su permiso | `test_supervisor_exporta_reportes`, `test_operario_no_exporta_evidencia` |
| US38 | Estabilidad de la variante | `test_variante_es_estable_por_usuario` |

### 6.1.4. Core System Tests

Pruebas de extremo a extremo sobre el sistema desplegado, ejecutadas manualmente sobre los
escenarios principales.

| # | Escenario | Pasos | Resultado esperado |
|---|---|---|---|
| ST01 | Ciclo completo del hallazgo | El operario reporta desde el móvil → el supervisor lo ve en la web → asigna → cierra | El hallazgo aparece cerrado en ambos clientes y el MTTR se actualiza |
| ST02 | Reporte sin conexión | Se activa el modo avión → se reporta → se restablece la conexión | El reporte queda pendiente y luego se sincroniza sin duplicarse |
| ST03 | Paridad por rol | Un supervisor ejecuta asignación y cierre desde el móvil y desde la web | El resultado es idéntico en ambos canales |
| ST04 | Aislamiento entre empresas | Un usuario de la empresa A consulta reportes | No aparece ningún dato de la empresa B |
| ST05 | Evidencia ante auditoría | Se exportan los cinco registros a Excel | Los archivos abren correctamente y contienen la trazabilidad completa |
| ST06 | Asignación del experimento | Dos operarios de distinta variante abren el formulario | Cada uno ve la variante que le corresponde, de forma estable |

## 6.2. Static testing & Verification

### 6.2.1. Static Code Analysis

#### 6.2.1.1. Coding standard & Code conventions

| Repositorio | Herramienta | Configuración | Ejecución |
|---|---|---|---|
| `sst-api` | ruff 0.8 | Línea de 100 caracteres, reglas E (pycodestyle), F (pyflakes), I (orden de imports), UP (modernización), B (bugbear) y DJ (específicas de Django); migraciones excluidas | `ruff check .` en cada PR |
| `sst-api` | Django | `makemigrations --check --dry-run` detiene el PR si hay cambios de modelo sin migración generada | En cada PR |
| `sst-web` | ESLint 9 | Reglas recomendadas de JavaScript y TypeScript más `react-hooks` | `npm run lint` |
| `sst-web` | TypeScript 5.7 | Modo estricto, `noUnusedLocals`, `noUnusedParameters`, `noFallthroughCasesInSwitch` | `npm run typecheck` |
| `sst-mobile` | Compilador de Kotlin | Verificación de tipos y advertencias en la compilación | `gradle assembleDebug` |
| Los cuatro | Hook `commit-msg` + workflow | Conventional Commits | Local y en PR |

**Resultado de la última verificación estática de la aplicación web:** `tsc --noEmit` sin
errores de tipo y ESLint sin advertencias sobre los 22 archivos de TypeScript del proyecto.

<!-- IMAGEN REQUERIDA: captura de la ejecución de ruff, eslint y tsc sin errores, en
     assets/img/evidencia-analisis-estatico.png -->

#### 6.2.1.2. Code Quality & Code Security

**Hallazgos de seguridad detectados y corregidos durante el desarrollo**

| # | Hallazgo | Severidad | Corrección |
|---|---|---|---|
| S1 | El endpoint de registro público aceptaba el campo `role`, permitiendo que cualquiera se registrara como `ADMIN` o `SUPERVISOR` (escalada de privilegios) | Alta | El serializador de registro dejó de aceptar `role` y fuerza `OPERARIO`. Se agregó la prueba `test_el_registro_publico_no_permite_elegir_rol` para impedir la regresión |
| S2 | El registro permitía asociar un usuario a un área de otra empresa | Media | Validación cruzada en el serializador y prueba asociada |
| S3 | Los tokens JWT se almacenan en `localStorage` en la aplicación web | Media | Aceptado como riesgo conocido para el alcance académico. En producción el refresh token debería moverse a una cookie `httpOnly` para reducir la exposición ante XSS. **Documentado como deuda técnica, no como no hallazgo** |

**Prácticas de seguridad aplicadas**

- Autenticación con JWT de vida corta (60 minutos) y renovación mediante refresh token.
- Autorización verificada en el backend en cada consulta, no en la interfaz: el filtrado por
  rol se aplica en `get_queryset()`, de modo que ocultar un botón nunca es la medida de control.
- Aislamiento multiempresa: toda consulta se restringe a la empresa del usuario autenticado.
- Validación de contraseñas con los validadores de Django.
- Secretos fuera del repositorio mediante variables de entorno.
- Tráfico en claro permitido únicamente contra direcciones de desarrollo, declarado
  explícitamente en `network_security_config.xml`.

### 6.2.2. Reviews

| Práctica | Aplicación |
|---|---|
| Pull Request obligatorio | Ningún cambio llega a `develop` ni a `main` sin PR; las ramas están protegidas contra push directo |
| Plantilla de PR | Cada PR declara qué hace, el tipo de cambio y una lista de verificación: rama correcta, Conventional Commits, pruebas ejecutadas, migraciones generadas, documentación del API actualizada y aviso al resto del equipo si cambió el contrato |
| Verificación automática previa | El PR no puede integrarse con el pipeline en rojo |
| Revisión de código | Revisión del diff completo antes de integrar, con foco en reglas de negocio, permisos y comentarios que expliquen decisiones |

<!-- IMAGEN REQUERIDA: captura de un Pull Request con su plantilla completada y los checks del
     pipeline en verde, en assets/img/evidencia-pull-request.png -->

## 6.3. Validation Interviews

### 6.3.1. Diseño de Entrevistas

Las entrevistas de validación se realizan sobre el producto funcionando, no sobre el concepto.
El entrevistado ejecuta tareas reales mientras se observa y se registra.

**Tareas a ejecutar — segmento operario**

1. Regístrate en la aplicación con el RUC que te doy.
2. Reporta esta condición insegura que te muestro, con foto.
3. Muéstrame dónde ves si tu reporte ya fue atendido.
4. Da conformidad a la entrega de EPP que tienes pendiente.

**Tareas a ejecutar — segmento supervisor**

1. Encuentra el hallazgo crítico que está abierto hace más días.
2. Asígnalo a alguien de tu equipo y ciérralo indicando qué se hizo.
3. Agrega a la matriz IPERC un peligro que venga de ese hallazgo.
4. Genera la evidencia que le mostrarías a un inspector de SUNAFIL.

**Preguntas posteriores a las tareas**

1. ¿Qué te resultó más confuso de lo que acabas de hacer?
2. ¿Qué esperabas que pasara y no pasó?
3. Si mañana tuvieras esto en tu trabajo, ¿lo usarías? ¿Qué te lo impediría?
4. ¿Qué le falta para reemplazar lo que usas hoy?

**Métricas de observación por tarea:** tiempo de ejecución, número de toques o clics,
finalización sin ayuda, y errores cometidos.

### 6.3.2. Registro de Entrevistas

### 6.3.3. Evaluaciones según heurísticas

## 6.4. Auditoría de Experiencias de Usuario

### 6.4.1. Auditoría realizada

#### 6.4.1.1. Información del grupo auditado

#### 6.4.1.2. Cronograma de auditoría realizada

#### 6.4.1.3. Contenido de auditoría realizada

### 6.4.2. Auditoría recibida

#### 6.4.2.1. Información del grupo auditor

#### 6.4.2.2. Cronograma de auditoría recibida

#### 6.4.2.3. Contenido de auditoría recibida

#### 6.4.2.4. Resumen de modificaciones para subsanar hallazgos

