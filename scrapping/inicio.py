from bs4 import BeautifulSoup
import requests

pagina = 'https://www.expertoanimal.com/razas-de-perros/chodsky-o-pastor-bohemio.html'
resultado = requests.get(pagina)
contenido = resultado.text

lista = ['prop-ig','prop-ig prop-ig--', 'prop-ig prop-ig--col']
lista2 = ['prop-ig prop-ig--sel prop-ig--perro-size','prop-ig prop-ig--sel prop-ig--perro-altura','prop-ig prop-ig--sel prop-ig--perro-peso','prop-ig prop-ig--sel prop-ig--perro-vida','prop-ig prop-ig--sel prop-ig--generic-3']

caracteristicas = {"Origen": "", "clasificacion FCI": "", "caracteristicas fisicas": ""}
caracteristicas2 = {"tamaño": "", "altura": "", "peso adulto": "", "esperanza de vida": "", "actividad fisica recomendada": ""}

temporal = []
temporal2 = []
temporal3 = []
contador = 0

soup = BeautifulSoup(contenido, 'lxml')

for x in lista2:
    elemento_clase = soup.find(class_=f'{x}')
    elementos_li = elemento_clase.find_all('li')
    numero_elemento_selected = 0


    for index, elemento in enumerate(elementos_li):
        if 'selected' in elemento['class']:
            indice_elemento_seleccionado = index
            break  # Salir del bucle una vez que se encuentre el índice

    temporal2.append(indice_elemento_seleccionado)



for box in lista2:
    caja = soup.find('div', class_=f'{box}')
    titulo = caja.getText()
    temporal.append(titulo)

lista_modificada = [elemento.replace('\n', ' ').strip() for elemento in temporal]
lista_modificada = [cadena.split() for cadena in lista_modificada]
lista3 = []

contador = 0
for fila in lista_modificada:
    
    lista3.append(fila.pop(temporal2[contador]))
    contador+=1

contador = 0   

for caracteristica in caracteristicas2:
    caracteristicas2[caracteristica] = lista3[contador]
    contador +=1


contador = 0    

for box in lista:
    caja = soup.find('div', class_=f'{box}')
    titulo = caja.getText()
    temporal.append(titulo)

lista_modificada = [elemento.replace('\n', ' ').strip() for elemento in temporal]

for caracteristica in caracteristicas:
    caracteristicas[caracteristica] = lista_modificada[contador]
    contador+=1


print(caracteristicas)
print(caracteristicas2)