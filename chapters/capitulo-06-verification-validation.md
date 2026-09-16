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

