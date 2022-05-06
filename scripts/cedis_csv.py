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

with open(r'C:\Users\miguel.alvarez\Desktop\Python\proyectos\proyecto outbounder\outbounder\archivos_csv\cedis_csv.csv') as f: 
    reader = csv.reader(f)
    next(f) # skip the header
    # cursor.execute(
    #     #se asigna la columna estado_id como clave foránea
    #     ''' ALTER TABLE campanias_cedi
    #         ADD CONSTRAINT cons_cedi   
    #         FOREIGN KEY (estado_id)
    #         REFERENCES campanias_estado (nombre)
    #     '''         
    # )
    for row in reader:
        # como row es una lista, se pasa el elemento a i para agregarlo normal y que no se agregue como lista
        nombre = row[0]
        estado = row[1]
        cursor.execute(
            'INSERT INTO campanias_cedi(nombre, fecha_creacion, fecha_modificacion, estado_id) VALUES(%s, %s, %s, %s)', (nombre, dt.now(), dt.now(), estado)
        )
    # # cursor.copy_from(f, 'campanias_estado', sep=',')


conexion.commit()