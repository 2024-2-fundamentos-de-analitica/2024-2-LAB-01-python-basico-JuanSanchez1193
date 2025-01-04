"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    # Inicializar un diccionario para acumular las sumas
    suma_por_letra = {}

    # Abrir el archivo para procesarlo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas por tabulación
            columnas = linea.strip().split("\t")

            # Columna 1 es la letra
            letra_columna_1 = columnas[0]

            # Columna 5 contiene el diccionario, separar por comas y procesar cada clave-valor
            diccionario_columna_5 = columnas[4].split(",")
            
            # Sumar los valores de columna 5
            suma_columna_5 = 0
            for item in diccionario_columna_5:
                clave, valor = item.split(":")
                suma_columna_5 += int(valor)  # Sumar el valor de la clave

            # Acumular la suma por letra en el diccionario
            if letra_columna_1 in suma_por_letra:
                suma_por_letra[letra_columna_1] += suma_columna_5
            else:
                suma_por_letra[letra_columna_1] = suma_columna_5

    return suma_por_letra

# Llamar a la función para probarla
print(pregunta_12())

