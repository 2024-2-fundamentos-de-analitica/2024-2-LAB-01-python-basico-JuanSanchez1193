"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    # Crear un diccionario donde la clave es el valor de la columna 2
    # y el valor es un conjunto de letras (sin repetir)
    valores_letras = {}

    # Abrir el archivo y procesarlo línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en columnas
            columnas = linea.strip().split('\t')
            
            # Obtener el valor de la columna 2 (convertirlo a entero)
            valor_columna_2 = int(columnas[1])  # Cambio aquí para tomar la columna 2
            # Obtener la letra de la columna 1
            letra_columna_1 = columnas[0]
            
            # Si el valor de la columna 2 ya existe en el diccionario,
            # agregar la letra a su conjunto
            if valor_columna_2 not in valores_letras:
                valores_letras[valor_columna_2] = set()
            valores_letras[valor_columna_2].add(letra_columna_1)

    # Convertir el diccionario en una lista de tuplas
    resultado = [(valor, sorted(list(letras))) for valor, letras in valores_letras.items()]

    # Ordenar la lista de tuplas por el valor de la columna 2 (el primer elemento de la tupla)
    resultado = sorted(resultado, key=lambda x: x[0])

    return resultado

# Llamar a la función para probar
print(pregunta_08())
