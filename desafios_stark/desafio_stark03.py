from data_stark import lista_heroes
import re
import os

#1.1
def extraer_iniciales(nombre_heroe = ""):
    if(nombre_heroe == ""):
        return "N/A"
    elif(re.search(r"the", nombre_heroe)):
        nombre_heroe = re.sub(r"the", "", nombre_heroe)
    elif(re.search(r"-", nombre_heroe)):
        nombre_heroe = re.sub(r"-"," ", nombre_heroe)
    
    iniciales = ""
    bandera_iniciales = False
    lista = nombre_heroe.split(" ")
    for elementos in lista:
        if(elementos == ""):
            lista.remove("")
    for nombre in lista:
        if(len(lista) > 1):
            if(not bandera_iniciales):
                bandera_iniciales = True
                iniciales += nombre[0].upper()
                iniciales += "."
            else:
                iniciales += nombre[0].upper()
        else:
            iniciales += nombre[0].upper()
    return iniciales
    
#1.2

def definir_iniciales_nombre(heroe):
    if(type(heroe) != dict):
        return False
    try:
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        return True
    except KeyError:
        return False

#1.3

def agregar_iniciales_nombre(lista:list):
    lista_iniciales = []
    for heroes in lista:
        if(definir_iniciales_nombre(heroes)):
            lista_iniciales.append(heroes)
        else:
            print("El origen de datos no contiene el formato correcto")
            return False
    return True
    
#1.4

def stark_imprimir_nombres_con_iniciales(lista):
    if(type(lista) != list):
        return False
    if(len(lista) == 0):
        return False
    agregar_iniciales_nombre(lista)
    for heroes in lista:
        print(f'{heroes["nombre"]}({heroes["iniciales"]})')

#2.1

def generar_codigo_heroe(id_heroe, genero_heroe):
    if(type(id_heroe) != int):
        return False
    if(genero_heroe != "M" and genero_heroe != "F" and genero_heroe != "NB"):
        return False
    cadena_genero_id = f'{genero_heroe}-{id_heroe}'
    return cadena_genero_id

#2.2

def agregar_codigo_heroe(heroe, id_heroe):
    if(len(heroe) == 0):
        return False
    codigo = generar_codigo_heroe(id_heroe, heroe["genero"])
    if(len(codigo) > 10):
        return False
    heroe["codigo_heroe"] = codigo
    return True

#2.3

def stark_generar_codigos_heroes(lista):
    if(len(lista) == 0):
        print("El origen de datos no contiene el formato correcto")
        return False
    contador = 0
    for heroes in lista:
        contador += 1
        if(type(heroes) != dict):
            print("El origen de datos no contiene el formato correcto")
            return False
        try:
            heroes["genero"]
        except KeyError:
            print("El origen de datos no contiene el formato correcto")
            return False
        agregar_codigo_heroe(heroes, contador)
    print(f'Se asignarion {contador} codigos')
    for heroes in lista:
        print(f'El codigo de {heroes["nombre"]} es {heroes["codigo_heroe"]}')

#3.1

def sanitizar_entero(numero_str):
    try:
        numero_str = numero_str.strip()
        if(numero_str[0] == "-"):
            return -2
        if(not numero_str.isdigit()):
            return -1
        return int(numero_str)
    except ValueError:
        return -3

#3.2

def sanitizar_flotante(numero_str):
    try:
        numero_str = numero_str.strip()
        if(numero_str[0] == "-"):
            return -2
        if(not numero_str.isdigit()):
            if(re.search(r"\.", numero_str)):
                if(re.search(r"[^0-9\.]", numero_str)):
                    return -1
                return float(numero_str)
            return -1
        return float(numero_str)
    except ValueError:
        return -3
    
#3.3

def sanitizar_string(valor_str, valor_por_defecto = "-"):
    if(re.findall(r'\d', valor_str)):
        return "N/A"
    valor_str = re.sub(r"/", " ", valor_str)
    if(len(valor_str) == 0):
        return valor_por_defecto.lower()
    valor_str = valor_str.strip().lower()
    return valor_str

#3.4

def sanitizar_dato(heroe, clave, tipo_dato):
    if(tipo_dato.lower() != "string" and tipo_dato.lower() != "entero" and tipo_dato.lower() != "flotante"):
        print("Tipo de dato no conocido")
        return False
    try:
        if(tipo_dato.lower() == "string"):
            sanitizar_string(heroe[clave])
            return True
        elif(tipo_dato.lower() == "entero"):
            sanitizar_entero(heroe[clave])
            return True
        elif(tipo_dato.lower() == "flotante"):
            sanitizar_flotante(heroe[clave])
            return True
    except KeyError:
        print('La clave especificada no existe en el héroe')
        return False
    
#3.5

def stark_normalizar_datos(lista):
    if(len(lista) == 0):
        print("Error, lista de heroes vacia")
        return False
    for heroes in lista:
        sanitizar_dato(heroes, "altura", "flotante")
        sanitizar_dato(heroes, "peso", "flotante")
        sanitizar_dato(heroes, "color_ojos", "string")
        sanitizar_dato(heroes, "color_pelo", "string")
        sanitizar_dato(heroes, "fuerza", "entero")
        sanitizar_dato(heroes, "inteligencia", "string")
    print("Datos normalizados")

#4.1

def generar_indice_nombres(lista):
    if(len(lista) == 0):
        print("lista vacia")
        return False
    lista_nombres = []
    try:
        for heroes in lista:
            if(type(heroes) != dict):
                print("Los elementos de la lista no son de tipo diccionario")
                return False
            lista_heroe = heroes["nombre"].split(" ")
            for nombre in lista_heroe:
                lista_nombres.append(nombre)
        return lista_nombres
    except KeyError:
        print('El origen de datos no contiene el formato correcto')
        return False
    
#4.2

def stark_imprimir_indice_nombre(lista):
    if(len(lista) == 0):
        print("Error, la lista de heroes esta vacia")
        return False
    lista_nombres = generar_indice_nombres(lista)
    cadena_nombres = "-".join(lista_nombres)
    print(cadena_nombres)

#5.1

def convertir_cm_a_mtrs(valor_cm):
    valor_cm = str(valor_cm)
    if(re.search(r'\.', valor_cm)):
        if(re.search(r"[^0-9\.]", valor_cm)):
            return -1
        valor_cm = float(valor_cm)
        valor_mtrs = valor_cm / 100
        return valor_mtrs
    return -1

   
#5.2

def generar_separador(patron:str, largo:int, imprimir = True):
    if(len(patron) < 1 or len(patron) > 2):
        print("El patron debe tener entre uno y dos caracteres")
        return "N/A"
    if(largo < 1 and largo > 235):
        print("El largo debe ser entre 1 y 235")
        return "N/A"
    separador = ""
    for i in range(largo):
        separador += patron
    if(imprimir):
        print(separador)
        return separador
    else:
        return separador
    
#5.3

def generar_encabezado(titulo:str):
    return f'{generar_separador("*", 50, False)}\n{titulo.upper()}\n{generar_separador("*", 50, False)}'

#5.4

def imprimir_ficha_heroe(heroe:dict):
    agregar_codigo_heroe(heroe, 1)
    print(generar_encabezado("general"))
    print(f'Nombre del heroe:         {heroe["nombre"]}')
    print(f'Identidad secreta:        {heroe["identidad"]}')
    print(f'Consultora:               {heroe["empresa"]}')
    print(f'Codigo del heroe:         {heroe["codigo_heroe"]}')
    print(generar_encabezado("fisico"))
    print(f'Altura:      {convertir_cm_a_mtrs(heroe["altura"])}')
    print(f'Peso:        {float(heroe["peso"])}')
    print(f'Fuerza:      {heroe["fuerza"]}')
    print(generar_encabezado("señas particulares"))
    print(f'Color de ojos:   {heroe["color_ojos"]}')
    print(f'Color de pelo:   {heroe["color_pelo"]}')

#5.5

def stark_navegar_fichas(lista):
    heroe_actual = 0
    while True:
        os.system("cls")
        imprimir_ficha_heroe(lista[heroe_actual])
        print("Elija una opcion")
        print("[1]ir a la izquierda          [2]ir a la derecha        [3]salir" )
        opcion = input("Ingrese una opcion: ")
        while(not opcion.isdigit() or (float(opcion) < 1 or float(opcion) > 3)):
            opcion = input("No es una opcion valida, por favor ingrese otra: ")
            print("[1]ir a la izquierda          [2]ir a la derecha        [3]salir" )
        match(opcion):
            case "1":
                if(heroe_actual == 0):
                    heroe_actual = len(lista)-1
                else:
                    heroe_actual -=1
                imprimir_ficha_heroe(lista[heroe_actual])
            case "2":
                if(heroe_actual == len(lista)-1):
                    heroe_actual = 0
                else:
                    heroe_actual += 1
                imprimir_ficha_heroe(lista[heroe_actual])
            case "3":
                print("saliste")
                break
        os.system("pause")

#6.1

def imprimir_menu():
    print("""*** Menu de opciones ***
    --------------------------
    1- Imprimir la lista de nombres junto con sus iniciales
    2- Generar códigos de héroes
    3- Normalizar datos
    4- Imprimir índice de nombres
    5- Navegar fichas
    6- Salir""")

#6.2

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    while(not opcion.isdigit() or (float(opcion) < 1 or float(opcion) > 16)):
        opcion = input("No es una opcion valida, por favor ingrese otra: ")
    return opcion

#6.3

def stark_marvel_app_3(lista:list):
    os.system("cls")
    while True:
        match(stark_menu_principal()):
            case"1":
                stark_imprimir_nombres_con_iniciales(lista)
            case"2":
                stark_generar_codigos_heroes(lista)
            case"3":
                stark_normalizar_datos(lista)
            case"4":
                stark_imprimir_indice_nombre(lista)
            case"5":
                stark_navegar_fichas(lista)
            case"6":
                print("saliste")
                break
        os.system("pause")

stark_marvel_app_3(lista_heroes)



        



    
    
    
        

