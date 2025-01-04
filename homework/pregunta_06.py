"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del carácter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    # Inicializar un diccionario para almacenar los valores mínimo y máximo por cada clave
    claves_valores = {}

    # Abrir el archivo y procesarlo línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en columnas
            columnas = linea.strip().split('\t')
            
            # Obtener el diccionario codificado de la quinta columna
            diccionario_str = columnas[4]
            
            # Dividir las claves y valores del diccionario codificado
            elementos = diccionario_str.split(',')
            
            for item in elementos:
                clave, valor = item.split(':')
                valor = int(valor)  # Convertir el valor a entero
                
                # Si la clave ya está en el diccionario, actualizar el valor mínimo y máximo
                if clave in claves_valores:
                    claves_valores[clave][0] = min(claves_valores[clave][0], valor)
                    claves_valores[clave][1] = max(claves_valores[clave][1], valor)
                else:
                    claves_valores[clave] = [valor, valor]

    # Convertir el diccionario a una lista de tuplas y ordenarla
    resultado = [(clave, valores[0], valores[1]) for clave, valores in claves_valores.items()]
    resultado = sorted(resultado)

    return resultado

# Llamar a la función para probar
print(pregunta_06())

