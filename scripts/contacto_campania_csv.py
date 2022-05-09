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

with open(r'C:\Users\miguel.alvarez\Desktop\Python\proyectos\proyecto outbounder\outbounder\archivos_csv\contactos_campania_csv.csv') as f: 
    reader = csv.reader(f)
    next(f) # skip the header
    # TODO: revisar si sólo se hace una vez: 

    # cursor.execute(
    #     #se asigna la columna estado_id como clave foránea
    #     ''' ALTER TABLE campanias_contacto_campania
    #         ADD PRIMARY KEY (id)   
    #     '''         
    # )

    for row in reader:
        # como row es una lista, se pasa el elemento a i para agregarlo normal y que no se agregue como lista
        contacto_id = row[0]
        campania_id = row[1]

        # la PK se autocompleta
        cursor.execute(
            'INSERT INTO campanias_contacto_campania(contacto_id, campania_id) VALUES(%s, %s)', (contacto_id, campania_id)
        )
    


conexion.commit()