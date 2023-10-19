import sqlite3
import csv

conexion = sqlite3.connect("intento1") # Crear la db
cursor = conexion.cursor() # Funciona para ejecutar sentencias sql
archivos = ['Grupoi','Grupoii','Grupoiii','Grupoiv','Grupov' ,'Grupovi', 'Grupovii', 'Grupoviii', 'Grupoix', 'Grupox']
listas = []

#cursor.execute("""CREATE TABLE caninos(
#               nombre TEXT,
#               origen TEXT,
#               clasificacion TEXT,
#               caracteristicas TEXT,
#               tamaño TEXT,
#               altura TEXT,
#               peso TEXT,
#               vida TEXT,
#               actividad TEXT,
#               caracter TEXT,
#               ideal TEXT,
#               recomendaciones TEXT,
#               clima TEXT,
#               pelo TEXT,
#               adiestramiento TEXT)
#                    """)

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
            lista_filas.append(fila)

    listas.append(lista_filas)


#for lista1 in listas:
#    for lista2 in lista1:
#        cursor.execute("INSERT INTO caninos(nombre, origen, clasificacion, caracteristicas, tamaño, altura, peso, vida, actividad, caracter, ideal, recomendaciones, clima, pelo, adiestramiento) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", lista2)

print("Datos agregados con exito")
conexion.commit() # Confirmar los cambios en la tabla
conexion.close()