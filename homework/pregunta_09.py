"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5, ordenado alfabéticamente.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    # Inicializar el diccionario para contar las ocurrencias de cada clave
    contador_claves = {}

    # Abrir el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas por tabulaciones
            columnas = linea.strip().split("\t")

            # La columna 5 contiene un diccionario de claves:valor
            columna_5 = columnas[4]  # La columna 5 está en el índice 4

            # Se separan las claves y valores por comas
            claves_valores = columna_5.split(",")

            # Recorrer cada elemento en la columna 5
            for clave_valor in claves_valores:
                # Se toma solo la clave antes del ":"
                clave = clave_valor.split(":")[0]

                # Contar las veces que aparece cada clave
                if clave in contador_claves:
                    contador_claves[clave] += 1
                else:
                    contador_claves[clave] = 1

    # Ordenar el diccionario por clave alfabéticamente
    contador_claves_ordenado = dict(sorted(contador_claves.items()))

    return contador_claves_ordenado

# Llamar a la función para probarla
print(pregunta_09())
