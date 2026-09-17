# Conclusiones

## Conclusiones y recomendaciones

**Sobre la arquitectura y la paridad entre plataformas.** Concentrar la totalidad de la lógica de
negocio en un único API REST consumido por ambos clientes resultó ser la decisión más
consecuente del proyecto. No solo evita la duplicación: hace **imposible** que la regla de
negocio diverja entre la web y el móvil, que es el requisito de paridad que el proyecto debía
satisfacer. Cuando el registro público dejó de aceptar el rol como campo de entrada, la
corrección aplicó simultáneamente a los tres clientes posibles sin tocar ninguno.

**Sobre el diseño para el contexto real de uso.** La operación sin conexión no es una
funcionalidad adicional sino una condición de existencia del producto. Un sistema de reporte de
peligros que exige conectividad no sirve en una obra o en una mina, que es exactamente donde los
peligros son mayores. La consecuencia técnica —guardar localmente antes de intentar el envío, e
identificar cada reporte con un UUID generado en el dispositivo para que el reintento no
duplique— nace de una restricción del dominio, no de una preferencia de ingeniería.

**Sobre la separación de responsabilidades como requisito de negocio.** La restricción de que
quien reporta no pueda cerrar su propio hallazgo no es una decisión de diseño de software: es lo
que la normativa de SST exige, y su implementación en el backend —verificada por pruebas
automatizadas— convierte un requisito legal en una propiedad del sistema. Descubrir que el
endpoint de registro permitía saltarse ese control, y corregirlo, fue el hallazgo de seguridad
más relevante del desarrollo.

**Sobre la medición como parte del producto.** Instrumentar el experimento dentro del propio
modelo de datos, en lugar de delegarlo a una herramienta de analítica externa, resultó coherente
con el contexto de uso: los eventos de una herramienta externa se pierden justamente cuando no
hay conectividad. El costo es un campo adicional en la tabla de reportes; el beneficio es que el
dato del experimento es tan confiable como el dato operativo.

**Sobre el rigor experimental y sus límites.** El cálculo de tamaño de muestra determinó que se
requieren 24 participantes para detectar, con significancia del 5 % y potencia del 80 %, el
efecto que la hipótesis afirma. Ese número es la conclusión metodológica más importante del
trabajo, porque define cuándo un resultado es interpretable y cuándo no. Un experimento
ejecutado con seis participantes solo podría detectar efectos superiores al 232 %: un resultado
no significativo en esas condiciones no refuta nada.

**Recomendaciones para la continuidad del producto**

1. Ejecutar el experimento con el número de participantes que el cálculo exige, o declarar
   explícitamente la limitación y reportar el estudio como no concluyente.
2. Implementar el circuito de retroalimentación al operario —avisarle cuando su hallazgo se
   cierra—, porque la evidencia del dominio sugiere que la ausencia de consecuencia visible es
   una causa central del abandono del reporte.
3. Priorizar el reporte anónimo opcional para actos inseguros de terceros, que ataca la barrera
   que la reducción de fricción no puede resolver.
4. Completar el pipeline hasta el despliegue automatizado y añadir notificaciones, que hoy están
   diseñadas pero no implementadas.
5. Mover el refresh token a una cookie `httpOnly` antes de cualquier uso en producción.

## Video App Validation

## Video About-the-Team

