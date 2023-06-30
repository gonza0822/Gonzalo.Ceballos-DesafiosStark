from data_stark import lista_heroes
import os

#A
def heroes_masculinos(lista):
    contador = 0
    for heroes in lista:
        if(heroes["genero"] == "M"):
            contador += 1
            print(f'Los heroes de sexo masculino son {heroes["nombre"]}')
    if(contador == 0):
        print("No hay heroes masculinos")

#B

def heroes_femeninos(lista):
    contador = 0
    for heroes in lista:
        if(heroes["genero"] == "F"):
            contador += 1
            print(f'Los heroes de sexo femenino son {heroes["nombre"]}')
    if(contador == 0):
        print("No hay heroinas")

#C

def heroe_mas_alto_masculino(lista):
    contador = 0
    for heroes in lista:
        if(heroes["genero"] == "M"):
            contador += 1
            bandera_mas_altura =  False
            max_altura = 0
            for heroes in lista:
                if(float(max_altura) < float(heroes["altura"])) or (bandera_mas_altura == False):
                    bandera_mas_altura = True
                    max_altura = heroes["altura"]
                    heroe_mas_alto = heroes["nombre"]
    if(contador == 0):
        print("No hay heroes maculinos")
    else:
        print(f"El superheroe mas alto del genero masculino es: {heroe_mas_alto}")

#D
    
def heroe_mas_alto_femenino(lista):
    contador = 0
    for heroes in lista:
        if(heroes["genero"] == "F"):
            contador += 1
            bandera_mas_altura =  False
            max_altura = 0
            for heroes in lista:
                if(float(max_altura) < float(heroes["altura"])) or (bandera_mas_altura == False):
                    bandera_mas_altura = True
                    max_altura = heroes["altura"]
                    heroina_mas_alta = heroes["nombre"]
    if(contador == 0):
        print("No hay heroinas")
    else:
        print(f"El superheroe mas alto del genero femenino es: {heroina_mas_alta}")


#E

def heroe_mas_bajo_masculino(lista):
    contador = 0
    for heroes in lista:
        if(heroes["genero"] == "M"):
            contador += 1
            bandera_menos_altura =  False
            menos_altura = 0
            for heroes in lista:
                if(float(menos_altura) > float(heroes["altura"])) or (bandera_menos_altura == False):
                    bandera_menos_altura = True
                    menos_altura = heroes["altura"]
                    heroe_mas_bajo = heroes["nombre"]
    if(contador == 0):
        print("No hay heroes maculinos")
    else:
        print(f"El superheroe mas bajo del genero masculino es: {heroe_mas_bajo}")

#F

def heroe_mas_bajo_femenino(lista):
    contador = 0
    for heroes in lista:
        if(heroes["genero"] == "F"):
            contador += 1
            bandera_menos_altura =  False
            menos_altura = 0
            for heroes in lista:
                if(float(menos_altura) > float(heroes["altura"])) or (bandera_menos_altura == False):
                    bandera_menos_altura = True
                    menos_altura = heroes["altura"]
                    heroina_mas_baja = heroes["nombre"]
    if(contador == 0):
        print("No hay heroinas")
    else:
        print(f"El superheroe mas bajo del genero femenino es: {heroina_mas_baja}")

#G

def altura_promedio_heroes(lista):
    contador = 0
    acumulador_alturas = 0
    for heroes in lista:
        if(heroes["genero"] == "M"):
            contador += 1
            acumulador_alturas += float(heroes["altura"])
    if(contador == 0):
        print("No hay heroes masculinos")
    else:
        promedio_altura = acumulador_alturas / len(lista)
    print(f"La altura promedio de los heroes del genero masculino es {promedio_altura}")

#H

def altura_promedio_heroinas(lista):
    contador = 0
    acumulador_alturas = 0
    promedio_altura = 0
    for heroes in lista:
        if(heroes["genero"] == "F"):
            contador += 1
            acumulador_alturas += float(heroes["altura"])
    if(contador == 0):
        print("No hay heroinas")
    else:
        promedio_altura = acumulador_alturas / len(lista)
        print(f"La altura promedio de los heroes del genero femenino es {promedio_altura}")

#I

def informar_heroes():
    heroe_mas_alto_masculino(lista_heroes)
    heroe_mas_alto_femenino(lista_heroes)
    heroe_mas_bajo_masculino(lista_heroes)
    heroe_mas_bajo_femenino(lista_heroes)

#J

def heroes_color_ojos(lista):
    lista_color_ojos = set()
    lista_colores_heroes = []

    for heroes in lista:
        lista_color_ojos.add(heroes["color_ojos"])

    for colores in lista_color_ojos:
        contador = 0
        for heroes in lista:
            if(colores == heroes["color_ojos"]):
                contador+=1
        lista_color_heroe = [colores, contador]
        lista_colores_heroes.append(lista_color_heroe)

    for listas in lista_colores_heroes:
        print(f"El color de ojos {listas[0]} lo tienen {listas[1]} heroes")

#K

def heroes_color_pelo(lista):
    lista_color_pelo = set()
    lista_colores_heroes = []

    for heroes in lista:
        lista_color_pelo.add(heroes["color_pelo"])

    for colores in lista_color_pelo:
        contador = 0
        for heroes in lista:
            if(colores == heroes["color_pelo"]):
                contador+=1
        lista_color_heroe = [colores, contador]
        lista_colores_heroes.append(lista_color_heroe)

    for listas in lista_colores_heroes:
        print(f"El color de pelo {listas[0]} lo tienen {listas[1]} heroes")

#L

def heroes_inteligencia(lista):
    lista_inteligencias = set()
    lista_inteligencias_heroes = []

    for heroes in lista:
        try:
            lista_inteligencias.add(heroes["inteligencia"])
        except KeyError:
            lista_inteligencias.add("no tiene")
        print(lista_inteligencias)

    for inteligencias in lista_inteligencias:
        contador = 0
        for heroes in lista:
            try:
                if(inteligencias == heroes["inteligencia"]):
                    contador+=1
            except KeyError:
                if(inteligencias == "no tiene"):
                    contador += 1
        lista_inteligencia_heroe = [inteligencias, contador]
        lista_inteligencias_heroes.append(lista_inteligencia_heroe)

    for listas in lista_inteligencias_heroes:
        if(listas[0] == "no tiene"):
            print("no tiene inteligencia")
        else:
            print(f"La inteligencia {listas[0]} la tienen {listas[1]} heroes")

#M

def listar_color_ojos(lista):
    lista_color_ojos = set()
    lista_color_heroes = []

    for heroes in lista:
        lista_color_ojos.add(heroes["color_ojos"])

    for colores in lista_color_ojos:
        lista_heroes_por_color = [colores]
        for heroes in lista:
            if(colores == heroes["color_ojos"]):
                lista_heroes_por_color.append(heroes["nombre"])
        lista_color_heroes.append(lista_heroes_por_color)

    for listas in lista_color_heroes:
        print(listas)

#N

def listar_color_pelo(lista):
    lista_color_pelo = set()
    lista_color_heroes = []

    for heroes in lista:
        lista_color_pelo.add(heroes["color_pelo"])

    for colores in lista_color_pelo:
        lista_heroes_por_color = [colores]
        for heroes in lista:
            if(colores == heroes["color_pelo"]):
                lista_heroes_por_color.append(heroes["nombre"])
        lista_color_heroes.append(lista_heroes_por_color)

    for listas in lista_color_heroes:
        print(listas)

#O

def listar_inteligencia(lista):
    lista_inteligencias = set()
    lista_inteligencia_heroes = []

    for heroes in lista:
        try:
            lista_inteligencias.add(heroes["inteligencia"])
        except KeyError:
            lista_inteligencias.add("no tiene")

    for inteligencias in lista_inteligencias:
        lista_heroes_por_inteligencia = [inteligencias]
        for heroes in lista:
            try:
                if(inteligencias == heroes["inteligencia"]):
                    lista_heroes_por_inteligencia.append(heroes["nombre"])
            except KeyError:
                if(inteligencias == "no tiene"):
                    lista_heroes_por_inteligencia.append(heroes["nombre"])
        lista_inteligencia_heroes.append(lista_heroes_por_inteligencia)

    for listas in lista_inteligencia_heroes:
        print(listas)

while True:
        os.system("cls")
        print("""*** Menu de opciones ***
    --------------------------
    1- Recorrer la lista imprimiendo el nombre de cada superheroe masculino
    2- Recorrer la lista imprimiendo el nombre de cada superheroe femenino
    3- Recorrer la lista imprimiendo el superheroe masculino mas alto
    4- Recorrer la lista imprimiendo el superheroe femenino mas alto
    5- Recorrer la lista imprimiendo el superheroe masculino mas bajo
    6- Recorrer la lista imprimiendo el superheroe femenino mas bajo
    7- Recorrer la lista imprimiendo el promedio de la altura de los superheroes masculinos
    8- Recorrer la lista imprimiendo el promedio de la altura de los superheroes femeninos
    9- indicar nombre de las opciones 3 a 6 
    10- Cuantos superheroes tienen cada tipo de color de ojos
    11- Cuantos superheroes tienen cada tipo de color de pelo
    12- Cuantos superheroes tienen cada tipo de inteligencia
    13- Listar todos los superhereos por color de ojos
    14- Listar todos los superhereos por color de pelo
    15- Listar todos los superhereos por tipo de inteligencia
    16-Salir del programa""")
        opcion = input("Ingrese una opcion: ")
        while(not opcion.isdigit() or (float(opcion) < 1 or float(opcion) > 16)):
            opcion = input("No es una opcion valida, por favor ingrese otra: ")

        match(opcion):
            case "1":
                heroes_masculinos(lista_heroes)
            case "2":
                heroes_femeninos(lista_heroes)
            case "3":
                heroe_mas_alto_masculino(lista_heroes)
            case "4":
                heroe_mas_alto_femenino(lista_heroes)
            case "5":
                heroe_mas_bajo_masculino(lista_heroes)
            case "6":
                heroe_mas_bajo_femenino(lista_heroes)
            case "7":
                altura_promedio_heroes(lista_heroes)
            case "8":
                altura_promedio_heroinas(lista_heroes)
            case "9":
                informar_heroes()
            case "10":
                heroes_color_ojos(lista_heroes)
            case "11":
                heroes_color_pelo(lista_heroes)
            case "12":
                heroes_inteligencia(lista_heroes)
            case "13":
                listar_color_ojos(lista_heroes)
            case "14":
                listar_color_pelo(lista_heroes)
            case "15":
                listar_inteligencia(lista_heroes)
            case "16":
                print("saliste del programa")
                break

        os.system("pause")