"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    # Inicializar un diccionario para almacenar las sumas
    suma_por_letra = {}

    # Abrir el archivo y procesarlo línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en columnas
            columnas = linea.strip().split('\t')
            
            # Obtener la letra de la primera columna y el valor de la segunda columna
            letra = columnas[0]
            try:
                valor = int(columnas[1])  # Convertir el valor de la segunda columna a entero
            except ValueError:
                continue  # Si no es un valor numérico, ignoramos esa línea

            # Sumar el valor a la letra correspondiente en el diccionario
            if letra in suma_por_letra:
                suma_por_letra[letra] += valor
            else:
                suma_por_letra[letra] = valor

    # Convertir el diccionario a una lista de tuplas y ordenarlo alfabéticamente
    resultado = sorted(suma_por_letra.items())

    return resultado

# Llamar a la función para probar
print(pregunta_03())


