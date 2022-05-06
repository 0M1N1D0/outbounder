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
# FIN

with open(r'C:\Users\miguel.alvarez\Desktop\Python\proyectos\proyecto outbounder\outbounder\archivos_csv\estados_csv.csv') as f: 
    reader = csv.reader(f)
    next(f) # skip the header
    for row in reader:
        # como row es una lista, se pasa el elemento a i para agregarlo normal y que no se agregue como lista
        i = row[0]
        cursor.execute(
            'INSERT INTO campanias_estado(nombre, fecha_creacion, fecha_modificacion) VALUES(%s, %s, %s)', (i, dt.now(), dt.now())
        )
    # # cursor.copy_from(f, 'campanias_estado', sep=',')


conexion.commit()