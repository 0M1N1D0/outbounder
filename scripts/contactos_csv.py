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

# #####################
# EJEMPLO
# #####################
# cursor.execute(
#     'SELECT * FROM campanias_cedi'
# )

# one = cursor.fetchone()
# print(one)
# #####################

with open(r'C:\Users\miguel.alvarez\Desktop\Python\proyectos\proyecto outbounder\outbounder\archivos_csv\contactos_csv.csv') as f: 
    reader = csv.reader(f)
    next(f) # skip the header
   
    for row in reader:
        # como row es una lista, se pasa el elemento a i para agregarlo normal y que no se agregue como lista
        codigo_eo = row[0]
        nombre = row[1]
        descuento = row[2]
        tel_casa = row[3]
        celular = row[4]
        pais = row[5]
        estado = row[6]
        centro_alta = row[7]
        email = row[8]
        fecha_ultima_compra = row[9]
        meses_sin_compra = row[10]
        fecha_alta = row[11]
        sexo = row[12]
        fecha_nacimiento = row[13]
        total_puntos = row[14]
        campania = row[15]
        cedis = row[16]

        cursor.execute(
            'INSERT INTO campanias_contacto(num_dist, nombre, descuento_choice, fecha_creacion, tel_casa, tel_cel, pais, estado, centro_alta, email, fecha_ultima_compra, meses_sin_compra, fecha_alta, sexo, fecha_nacimiento, total_puntos, campania_id, cedis_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (codigo_eo, nombre, descuento, dt.now(), tel_casa, celular, pais, estado, centro_alta, email, fecha_ultima_compra, meses_sin_compra, fecha_alta, sexo, fecha_nacimiento, total_puntos, campania, cedis)
        )
    # # cursor.copy_from(f, 'campanias_estado', sep=',')


conexion.commit()