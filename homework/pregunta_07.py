"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    # Definir el archivo y leerlo
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
    
    # Inicializar un diccionario para almacenar las asociaciones
    associations = {}

    # Recorrer las líneas del archivo (ignorando la primera línea de encabezado)
    for line in lines:
        parts = line.strip().split("\t")  # Separar los campos por tabulador
        letter = parts[0]  # Columna 0 (letra)
        value = int(parts[1])  # Columna 1 (valor numérico)

        # Asociar las letras a su valor de la columna 2
        if value not in associations:
            associations[value] = []
        associations[value].append(letter)
    
    # Crear la lista de tuplas para la respuesta
    result = []
    for value in sorted(associations.keys()):  # Ordenar los valores
        result.append((value, associations[value]))

    return result

    
    
print(pregunta_07())