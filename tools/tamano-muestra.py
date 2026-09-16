#!/usr/bin/env python3
"""Cálculo del tamaño de muestra del experimento A/B de Resguardo.

    python tools/tamano-muestra.py

Compara la media de reportes por usuario entre dos grupos independientes (formulario rápido
frente a formulario largo). Usa la aproximación normal para la diferencia de medias:

    n por grupo = 2 · (Z(α/2) + Z(β))² · σ² / Δ²

Se asume que el número de reportes por usuario en la ventana de medición se comporta de forma
aproximadamente Poisson, por lo que la varianza se estima igual a la media. Es una aproximación
conservadora y explícita: si la dispersión real resulta mayor (sobredispersión, algo común en
conteos de comportamiento humano), el tamaño necesario será mayor y debe recalcularse con la
varianza observada en el piloto.
"""
from math import ceil

# --- Parámetros del diseño -------------------------------------------------
ALFA = 0.05          # nivel de significancia, dos colas
POTENCIA = 0.80      # potencia estadística
Z_ALFA_2 = 1.959964  # valor crítico de Z para α/2 = 0.025
Z_BETA = {0.80: 0.841621, 0.90: 1.281552, 0.95: 1.644854}

# --- Supuestos del dominio -------------------------------------------------
# Tasa base del grupo de control (formulario largo), en reportes por usuario y por día.
# ¡Debe calibrarse con datos reales del piloto antes de la entrega!
TASA_BASE_DIARIA = 0.15
DIAS_DE_MEDICION = 14
MDE_RELATIVO = 1.00   # efecto mínimo detectable: +100 % (la hipótesis dice "el doble")


def tamano_por_grupo(media_control, media_tratamiento, potencia=POTENCIA):
    """Devuelve el número de usuarios necesarios por grupo."""
    z_beta = Z_BETA[potencia]
    varianza = (media_control + media_tratamiento) / 2  # Poisson: varianza ≈ media
    delta = media_tratamiento - media_control
    n = 2 * (Z_ALFA_2 + z_beta) ** 2 * varianza / delta ** 2
    return ceil(n)


def efecto_detectable(n_por_grupo, media_control, potencia=POTENCIA):
    """Dado un n fijo, ¿qué diferencia relativa mínima se puede detectar?"""
    z_beta = Z_BETA[potencia]
    # Resolución iterativa simple: se busca el menor efecto detectable con ese n.
    efecto = 0.01
    while efecto < 10:
        media_tratamiento = media_control * (1 + efecto)
        if tamano_por_grupo(media_control, media_tratamiento, potencia) <= n_por_grupo:
            return efecto
        efecto += 0.01
    return None


if __name__ == "__main__":
    control = TASA_BASE_DIARIA * DIAS_DE_MEDICION
    tratamiento = control * (1 + MDE_RELATIVO)

    print("PARÁMETROS DEL DISEÑO")
    print(f"  Nivel de significancia (α):      {ALFA} (dos colas)")
    print(f"  Ventana de medición:             {DIAS_DE_MEDICION} días")
    print(f"  Tasa base supuesta:              {TASA_BASE_DIARIA} reportes/usuario/día")
    print(f"  Media esperada del control:      {control:.2f} reportes/usuario")
    print(f"  Media esperada del tratamiento:  {tratamiento:.2f} reportes/usuario")
    print(f"  Efecto mínimo detectable (MDE):  +{MDE_RELATIVO:.0%}")
    print()

    print("TAMAÑO DE MUESTRA REQUERIDO")
    for potencia in (0.80, 0.90, 0.95):
        n = tamano_por_grupo(control, tratamiento, potencia)
        print(f"  Potencia {potencia:.0%}:  {n:>3} usuarios por grupo  ->  {n * 2:>3} en total")
    print()

    print("SI LA MUESTRA DISPONIBLE ES MENOR (efecto mínimo que se podría detectar)")
    for n in (3, 5, 8, 12, 20):
        efecto = efecto_detectable(n, control)
        if efecto is None:
            print(f"  {n:>2} por grupo: ningún efecto razonable resulta detectable")
        else:
            print(f"  {n:>2} por grupo ({n * 2:>2} en total): solo efectos de +{efecto:.0%} o mayores")
