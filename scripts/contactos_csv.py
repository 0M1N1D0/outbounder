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

with open(r'C:\Users\miguel.alvarez\Desktop\Python\proyectos\proyecto outbounder\outbounder\archivos_csv\contactos_csv.csv') as f: 
    reader = csv.reader(f)
    next(f) # skip the header
   
    for row in reader:
        # como row es una lista, se pasa el elemento a i para agregarlo normal y que no se agregue como lista
        codigo_eo = row[0]
        nombres = row[1]
        apellido_paterno = row[2]
        apellido_materno = row[3]
        descuento = row[4]
        telefono = row[5]
        cursor.execute(
            'INSERT INTO campanias_contacto(codigo_eo, nombres, apellido_paterno, apellido_materno, descuento, fecha_creacion, fecha_modificacion, telefono) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', (codigo_eo, nombres, apellido_paterno, apellido_materno, descuento, dt.now(), dt.now(), telefono)
        )
    # # cursor.copy_from(f, 'campanias_estado', sep=',')


conexion.commit()