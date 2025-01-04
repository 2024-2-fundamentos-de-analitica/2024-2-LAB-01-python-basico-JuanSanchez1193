"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    # Inicializar un diccionario para contar los registros por mes
    contador_meses = {str(i).zfill(2): 0 for i in range(1, 13)}  # Crear claves '01', '02', ..., '12'

    # Abrir el archivo y procesarlo línea por línea
    with open('files/input/data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en columnas
            columnas = linea.strip().split('\t')
            
            # Obtener la fecha de la tercera columna
            fecha = columnas[2]
            
            # Extraer el mes de la fecha (formato YYYY-MM-DD, el mes está en la posición 5-6)
            mes = fecha[5:7]
            
            # Incrementar el contador del mes correspondiente
            if mes in contador_meses:
                contador_meses[mes] += 1

    # Convertir el diccionario a una lista de tuplas y ordenarlo
    resultado = sorted(contador_meses.items())

    return resultado

# Llamar a la función para probar
print(pregunta_04())

