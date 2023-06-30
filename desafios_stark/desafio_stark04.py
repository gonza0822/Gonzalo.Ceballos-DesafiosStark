import json
import re
import os

def imprimir_dato(dato:str):
    print(dato)

#1.1

def imprimir_menu_desafio_5():
    imprimir_dato("*** Menu de opciones ***")
    imprimir_dato("-----------------------------")
    imprimir_dato("A- Recorrer la lista imprimiendo el nombre de cada superheroe masculino")
    imprimir_dato("B- Recorrer la lista imprimiendo el nombre de cada superheroe femenino")
    imprimir_dato("C-  Recorrer la lista imprimiendo el superheroe masculino mas alto")
    imprimir_dato("D- Recorrer la lista imprimiendo el superheroe femenino mas alto")
    imprimir_dato("E- Recorrer la lista imprimiendo el superheroe masculino mas bajo")
    imprimir_dato("F- Recorrer la lista imprimiendo el superheroe femenino mas bajo")
    imprimir_dato("G- Recorrer la lista imprimiendo el promedio de la altura de los superheroes masculinos")
    imprimir_dato("H- Recorrer la lista imprimiendo el promedio de la altura de los superheroes femeninos")
    imprimir_dato("I- indicar nombre de las opciones C a F ")
    imprimir_dato("J- Cuantos superheroes tienen cada tipo de color de ojos")
    imprimir_dato("K- Cuantos superheroes tienen cada tipo de color de pelo")
    imprimir_dato("L- Cuantos superheroes tienen cada tipo de inteligencia")
    imprimir_dato("M- Listar todos los superhereos por color de ojos")
    imprimir_dato("N- Listar todos los superhereos por color de pelo")
    imprimir_dato("O- Listar todos los superhereos por tipo de inteligencia")
    imprimir_dato("Z- Salir")

#1.2

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    eleccion_usuario = input("Elegir una opcion de la A a la O, o Z para salir")
    eleccion_usuario = eleccion_usuario.upper()
    coincidencia = re.search(r"[A-OZ]", eleccion_usuario)
    if coincidencia:
        return eleccion_usuario
    else:
        return -1


#1.4

def leer_archivo(archivo:str)->list:
    with open(archivo, "r") as file:
        contenido = file.read()
        lista_heroes = json.loads(contenido)
        lista_heroes = lista_heroes["heroes"]
    return lista_heroes

lista_heroes = leer_archivo("C:\\Users\\gonza\\Documents\\tecnicatura\\1A\\programacion1\\ejemplo1\\ejecicios_clase3\\data_stark.json")

#1.5

def guardar_archivo(archivo:str, contenido:str):
    try:
        with open(archivo, "w") as file:
            file.write(contenido)
            print("Se creo el archivo exitosamente")
            return True
    except Exception:
        print(f'Error al crear el archivo {archivo}')

#1.6

def capitalizar_palabras(cadena:str):
    lista_palabra = cadena.split(" ")
    for i in range(len(lista_palabra)):
        lista_palabra[i] = lista_palabra[i].capitalize()
    cadena = " ".join(lista_palabra)
    return cadena

#1.7

def obtener_nombre_capitalizado(heroe:dict):
    return f"Nombre:  {capitalizar_palabras(heroe['nombre'])}"

#1.8

def obtener_nombre_y_dato(heroe:dict, key:str):
    try:
        return f"Nombre: {heroe['nombre']} | {key}: {heroe[key]}"
    except KeyError:
        print("Ese atributo no esta en el heroe")
        return False

#2.1

def es_genero(heroe:dict, key:str):
    if(key.upper() != "M" and key.upper() != "F" and key.upper() != "NB"):
        return False
    if(heroe["genero"] == key.upper()):
        return True
    else:
        return False

#2.2

def stark_guardar_heroe_genero(lista:list, genero:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    contenido = "HEROES\n"
    for i in range(len(lista)):
        if(es_genero(lista[i], genero)):
            imprimir_dato(lista[i]["nombre"])
            contenido += f'{obtener_nombre_capitalizado(lista[i])}, '
    contenido = contenido[:-2]
    print(contenido)
    guardar_archivo(f'heroes_{genero.upper()}.csv', contenido)

#3.2

def calcular_max_genero(genero:str, lista:list, key:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    key_max = 0
    nombre_key_max = ""
    bandera_heroes = False
    lista_heroes_genero = []

    for heroes in lista:
        if(heroes["genero"] == genero.upper()):
            lista_heroes_genero.append(heroes)

    for heroes in lista_heroes_genero:
        if(len(heroes)==0):
            return False
        else:
            if(bandera_heroes == False):
                key_max = heroes[key]
                nombre_key_max = heroes["nombre"]
                bandera_heroes = True
            elif(float(heroes[key]) > float(key_max)):
                key_max = heroes[key]
                nombre_key_max = heroes["nombre"]
    return nombre_key_max

#3.1

def calcular_min_genero(genero:str, lista:list, key:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    key_min = 0
    nombre_key_min = ""
    bandera_heroes = False
    lista_heroes_genero = []

    for heroes in lista:
        if(heroes["genero"] == genero.upper()):
            lista_heroes_genero.append(heroes)

    for heroes in lista_heroes_genero:
        if(len(heroes)==0):
            return False
        else:
            if(bandera_heroes == False):
                key_min = heroes[key]
                nombre_key_min = heroes["nombre"]
                bandera_heroes = True
            elif(float(heroes[key]) < float(key_min)):
                key_min = heroes[key]
                nombre_key_min = heroes["nombre"]
    return nombre_key_min

#3.3

def calcular_max_min_dato_genero(lista:list, calculo:str, key:str, genero:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    if(calculo == "maximo"):
        nombre_pedido = calcular_max_genero(genero, lista, key)
    elif(calculo == "minimo"):
        nombre_pedido = calcular_min_genero(genero, lista, key)
    else:
        return -1
    return nombre_pedido

#3.4

def stark_calcular_imprimir_guardar_heroe_genero(lista:list, calculo:str, key:str, genero:str):
    nombre_pedido = calcular_max_min_dato_genero(lista, calculo, key, genero)
    for heroes in lista:
        if(heroes["nombre"] == nombre_pedido):
            cadena = obtener_nombre_y_dato(heroes, key)
            imprimir_dato(cadena)
    guardar_archivo(f'heroes_{calculo}_{key}_{genero.upper()}.csv', cadena)

#4.1

def sumar_dato_heroe_genero(lista:list, key:str, genero:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    lista_heroes_genero = []
    for heroes in lista:
        if(heroes["genero"] == genero.upper()):
            lista_heroes_genero.append(heroes)
    suma = 0
    for heroes in lista_heroes_genero:
        if(not isinstance(heroes, dict)) or len(heroes) == 0:
            return -1
        else:
            suma += float(heroes[key])
    return suma

#4.2

def cantidad_heroes_genero(lista:list, genero:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    lista_heroes_genero = []
    for heroes in lista:
        if(heroes["genero"] == genero.upper()):
            lista_heroes_genero.append(heroes)
    cantidad = 0
    for heroes in lista_heroes_genero:
        cantidad += 1
    return cantidad

#4.3

def calcular_promedio_genero(lista:list, key:str, genero:str):
    if(genero.upper() != "M" and genero.upper() != "F"):
        return False
    suma = sumar_dato_heroe_genero(lista, key, genero)
    cantidad = cantidad_heroes_genero(lista_heroes, genero)
    promedio = round(suma / cantidad)
    return promedio

#4.4

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list, genero):
     if(len(lista) == 0):
         print("La lista esta vacia")
         return False
     contenido = calcular_promedio_genero(lista, "altura", genero)
     imprimir_dato(f'Altura promedio genero {genero.upper()}: {str(calcular_promedio_genero(lista, "altura", genero))}')
     guardar_archivo(f'heroes_promedio_altura_{genero.upper()}.csv', str(contenido))
    
#5.1

def calcular_cantidad_tipo(lista:list, key:str):
    if(len(lista) == 0):
        return {
            "Error": "La lista se encuenta vacia"
        }
    lista_tipos = set()
    diccionario_cantidad_tipos = {}
    for heroes in lista:
        lista_tipos.add(heroes[key])
    for tipos in lista_tipos:
        contador = 0
        for heroes in lista:
            if(tipos == heroes[key]):
                contador += 1
        diccionario_cantidad_tipos[capitalizar_palabras(tipos)] = contador
    return diccionario_cantidad_tipos

#5.2

def guardar_cantidad_heroes_tipo(tipos_datos:dict, dato:str):
    mensaje = ""
    for key in tipos_datos:
        mensaje += f'Caracteristica: {dato} {key} - Cantidad de heroes: {tipos_datos[key]}\n'
    guardar_archivo(f'Heroes_cantidad_{dato}.csv', mensaje)
    return True
    
#5.3

def stark_calcular_cantidad_por_tipo(lista:list, key:str):
    try:
        guardar_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes, key), key)
        return True
    except Exception:
        return False

#6.1

def obtener_lista_de_tipos(lista:list, key:str):
    lista_de_tipos = []
    for heroes in lista:
        if(heroes[key] == ""):
            lista_de_tipos.append("N/A")
        lista_de_tipos.append(capitalizar_palabras(heroes[key]))
    for keys in lista_de_tipos:
        if(keys == ""):
            lista_de_tipos.remove(keys)
    lista_de_tipos = set(lista_de_tipos)
    return lista_de_tipos

#6.2

def normalizar_dato(dato:str, valor_por_defecto = "N/A"):
    if(dato == ""):
        dato = valor_por_defecto
    return dato

#6.3

def normalizar_heroe(heroe:dict, key:str):
    atributo = capitalizar_palabras(heroe[key])
    atributo = normalizar_dato(atributo)
    nombre_heroe = capitalizar_palabras(heroe["nombre"])
    return f'{nombre_heroe} {atributo}'

#6.4

def obtener_heroes_por_tipo(lista:list, set_de_tipos:set, key:str):
    diccionario_tipos_nombres = {}
    bandera_tipos = False
    for tipos in set_de_tipos:
        lista_nombres = []
        for heroes in lista:
            if(tipos == heroes[key]):
                lista_nombres.append(heroes["nombre"])
        diccionario_tipos_nombres[normalizar_dato(tipos)] = lista_nombres
    for tipos in set_de_tipos:
        for keys in diccionario_tipos_nombres:
            if(tipos == keys):
                bandera_tipos = True
        if(bandera_tipos == False):
            diccionario_tipos_nombres[tipos] = []
    return diccionario_tipos_nombres

#6.5

def guardar_heroes_por_tipo(diccionario:dict, key:str):
    mensajes = ""
    for keys in diccionario:
        mensaje = f'{key} {keys}: '
        for nombre in diccionario[keys]:
            mensaje += f'{nombre} | '
        mensaje = mensaje[:-2]
        mensajes += f'{mensaje}\n'

    print(mensajes)
    try:
        guardar_archivo(f'heroes_segun_{key}.csv', mensajes)
        return True
    except Exception:
        return False

guardar_heroes_por_tipo(obtener_heroes_por_tipo(lista_heroes, obtener_lista_de_tipos(lista_heroes, "color_ojos"), "color_ojos"), "color_ojos")

#6.6

def stark_listar_heroes_por_dato(lista:list, key:str):
    try:
        guardar_heroes_por_tipo(obtener_heroes_por_tipo(lista, obtener_lista_de_tipos(lista, key), key), key)
        return True
    except Exception:
        return False

#1.3

def stark_marvel_app_5(lista:list):
    while True:
        os.system("cls")
        match(stark_menu_principal_desafio_5()):
            case "A":
                stark_guardar_heroe_genero(lista, "m")
            case "B":
                stark_guardar_heroe_genero(lista, "f")
            case "C":
                print(calcular_max_min_dato_genero(lista, "maximo", "altura", "m"))
            case "D":
                print(calcular_max_min_dato_genero(lista, "maximo", "altura", "f"))
            case "E":
                print(calcular_max_min_dato_genero(lista, "minimo", "altura", "m"))
            case "F":
                print(calcular_max_min_dato_genero(lista, "minimo", "altura", "f"))
            case "G":
                print(calcular_promedio_genero(lista, "altura", "m"))
            case "H":
                print(calcular_promedio_genero(lista, "altura", "f"))
            case "I":
                print(calcular_max_min_dato_genero(lista, "maximo", "altura", "m"))
                print(calcular_max_min_dato_genero(lista, "maximo", "altura", "f"))
                print(calcular_max_min_dato_genero(lista, "minimo", "altura", "m"))
                print(calcular_max_min_dato_genero(lista, "minimo", "altura", "f"))
            case "J":
                stark_calcular_cantidad_por_tipo(lista, "color_ojos")
            case "K":
                stark_calcular_cantidad_por_tipo(lista, "color_pelo")
            case "L":
                stark_calcular_cantidad_por_tipo(lista, "inteligencia")
            case "M":
                stark_listar_heroes_por_dato(lista, "color_ojos")
            case "N":
                stark_listar_heroes_por_dato(lista, "color_pelo")
            case "O":
                stark_listar_heroes_por_dato(lista, "inteligencia")
            case "Z":
                print("saliste")
                break
        os.system("pause")

stark_marvel_app_5(lista_heroes)





    






 










