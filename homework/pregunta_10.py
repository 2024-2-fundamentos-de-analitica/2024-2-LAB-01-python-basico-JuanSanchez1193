"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas que contengan, por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    resultado = []

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas por tabulaciones
            columnas = linea.strip().split("\t")

            # Columna 1: Letra (primer valor de la línea)
            letra = columnas[0]

            # Columna 4: lista separada por comas
            columna_4 = columnas[3].split(",")  # Separar por comas para obtener la lista
            cantidad_columna_4 = len(columna_4)  # Número de elementos en la columna 4

            # Columna 5: diccionario con claves:valor, que se separan por comas
            columna_5 = columnas[4].split(",")  # Separar por comas
            cantidad_columna_5 = len(columna_5)  # Número de elementos en la columna 5

            # Añadir tupla (letra, cantidad de columna 4, cantidad de columna 5) a la lista
            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))

    return resultado

# Llamar a la función para probarla
print(pregunta_10())

