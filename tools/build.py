#!/usr/bin/env python3
"""Herramientas del informe: índice automático y compilación a un solo archivo.

    python tools/build.py toc   -> regenera la tabla de contenidos dentro del README
    python tools/build.py       -> arma informe-completo.md (README + capítulos)

El informe se escribe en varios archivos para que sea manejable, pero la entrega es un
único PDF. Este script une todo en el orden correcto justo antes de exportar, así no hay
que mantener a mano ni el índice ni el documento final.
"""
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAPITULOS = [
    "capitulo-01-introduccion.md",
    "capitulo-02-requirements-elicitation.md",
    "capitulo-03-requirements-specification.md",
    "capitulo-04-product-design.md",
    "capitulo-05-product-implementation.md",
    "capitulo-06-verification-validation.md",
    "capitulo-07-devops-practices.md",
    "capitulo-08-experiment-driven.md",
    "conclusiones.md",
    "bibliografia.md",
    "anexos.md",
]

INICIO = "<!-- TOC:inicio -->"
FIN = "<!-- TOC:fin -->"


def ancla(titulo: str) -> str:
    """Reproduce el identificador que GitHub genera para un encabezado."""
    texto = titulo.strip().lower()
    texto = texto.replace(" ", "-")
    # GitHub conserva letras (incluidas acentuadas), números, guiones y guiones bajos.
    permitidos = []
    for caracter in texto:
        if caracter in "-_" or caracter.isalnum():
            permitidos.append(caracter)
    return "".join(permitidos)


def encabezados(ruta: Path):
    """Devuelve (nivel, título) de cada encabezado, ignorando los bloques de código."""
    en_codigo = False
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        coincidencia = re.match(r"^(#{1,4})\s+(.*)$", linea)
        if coincidencia:
            yield len(coincidencia.group(1)), coincidencia.group(2).strip()


def construir_toc() -> str:
    lineas = []
    for nombre in CAPITULOS:
        ruta = RAIZ / "chapters" / nombre
        if not ruta.exists():
            continue
        for nivel, titulo in encabezados(ruta):
            sangria = "  " * (nivel - 1)
            limpio = re.sub(r"[*`]", "", titulo)
            lineas.append(f"{sangria}- [{limpio}](chapters/{nombre}#{ancla(titulo)})")
    return "\n".join(lineas)


def escribir_toc() -> None:
    readme = RAIZ / "README.md"
    texto = readme.read_text(encoding="utf-8")
    if INICIO not in texto or FIN not in texto:
        sys.exit("No encuentro las marcas del índice en el README.")
    antes = texto.split(INICIO)[0]
    despues = texto.split(FIN)[1]
    readme.write_text(
        f"{antes}{INICIO}\n\n{construir_toc()}\n\n{FIN}{despues}",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Índice actualizado: {len(construir_toc().splitlines())} entradas.")


def compilar() -> None:
    partes = [(RAIZ / "README.md").read_text(encoding="utf-8")]
    for nombre in CAPITULOS:
        ruta = RAIZ / "chapters" / nombre
        if not ruta.exists():
            print(f"  aviso: falta {nombre}")
            continue
        # Salto de página para la exportación a PDF: cada capítulo empieza en página nueva.
        partes.append('\n<div style="page-break-after: always;"></div>\n')
        partes.append(ruta.read_text(encoding="utf-8"))

    salida = RAIZ / "informe-completo.md"
    salida.write_text("\n".join(partes), encoding="utf-8", newline="\n")

    contenido = salida.read_text(encoding="utf-8")
    pendientes = contenido.count("**PENDIENTE.**")
    completar = contenido.count("COMPLETAR")
    print(f"informe-completo.md generado: {len(contenido.splitlines())} líneas.")
    print(f"  secciones pendientes: {pendientes}")
    print(f"  marcas COMPLETAR:     {completar}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "toc":
        escribir_toc()
    else:
        escribir_toc()
        compilar()
