# Importar las librerias para Scraping
from bs4 import BeautifulSoup
import requests
import csv

# Importar las librerias para poder obtener la URL de cada pagina
import re
from unidecode import unidecode 

grupos = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

for a in grupos:
    # Importamos el codigo HTML del primer grupo FCI
    pagina_principal = requests.get(f'https://www.expertoanimal.com/razas-de-perros/fci/grupo-{a}.html')
    contenido_pagina = pagina_principal.text
    soup = BeautifulSoup(contenido_pagina, 'lxml')

    lista_paginas = [] # Lista donde se guardara cada url de la pagina
    titulos = soup.find_all('a', class_='titulo titulo--resultado') # Buscamos el nombre de cada animal en la pagina principal
    lista_resultados = [] # Lista vacia donde se guardan los resultados de todas las paginas

    # Buscaremos cada nombre de los perros
    for titulo in titulos:
        texto = titulo.get_text()
        texto_formateado = re.sub(r'\W+', '-', texto)  # Dividir por caracteres no alfanuméricos
        texto_formateado = texto_formateado.rstrip('-') # Reemplazar espacios por guiones en cada parte
        texto_lower = unidecode(texto_formateado.lower()) # Colocamos los nombres sin ningun caracter extraño y lo volvemos minusculas
        lista_paginas.append(f"https://www.expertoanimal.com/razas-de-perros/{texto_lower}.html")
        # Cada url consta de la siguiente sintaxis https://www.expertoanimal.com/razas-de-perros/el-nombre-del-animal-separado-por"-".html
        # Por eso se coloca el titulo y se agrega a la lista de las url

    # En este bucle iremos a cada una de las sub-paginas en la lista del grupo 1
    for url in lista_paginas:
        print(url) # Mostramos la url de la pagina analizada en caso de algun error saber cual pagina es

        # Obtenemos la informacion de la pagina
        contenido = requests.get(f'{url}')
        contenido_pagina = contenido.text
        soup = BeautifulSoup(contenido_pagina, 'lxml')

        title = soup.find('h1', class_='titulo titulo--articulo').get_text() # Buscamos el titulo de cada animal
        temp = [] # Variables temporales para guardar informacion
        temp2 = [] # Variables temporales para guardar informacion
        contador = 0
        contador2 = 0
        contador4 = 0

        caracteristicas = {} # Creamos un diccionario donde tendremos el nombre y la caracteristica
        caracteristicasFinales = {"nombre":"", "Origen":"", "Clasificación FCI":"", "Características físicas":"", "Tamaño":"", "Altura":"", "Peso adulto":"", "Esperanza de vida":"" , "Actividad física recomendada":"", "Carácter":"", "Ideal para":"", "Recomendaciones":"", "Clima recomendado":"", "Tipo de pelo":"", "Nivel de adiestramiento":""}
        nombres_caracteristicas = soup.find_all(class_='titulo titulo--infografia') # Buscamos todos los titulos en el html
        caracteristicas_repetidas = soup.find_all(class_='prop-ig prop-ig--col') # Buscamos todas las caracteristicas repetidas
        divs_elemento = soup.select('.elemento.el--generic div') # Seleccionar todos los elementos <div> dentro de la estructura <div class="elemento el--generic">

        # Obtener las clases de los elementos seleccionados
        for div in divs_elemento:
            clases = div.get('class')
            temp.append(clases)

        # En el primer temporal guardaremos una lista de las caracteristicas del perro dependiendo de su titulo
        temp = [sublista for sublista in temp if not ("titulo" in sublista or "titulo--infografia" in sublista)]
        temp = [' '.join(sublista) for sublista in temp]

        for nombre in nombres_caracteristicas: # Iteramos en cada uno de los titulos
            caracteristicas[nombre.text.strip()] = temp[contador] # para cada caracteristicas guardamos el valor en el temporal
            contador += 1

        contador = 0
        
        for x in caracteristicas.values():
            elemento_clase = soup.find(class_=f'{x}')
            if elemento_clase:
                elementos_li = elemento_clase.find_all('li')
                indice_elemento_seleccionado = None  # Inicializar como None

                for index, elemento in enumerate(elementos_li):
                    if 'selected' in elemento.get('class', []):  # Utilizar el método get para obtener la lista de clases
                        indice_elemento_seleccionado = index
                        break  # Salir del bucle una vez que se encuentre el índice

                if indice_elemento_seleccionado is not None:
                    temp2.append(indice_elemento_seleccionado)

        for nombre in caracteristicas:
            clase_lista = caracteristicas[nombre]

            if clase_lista in ["prop-ig prop-ig--sel prop-ig--perro-size", "prop-ig prop-ig--sel prop-ig--perro-altura", "prop-ig prop-ig--sel prop-ig--perro-peso", "prop-ig prop-ig--sel prop-ig--perro-vida", "prop-ig prop-ig--sel prop-ig--generic-3"]:
                texto_caracteristicas = soup.find(class_= f'{clase_lista}')
                valor = texto_caracteristicas.text.strip()
                valores_lista = valor.split('\n')  # Dividir el valor por '\n'
                caracteristicas[nombre] = valores_lista.pop(temp2[contador])  # Asegúrate de definir temp2 y contador
                contador += 1
            
            elif clase_lista == "prop-ig prop-ig--carts":
                nombre_listas = soup.find_all(class_= clase_lista)
                lista3 = []
                contador3 = 0
                nombreClima = nombre_listas[0]

                if len(nombre_listas) > 1:
                    nombreAdiestramiento = nombre_listas[1]
                    if contador4 == 0:
                        # Encontrar el elemento li con la clase "selected"
                        opcion_seleccionada = nombreClima.find('li', class_='selected')
                        texto_opcion = opcion_seleccionada.text.strip()
                        lista3.append(texto_opcion)
                        caracteristicas[nombre] = lista3[contador3]  # Asegúrate de definir contador2
                        contador3 += 1
                        contador4 +=1
                    else:
                        opcion_seleccionada = nombreAdiestramiento.find('li', class_='selected')
                        texto_opcion = opcion_seleccionada.text.strip()
                        lista3.append(texto_opcion)
                        caracteristicas[nombre] = lista3[contador3]  # Asegúrate de definir contador2
                        contador3 += 1

                else:
                    opcion_seleccionada = nombreClima.find('li', class_='selected')
                    texto_opcion = opcion_seleccionada.text.strip()
                    lista3.append(texto_opcion)
                    caracteristicas[nombre] = lista3[contador3]  # Asegúrate de definir contador2
                    contador3 += 1
                
        
            elif clase_lista == "prop-ig prop-ig--col":
                nombre_listas = soup.find_all(class_=clase_lista)
                lista2 = []
                for nombre2 in nombre_listas:
                    lista2.append(nombre2.text.replace('\n', ' ').strip())
                caracteristicas[nombre] = lista2[contador2]  # Asegúrate de definir contador2
                contador2 += 1

            else:
                texto_caracteristicas = soup.find(class_= f'{clase_lista}')
                caracteristicas[nombre] = texto_caracteristicas.text.strip()


        # Este for solamente se encarga de arreglar el texto para que sea legible
        for clave, valor in caracteristicas.items():
            caracteristicas[clave] = valor.replace('\n', ' ')

        nombre_animal = {'nombre': title}
        caracteristicas= {**nombre_animal, **caracteristicas}

        for clave in caracteristicas:
                if clave in caracteristicasFinales and caracteristicas[clave] != caracteristicasFinales[clave]:
                    caracteristicasFinales[clave] = caracteristicas[clave]
                else:
                    pass

        listatemp = []
        for valor in caracteristicasFinales.values():
            listatemp.append(valor)

        lista_resultados.append(listatemp)



    encabezados = [
        "nombre", "origen", "clasificacion", "caracteristicas fisicas", 
        "tamaño", "altura", "peso adulto", "esperanza vida", "actividad fisica",
        "caracter", "ideal para", "recomendaciones","clima recomendado", "tipo de pelo", "nivel de adiestramiento"
    ]


    nombre_archivo = (f"Grupo{a}.csv")

    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        # Escribir la primera fila con los encabezados
        writer.writerow(encabezados)
        writer.writerows(lista_resultados)

    print(f"Archivo '{nombre_archivo}' creado exitosamente.")
