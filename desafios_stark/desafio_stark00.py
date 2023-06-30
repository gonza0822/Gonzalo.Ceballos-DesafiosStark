from data_stark import lista_heroes
import os

#A

#B

def nombre_heroes(lista):
    for hereos in lista:
        print("nombre: "+ hereos["nombre"])
    print("------------------------")

#C

def nombre_altura_heroes(lista):
    for hereos in lista_heroes:
        print(f'nombre: {hereos["nombre"]}, altura: {hereos["altura"]}')
    print("-------------------------")

#D 
def heroe_mas_alto(lista):
    bandera_mas_altura =  False
    max_altura = 0
    for heroes in lista:
        if(float(max_altura) < float(heroes["altura"])) or (bandera_mas_altura == False):
            bandera_mas_altura = True
            max_altura = heroes["altura"]
    print(max_altura)
    print("---------------------------")

#E
def heroe_mas_bajo(lista):
    bandera_menos_altura =  False
    menos_altura = 0
    for heroes in lista:
        if(float(menos_altura) > float(heroes["altura"])) or (bandera_menos_altura == False):
            bandera_menos_altura = True
            menos_altura = heroes["altura"]
    print(menos_altura)
    print("---------------------------")

#F
def promedio_altura(lista):
    acumulador_alturas = 0
    for i in range(len(lista)):
        acumulador_alturas += float(lista[i]["altura"])
    promedio_altura = acumulador_alturas / len(lista)
    print(promedio_altura)
    print("---------------------------")

#G
def nombre_heroe_mas_bajo_alto(lista):
    bandera_altura =  False
    max_altura = 0
    menos_altura = 0
    for heroes in lista:
        altura = float(heroes["altura"])
        max_altura = float(max_altura)
        menos_altura = float(menos_altura)
        if(not bandera_altura):
            bandera_altura = True
            menos_altura = heroes["altura"]
            max_altura = heroes["altura"]
            nombre_menos_altura = heroes["nombre"]
            nombre_max_altura = heroes["nombre"]
        elif(max_altura < altura):
            max_altura = heroes["altura"]
            nombre_max_altura = heroes["nombre"]
        elif(menos_altura > altura):
            menos_altura = heroes["altura"]
            nombre_menos_altura = heroes["nombre"]
    print(f"El heroe con mas altura es: {nombre_max_altura} y el de menos altura {nombre_menos_altura}")


#H
def heroe_mas_menos_pesado(lista):
    bandera_peso =  False
    max_peso = 0
    menos_peso = 0
    for heroes in lista:
        peso = float(heroes["peso"])
        max_peso = float(max_peso)
        menos_peso = float(menos_peso)
        if(not bandera_peso):
            bandera_peso = True
            menos_peso = heroes["peso"]
            max_peso = heroes["peso"]
            nombre_menos_peso = heroes["nombre"]
            nombre_max_peso = heroes["nombre"]
        elif(max_peso < peso):
            max_peso = heroes["peso"]
            nombre_max_peso = heroes["nombre"]
        elif(menos_peso > peso):
            menos_peso = heroes["peso"]
            nombre_menos_peso = heroes["nombre"]
    print(f"El heroe con mas peso es: {nombre_max_peso} y el de menos peso {nombre_menos_peso}")

#I

#J

while True:
        os.system("cls")
        print("""*** Menu de opciones ***
    --------------------------
    1- Ver el nombre de cada superheroe
    2- Ver el nombre y altura de cada superheroe
    3- Superheroe mas alto
    4- Superheroe mas bajo
    5- Altura promedio de los superheroes
    6- Nombre superheroe con mas y menos altura
    7- Nombre superheroe con mas y menos peso
    8-Salir del programa""")
        opcion = input("Ingrese una opcion: ")
        while(not opcion.isdigit() or (float(opcion) < 1 or float(opcion) > 8)):
            opcion = input("No es una opcion valida, por favor ingrese otra: ")

        match(opcion):
            case "1":
                nombre_heroes(lista_heroes)
            case "2":
                nombre_altura_heroes(lista_heroes)
            case "3":
                heroe_mas_alto(lista_heroes)
            case "4":
                heroe_mas_bajo(lista_heroes)
            case "5":
                promedio_altura(lista_heroes)
            case "6":
                nombre_heroe_mas_bajo_alto(lista_heroes)
            case "7":
                heroe_mas_menos_pesado(lista_heroes)
            case "8":
                print("Saliste del programa")
                break
        os.system("pause")
    

    

    




    