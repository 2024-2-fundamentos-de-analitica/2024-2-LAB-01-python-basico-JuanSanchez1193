"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    # Inicializar un diccionario para almacenar los valores de la segunda columna
    # para cada letra de la primera columna
    valores_por_letra = {}

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

            # Si la letra ya está en el diccionario, actualizar los valores máximos y mínimos
            if letra in valores_por_letra:
                valores_por_letra[letra].append(valor)
            else:
                valores_por_letra[letra] = [valor]

    # Crear la lista de tuplas con el valor máximo y mínimo para cada letra
    resultado = [(letra, max(valores), min(valores)) for letra, valores in valores_por_letra.items()]

    # Ordenar la lista de tuplas alfabéticamente por la letra
    resultado = sorted(resultado)

    return resultado

# Llamar a la función para probar
print(pregunta_05())

