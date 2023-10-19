"""
Caracteristicas claves: tamaño, actividad, caracter, clima
Preguntas claves:
    Tamaño: ¿Prefieres perros pequeños, medianos o grandes?

    Actividad fisica: ¿Qué tan activo eres como persona?, ¿Cuánto tiempo puedes dedicar al ejercicio diario del perro?, ¿Te gustaría un perro que sea activo y juguetón o más tranquilo?

    Caracter:  ¿Prefieres perros que sean más independientes o aquellos que son más afectuosos y buscan compañía?, ¿Tienes niños en casa? En ese caso, ¿buscas un perro amigable con los niños?
    
    Clima recomendado: ¿Vives en un área con un clima cálido o frío?, ¿Estás dispuesto a cuidar el pelaje de un perro que pueda ser sensible a ciertos climas?
"""

def obtener_tamaño_perro():
    puntaje = 0
    respuesta = input("¿Prefieres perros pequeños, medianos o grandes?: ")

    if respuesta == "pequeños":
        puntaje = 0
    elif respuesta == "medianos":
        puntaje = 1
    elif respuesta == "grandes":
        puntaje = 3

    return puntaje

def obtener_actividad_fisica():
    sumatoria = 0
    pregunta1 = input("¿Qué tan activo eres como persona? (poco, normal, mucho): ")
    pregunta2 = input("¿Cuánto tiempo puedes dedicar al ejercicio diario del perro? [(15 - 30 min), (40 - 60 min), (70 - 120 min)]: ")
    pregunta3 = input("¿Te gustaría un perro que sea activo y juguetón o más tranquilo?: ")

    if pregunta1 == "poco":
        sumatoria += 0
    elif pregunta1 == "normal":
        sumatoria += 1
    elif pregunta1 == "mucho":
        sumatoria += 2


    if pregunta2 == "15 - 30 min":
        sumatoria += 0
    elif pregunta2 == "40 - 60 min":
        sumatoria += 1
    elif pregunta2 == "70 - 120 min":
        sumatoria += 2

    if pregunta3 == "tranquilo":
        sumatoria += 0
    elif pregunta3 == "jugueton":
        sumatoria += 2

    sumatoria = (sumatoria) / 3

    return sumatoria

def obtener_caracter():
    sumatoria = 0
    pregunta1 = input("¿Prefieres perros que sean más independientes o aquellos que son más afectuosos y buscan compañía?: ")
    pregunta2 = input("¿Tienes niños en casa?: ")
    

    if pregunta1 == "independientes":
        sumatoria += 0
    elif pregunta1 == "afectuosos":
        sumatoria += 1

    if pregunta2 == "no":
        sumatoria += 0
    elif pregunta2 == "si":
        pregunta3 = input("¿Buscas un perro amigable con los niños?: ")
        if pregunta2 == "no":
            sumatoria += 0
        elif pregunta2 == "si":
            sumatoria += 1

    sumatoria = (sumatoria) / 3
    return sumatoria

def obtener_clima():
    sumatoria = 0
    pregunta1 = input("¿Vives en un área con un clima cálido, frío o templado?: ")
    pregunta2 = input("¿Estás dispuesto a cuidar el pelaje de un perro que pueda ser sensible a ciertos climas?: ")

    if pregunta1 == "calido":
        sumatoria += 0
    elif pregunta1 == "templado":
        sumatoria += 1
    elif pregunta1 == "frio":
        sumatoria += 2


    if pregunta2 == "no":
        sumatoria += 0
    elif pregunta2 == "si":
        sumatoria += 1    

    sumatoria = (sumatoria) / 3

    return sumatoria

def calcular_similitud():

    puntaje_tamaño = obtener_tamaño_perro()
    puntaje_actividad = obtener_actividad_fisica()
    puntaje_caracter = obtener_caracter()
    puntaje_clima = obtener_clima()
    puntajeTotal = (puntaje_tamaño + puntaje_actividad + puntaje_caracter + puntaje_clima) / 4
    return puntajeTotal 
    

print(calcular_similitud())

