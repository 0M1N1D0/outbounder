import csv
import psycopg2
from datetime import datetime as dt

# estableciendo conexión
conexion = psycopg2.connect(
    database='outbounderDB',
    user="mike",
    password='2010',
    host='localhost',
    port='5432'
)

conexion.autocommit = True
# creando cursor 
cursor = conexion.cursor()

# PRUEBA: 
# cursor.execute(
#     'SELECT * FROM campanias_cedi'
# )

# one = cursor.fetchone()
# print(one)
# FIN PRUEBA

with open(r'C:\Users\miguel.alvarez\Desktop\Python\proyectos\proyecto outbounder\outbounder\archivos_csv\paises_csv.csv') as f: 
    reader = csv.reader(f)
    next(f) # skip the header
    for row in reader:
        # como row es una lista, se pasa el elemento a i para agregarlo normal y que no se agregue como lista
        i = row[0]
        cursor.execute(
            # no importa el orden
            'INSERT INTO campanias_pais(fecha_creacion, fecha_modificacion, nombre) VALUES(%s, %s, %s)', (dt.now(), dt.now(), i)
        )
    # # cursor.copy_from(f, 'campanias_estado', sep=',')


conexion.commit()