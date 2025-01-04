"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    # Inicializar un diccionario para acumular las sumas por letra
    suma_por_letra = {}

    # Abrir el archivo para procesarlo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas por tabulación
            columnas = linea.strip().split("\t")

            # Columna 2 tiene el valor numérico, convertirlo a entero
            valor_columna_2 = int(columnas[1])

            # Columna 4 tiene las letras separadas por coma
            letras_columna_4 = columnas[3].split(",")

            # Sumar el valor de la columna 2 para cada letra en la columna 4
            for letra in letras_columna_4:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_columna_2
                else:
                    suma_por_letra[letra] = valor_columna_2

    # Ordenar el diccionario por clave (alfabéticamente)
    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada

# Llamar a la función para probarla
print(pregunta_11())

