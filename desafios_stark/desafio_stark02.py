from data_stark import lista_heroes

def stark_normalizar_datos(lista: list):
    if(len(lista) == 0):
        print("La lista esta vacia")
    else:
        for heroes in lista:
            print(heroes)
            for datos in heroes:
                if (heroes[datos].isdigit()):
                    print(heroes[datos])
                    heroes[datos] = int(heroes[datos])
        print("Datos normalizados")

stark_normalizar_datos(lista_heroes)

#Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
#Nombre: Howard the Duck

def obtener_nombre(heroe:dict) ->str:
    return f'Nombre: {heroe["nombre"]}'

print(obtener_nombre(lista_heroes[1]))

#Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.

def imprimir_dato(dato:str):
    print(dato)

imprimir_dato(lista_heroes[0]["nombre"])

#Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.

def stark_imprimir_nombres_heroes(lista: list):
    if len(lista) == 0:
        print("La lista esta vacia")
    else:
        print(lista)

stark_imprimir_nombres_heroes(lista_heroes)

#Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 

#La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.

#El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
#Nombre: Venom | fuerza: 500


def obtener_nombre_y_dato(heroe:dict, key:str) -> str:
    return f"Nombre: {heroe['nombre']} | {key}: {heroe[key]}"

print(obtener_nombre_y_dato(lista_heroes[0], "peso"))

#Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.

def stark_imprimir_nombres_alturas(lista: list):
    for heroes in lista:
        if(len(heroes)==0):
            return False
        else:
            print(obtener_nombre_y_dato(heroes, "altura"))
    
stark_imprimir_nombres_alturas(lista_heroes)

#Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto.
#Ejemplo de llamada:
#	calcular_max(lista, 'edad')

def calcular_max(lista:list, key:str)->str:
    key_max = 0
    nombre_key_max = ""
    bandera_heroes = False

    for heroes in lista:
        if(len(heroes)==0):
            return False
        else:
            if(bandera_heroes == False):
                key_max = heroes[key]
                nombre_key_max = heroes["nombre"]
                bandera_heroes = True
            elif(heroes[key] > key_max):
                key_max = heroes[key]
                nombre_key_max = heroes["nombre"]
    return nombre_key_max
    
print(calcular_max(lista_heroes, "fuerza"))

#Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más bajo. 

def calcular_min(lista:list, key:str)->str:
    key_min = 0
    nombre_key_min = ""
    bandera_heroes = False

    for heroes in lista:
        if(len(heroes)==0):
            return False
        else:
            if(bandera_heroes == False):
                key_min = heroes[key]
                nombre_key_min = heroes["nombre"]
                bandera_heroes = True
            elif(heroes[key] < key_min):
                key_min = heroes[key]
                nombre_key_min = heroes["nombre"]
    return nombre_key_min
    
print(calcular_min(lista_heroes, "fuerza"))

#4.3

def calcular_max_min_dato(lista:list, calculo:str, key:str)->str:
    if(calculo == "maximo"):
        nombre_pedido = calcular_max(lista, key)
    elif(calculo == "minimo"):
        nombre_pedido = calcular_min(lista, key)
    else:
        return -1
    return nombre_pedido

print(calcular_max_min_dato(lista_heroes, "minimo", "fuerza"))

#4.4

def stark_calcular_imprimir_heroe(lista:list, calculo:str, key:str):
    if(calculo == "maximo"):
        nombre_pedido = calcular_max(lista, key)
        for heroes in lista:
            if(heroes["nombre"] == nombre_pedido):
                print(obtener_nombre_y_dato(heroes, key))
    elif(calculo == "minimo"):
        nombre_pedido = calcular_min(lista, key)
        for heroes in lista:
            if(heroes["nombre"] == nombre_pedido):
                print(obtener_nombre_y_dato(heroes, key))
    else:
        return -1

stark_calcular_imprimir_heroe(lista_heroes, "maximo", "fuerza")
     

#Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro

def sumar_dato_heroe(lista:list, key:str)->int:
    suma = 0
    for heroes in lista:
        if(not isinstance(heroes, dict)) or len(heroes) == 0:
            return -1
        else:
            suma += float(heroes[key])
    return suma

print(sumar_dato_heroe(lista_heroes, "peso"))

#Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0, caso contrario realizar la división entre los parámetros y retornar el resultado

def dividir(dividendo:int, divisor:int)->int:
    if divisor == 0:
        return 0
    else:
        resultado = dividendo/divisor
        return resultado
    
print(dividir(float(lista_heroes[0]["altura"]), float(lista_heroes[1]["altura"])))

#Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro

def calcular_promedio(lista:list, key:str)->int:
    contador = 0
    suma_datos = 0
    for heroes in lista:
        suma_datos += float(heroes[key])
        contador += 1
    promedio = round(suma_datos / contador)
    return promedio

print(calcular_promedio(lista_heroes, "fuerza"))

#Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
#IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3

def stark_calcular_imprimir_promedio_altura(lista:list):
     for heroes in lista:
        if len(heroes) == 0:
            return -1
     imprimir_dato(str(calcular_promedio(lista, "altura")))

stark_calcular_imprimir_promedio_altura(lista_heroes)

#Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)

def imprimir_menu():
    imprimir_dato("*** Menu de opciones ***\n 1 - calcular la altura promedio de los heroes\n 2 - calcular el promedio de cualquier dato numerico de los heroes\n 3 - dividir dos numeros\n 4 - sumar un dato de un heroe\n 5 - calcular maximo o minimo de un atributo numero de un heroe")

#imprimir_menu()

#Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario

def validar_entero(numero:str):
    if not numero.isdigit():
        return False
    else :
        return True
    
print(validar_entero("123.12"))


#Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2

def stark_menu_principal():
    imprimir_menu()
    eleccion_usuario =input("Ingrese una opcion valida: ")

    if (validar_entero(eleccion_usuario)) and (int(eleccion_usuario) > 0 and int(eleccion_usuario) < 6):
        return int(eleccion_usuario)
    else:
        return -1
    
#print(stark_menu_principal())

#Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
#Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.


def stark_marvel_app(lista:list):
    eleccion_usuario = stark_menu_principal()

    match(eleccion_usuario):
        case 1:
            stark_calcular_imprimir_promedio_altura(lista)
        case 2:
            dato = input("que dato desea calcular: ")
            print(calcular_promedio(lista, dato))
        case 3:
            dividendo = int(input("Que numero desea dividir: "))
            divisor = int(input("Por cual numero desea dividirlo: "))
            print(dividir(dividendo, divisor))
        case 4:
            dato = input("Que dato desea que se sumen: ")
            print(sumar_dato_heroe(lista, dato))
        case 5:
            dato = input("Que dato desea calcular el maximo o minimo: ")
            opcion = input("Desea calcular el maximo o el minimo: ")
            print(calcular_max_min_dato(lista, opcion, dato))



stark_marvel_app(lista_heroes)
