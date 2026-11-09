#!/usr/bin/env python3
"""
paridad.py — TP7 Redes de Computadoras.

Lee un archivo de texto con unos y ceros (una fila por línea) y muestra la
matriz con la paridad par de cada fila (a la derecha) y de cada columna (abajo).

Modificación (Consigna 7): si además se le pasan los bits de control recibidos
(campo CHECK), compara las paridades calculadas con las recibidas e indica qué
filas y qué columnas fallan.

Uso:
    python paridad.py                         # lee mensaje.txt
    python paridad.py otro_archivo.txt
    python paridad.py otro_archivo.txt CHECK  # además compara con CHECK
"""
import sys

ruta = sys.argv[1] if len(sys.argv) > 1 else "mensaje.txt"
check = sys.argv[2] if len(sys.argv) > 2 else None  # agregado

with open(ruta, encoding="utf-8") as f:
    filas = [linea.strip() for linea in f if linea.strip()]

for fila in filas:
    print(fila, "|" + str(fila.count("1") % 2))
print("-" * (len(filas[0]) + 2))
print("".join(str(sum(fila[j] == "1" for fila in filas) % 2) for j in range(len(filas[0]))))

# --- Agregado: comparación con los bits de control recibidos ---
if check:
    n = len(filas)
    paridad_filas = "".join(str(fila.count("1") % 2) for fila in filas)
    paridad_columnas = "".join(str(sum(fila[j] == "1" for fila in filas) % 2) for j in range(len(filas[0])))

    # En CHECK vienen primero los bits de las filas y luego los de las columnas
    check_filas = check[:n]
    check_columnas = check[n:]

    filas_mal = [i for i in range(n) if paridad_filas[i] != check_filas[i]]
    columnas_mal = [j for j in range(len(paridad_columnas)) if paridad_columnas[j] != check_columnas[j]]

    print()
    print("Filas que fallan:   ", filas_mal)
    print("Columnas que fallan:", columnas_mal)
