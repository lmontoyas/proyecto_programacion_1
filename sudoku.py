from generador import init
from display import mostrar
from jugada import operar
from jugada import is_over
import sys

import json

from colorama import Fore, Back, Style
import timeit

global name
name = ""

def showname():
    global name
    space = " "*(20 - len(name))
    print(Back.YELLOW + Fore.BLACK + " ฅ^•ﻌ•^ฅ "+ Back.BLUE +" "+name + " ")
    print(Style.RESET_ALL)

def clear():
    print("\x1b[2J\x1b[H",end="")
    showname()

def showpuntaje(ptos, puntaje):

    blue = Fore.BLUE
    white = Fore.WHITE
    cyan = Fore.CYAN
    red = Fore.RED
    green = Fore.GREEN

    print("Puntaje", end="")
    if ptos:
        print("(", end="")
        if ptos < 0:
            print(red, end="")
        else:
            print(green+"+", end="")
        print(str(ptos), end="")
        print(white+")", end="")
    print(":", end="")
    print(blue,puntaje,end="")
    print('★'+white)

def turno(tablero, n, mensaje, pistas, ptos, puntaje, tiempo):

    clear()

    blue = Fore.BLUE
    white = Fore.WHITE
    cyan = Fore.CYAN
    red = Fore.RED
    green = Fore.GREEN

    textoez = """  ____ _____
 / _  |___  )
( (/ / / __/
 \____|_____)"""

    textohard = """  __   _  ____    _____   _____
 |  |_| ||    \  |     | |     \ .
 |   _  ||     \ |     \ |      \ .
 |__| |_||__|\__\|__|\__\|______/ ."""

    if n == 2 : print(cyan+textoez+white)
    else: print(cyan+textohard+white)

    print()
    showpuntaje(ptos, puntaje)

    print()

    mostrar(tablero, n, pistas)
    print()

    print(mensaje, end=" ")
    if tiempo > 0:
        print("("+str(tiempo)+"s)")
    else:
        print()

    start = timeit.default_timer()

    N = n ** 2

    salir = "salir/quit/exit"

    print("Para salir escriba: "+salir)
    salir = salir.split("/")

    F = input(white+"Ingrese FILA (1-"+str(N)+"): "+blue)

    if F.lower() in salir:
        return pantalla()

    C = input(white+"Ingrese COLUMNA (A-"+chr(ord('A') + N - 1)+"): "+blue)

    if C.lower() in salir:
        return pantalla()

    V = input(white+"Ingrese VALOR (1-"+str(N)+"): "+blue)

    if V.lower() in salir:
        return pantalla()

    print(white)


    stop = timeit.default_timer()

    msj, ptos = operar(F, C, V, tablero, n, pistas)

    # penalidad por segundo
    PT = 10
    tiempo = round(stop - start, 1)

    return msj, ptos - int(tiempo)*PT, tiempo

def nivel(nivel, dificultad, key = False):
    n = nivel

    green = Fore.GREEN
    white = Fore.WHITE

    with open('memory.json', 'r') as f:
        memory = json.load(f)

    msj = ""

    tiempo = -1

    ptos = 0

    if not key:
        key = name + " - " +  str(10*n + dificultad)
        tablero, pistas = init(n, dificultad)
        puntaje = 0 # Puntaje inicial
        game_state = {
            'name': name,
            'tablero': tablero,
            'puntaje': puntaje,
            'nivel': n,
            'dificultad': dificultad,
            'terminada': False,
            'pistas': pistas
        }

        memory[ key ] = game_state

    game_state = memory[ key ]
    puntaje = memory[key]["puntaje"]
    tablero = memory[key]["tablero"]
    pistas =  memory[key]["pistas"]

    pistas = [(x,y) for x,y in pistas]

    with open('memory.json', 'w') as fp:
        json.dump(memory, fp)

    #############

    while not is_over(tablero):
        msj, ptos,tiempo = turno(tablero, n, msj, pistas, ptos, puntaje, tiempo)

        puntaje += ptos

        game_state['tablero'] = tablero
        game_state['puntaje'] = puntaje

        with open('memory.json', 'w') as fp:
            json.dump(memory, fp)

    game_state["terminada"] = True

    with open('memory.json', 'w') as fp:
        json.dump(memory, fp)

    image = """  ________  ________
 /  _____/ /  _____/ .
/   \  ___/   \  ___
\    \_\  \    \_\  \ .
 \______  /\______  / .
        \/        \/ """

    pantalla("", image, puntaje)

def nuevapartida(msj=""):

    clear()

    image = ''' _ __   _____      __
| '_ \ / _ \ \ /\ / /
| | | |  __/\ V  V /
|_| |_|\___| \_/\_/
                 _       _
 _ __ ___   __ _| |_ ___| |__
| '_ ` _ \ / _` | __/ __| '_ \.
| | | | | | (_| | || (__| | | |
|_| |_| |_|\__,_|\__\___|_| |_|'''

    blue = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    white = Fore.WHITE
    red = Fore.RED
    cyan = Fore.CYAN

    error_opcion = red + "Opción inválida, debe escribir 1,2 o 3" + white

    print(blue)
    print(image)
    print(blue)
    print()
    print(blue+'Seleccionar dificultad:'+white)
    print()
    print("["+blue+"1"+white+"]"+green+" Fácil: "+white+"TABLERO 4x4")
    print()
    print("["+blue+"2"+white+"]"+green+" Dificil: "+white+"TABLERO 9x9")
    print()
    print("["+blue+"3"+white+"]"+blue+" Regresar"+white)
    print()
    print(msj)
    n = input("Elija opción: ")

    if not n in ['1','2','3']:
        return nuevapartida(error_opcion)

    n = int(n)

    if n == 3:
        return pantalla()

    msj = " "

    while msj:
        clear()
        print(yellow)


        image_nivel = ''' ________          ________
/   __   \___  ___/   __   \.
\____    /\  \/  /\____    /
   /    /  >    <    /    /
  /____/  /__/\_ \  /____/
                \/          '''

        if n == 1:
            image_nivel = '''   _____           _____
  /  |  |___  ___ /  |  |
 /   |  |\  \/  //   |  |_
/    ^   />    </    ^   /
\____   |/__/\_ \____   |
     |__|      \/    |__| '''


        print(image_nivel)
        print()

        print(blue+'Seleccionar nivel:'+white)
        print()
        print("["+blue+"1"+white+"]"+white+" Principiante "+white+"")
        print()
        print("["+blue+"2"+white+"]"+green+" Intermedio "+white+"")
        print()
        print("["+blue+"3"+white+"]"+yellow+" Avanzado "+white+"")
        print()
        print("["+blue+"4"+white+"]"+blue+" REGRESAR"+white)

        print()
        print(msj)
        m = input("Elija opción: ")

        if not m in ['1', '2', '3', '4']:
            msj = error_opcion
            continue
        else:
            msj = False

    m = int(m)

    if m == 4:
        return nuevapartida()

    nivel(n + 1, m)

def cargar(msj=""):
    global name

    blue = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    white = Fore.WHITE
    red = Fore.RED
    cyan = Fore.CYAN

    error_opcion = red + "Opción inválida" + white

    clear()

    image = '''                    __  _
  _________  ____  / /_(_)___  __  _____
 / ___/ __ \/ __ \/ __/ / __ \/ / / / _ \.
/ /__/ /_/ / / / / /_/ / / / / /_/ /  __/
\___/\____/_/ /_/\__/_/_/ /_/\__,_/\___/
                                         '''

    print(image)
    print()
    print("Partidas guardadas:")
    print()

    with open('memory.json', 'r') as f:
        memory = json.load(f)

    memorias = []
    for key in memory:
        nombre, lvl = key.split(' - ')
        if nombre != name:
            continue
        memorias.append(key)

    for i, key in enumerate(memorias):
        nombre, _ = key.split(' - ')
        puntaje = str(memory[key]["puntaje"])
        n = str(memory[key]["nivel"] ** 2)
        lvl = n + "X" + n

        dificultad = memory[key]["dificultad"]
        dificultad = ["Principiante","Intermedio","Avanzado"][dificultad - 1]

        print( "["+str(i + 1)+"] " + Fore.BLACK
               + Back.BLUE +" ⎙ "+ nombre +" "
               + Back.YELLOW + " " + puntaje + "★ "
               + Back.WHITE + " " + lvl + " "
               + Back.YELLOW + " " + dificultad + " ")
        print(Style.RESET_ALL)

    if not memorias:
        print("No hay partidas guardadas para tu usuario")

    print("["+str(len(memorias) + 1)+"] SALIR")
    print(msj)

    key = input("Elegir opción: ")
    if key not in list([str(i) for i in range(1, len(memorias) + 2)]):
        return cargar(error_opcion)
    key = int(key) - 1
    if key == len(memorias):
        return pantalla()
    key = memorias[key]
    n = memory[key]["nivel"]
    dif = memory[key]["dificultad"]
    nivel(n, dif, key)

def tablero():
    global name

    blue = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    white = Fore.WHITE
    red = Fore.RED
    cyan = Fore.CYAN

    clear()

    image = '''  ____             _    _
 |  _ \ __ _ _ __ | | _(_)_ __   __ _
 | |_) / _` | '_ \| |/ / | '_ \ / _` |
 |  _ < (_| | | | |   <| | | | | (_| |
 |_| \_\__,_|_| |_|_|\_\_|_| |_|\__, |
                                |___/ '''

    print(image)
    print()
    print("Ranking de puntajes máximos:")
    print()

    with open('memory.json', 'r') as f:
        memory = json.load(f)

    memorias = []
    ranking = {}

    for key in memory:
        nombre, lvl = key.split(' - ')
        memorias.append(key)

    for i, key in enumerate(memorias):
        nombre, _ = key.split(' - ')
        puntaje = memory[key]["puntaje"]
        if not nombre in ranking:
            ranking[nombre] = {}
        ranking[nombre]["puntaje"] = max(puntaje ,ranking[nombre].get("puntaje", 0))
        ranking[nombre]["partidas"] = ranking[nombre].get("partidas", 0) + 1

    letop = [(-ranking[key]["puntaje"], key) for key in ranking]
    letop.sort()

    for i,(_, key) in enumerate(letop):
        partidas = str(ranking[key]["partidas"])
        puntaje = str(ranking[key]["puntaje"])
        nombre = key

        print( str(i + 1)+". " + Fore.BLACK
               + Back.BLUE +" ★ "+ nombre +" "
               + Back.YELLOW + " " + puntaje + "★ "
               + Back.WHITE + " " + partidas + " partida/s jugadas ")

        print(Style.RESET_ALL)

    input("Presione [ENTER] para regresar al menu.")
    pantalla()

def setname():

    global name

    image = '''.__           .__  .__
|  |__   ____ |  | |  |   ____
|  |  \_/ __ \|  | |  |  /  _ \.
|   Y  \  ___/|  |_|  |_(  <_> )
|___|  /\___  >____/____/\____/
     \/     \/                  '''

    clear()
    print(image)
    print()
    name = input("Ingrese su nombre: ").lower().replace(" ","-")
    pantalla()

def pantalla(msj="", image=False, ganaste=False):

    clear()
    blue = Fore.BLUE
    green = Fore.GREEN
    white = Fore.WHITE
    red = Fore.RED
    cyan = Fore.CYAN

    if ganaste:
        print(green+"¡Hiciste "+ str(ganaste) +" puntos!. ¿Jugar de nuevo?"+white)

    error_opcion = red + "Opción inválida, debe escribir 1,2 o 3" + white

    imagen=image or """                 .___      __
  ________ __  __| _/____ |  | ____ __
 /  ___/  |  \/ __ |/  _ \|  |/ /  |  \ .
 \___ \|  |  / /_/ (  <_> )    <|  |  /
/____  >____/\____ |\____/|__|_ \____/
     \/           \/           \/"""

    print(imagen)
    print()

    print(blue+'Seleccionar opción:'+white)
    print()
    print("["+green+"1"+white+"]"+green+" NUEVA PARTIDA"+white)
    print()
    print("["+green+"2"+white+"]"+green+" CONTINUAR PARTIDA"+white)
    print()
    print("["+blue+"3"+white+"]"+blue+" TABLA DE POSICIONES"+white)
    print()
    print("["+blue+"4"+white+"]"+blue+" SALIR"+white)
    print()

    n = 0
    print(msj)
    n = input("Elija opción: ")
    if not n in ['1','2','3','4']:
        pantalla(error_opcion, image, ganaste)
    if n == '1':
        nuevapartida()
    if n == '2':
        cargar()
    if n == '3':
        tablero()

    sys.exit()

def main():
    setname()

main()
