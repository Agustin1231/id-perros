import sqlite3
import csv
from math import ceil

conexion = sqlite3.connect("intento1")  # Crear la db
cursor = conexion.cursor()  # Funciona para ejecutar sentencias sql
archivos = ['Grupoi', 'Grupoii', 'Grupoiii', 'Grupoiv', 'Grupov', 'Grupovi', 'Grupovii', 'Grupoviii', 'Grupoix', 'Grupox']
listas = []

cursor.execute("""CREATE TABLE caninos(
               nombre TEXT,
               origen TEXT,
               clasificacion TEXT,
               caracteristicas TEXT,
               tamaño TEXT,
               altura TEXT,
               peso TEXT,
               vida TEXT,
               actividad TEXT,
               caracter TEXT,
               ideal TEXT,
               recomendaciones TEXT,
               clima TEXT,
               pelo TEXT,
               adiestramiento TEXT,
               puntaje INTEGER)""")

for archivo in archivos:
    # Abre el archivo CSV en modo lectura
    with open(f'{archivo}.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        # Inicializa una lista para almacenar las filas del archivo CSV
        lista_filas = []

        # Salta la primera fila (encabezado)
        next(lector_csv, None)

        # Itera a través de las filas del archivo CSV y las almacena como sublistas
        for fila in lector_csv:
            # Lógica para asignar puntaje
            puntaje = 0
            if fila[4].lower() == 'toy' or fila[4].lower() == 'pequeño':
                puntaje += 0
            elif fila[4].lower() == 'mediano':
                puntaje += 1
            elif fila[4].lower() == 'grande' or fila[4].lower() == 'Gigante':
                puntaje += 2



            if fila[8].lower() == 'baja':
                puntaje += 0
            elif fila[8].lower() == 'media':
                puntaje += 1
            elif fila[8].lower() == 'alta':
                puntaje += 2

            if 'Tranquilo' in fila[9] or 'Dominante' in fila[9] or 'Activo' in fila[9]:
                puntaje += 1
            elif 'Cariñoso' in fila[9] or 'Sociable' in fila[9]:
                puntaje += 2

            if fila[12].lower() == 'caluroso':
                puntaje += 0
            elif fila[12].lower() == 'temperado':
                puntaje += 1
            elif fila[12].lower() == 'frío':
                puntaje += 2


            # Agregar la columna 'puntaje' con el valor redondeado
            fila.append((puntaje / 4))  # Dividir por 4 y redondear

            lista_filas.append(fila)

    listas.append(lista_filas)

for lista1 in listas:
    for lista2 in lista1:
        cursor.execute(
            "INSERT INTO caninos(nombre, origen, clasificacion, caracteristicas, tamaño, altura, peso, vida, actividad, caracter, ideal, recomendaciones, clima, pelo, adiestramiento, puntaje) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            lista2)

print("Datos agregados con éxito")
conexion.commit()  # Confirmar los cambios en la tabla
conexion.close()
