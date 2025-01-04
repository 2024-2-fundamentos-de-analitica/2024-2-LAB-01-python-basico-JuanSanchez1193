"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    # Inicializar un diccionario para contar las apariciones
    contador = {}

    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en columnas y tomar la primera columna
            letra = linea.strip().split('\t')[0]
            # Incrementar el contador para la letra
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(contador.items())

    return resultado

# Llamar a la función para probar
print(pregunta_02())

                    

                

                    

