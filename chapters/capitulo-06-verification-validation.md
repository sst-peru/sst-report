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

> **PENDIENTE.** Actualizar el número total de pruebas y adjuntar la captura de la ejecución
> después de la última corrida.

