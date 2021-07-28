from generador import init
from display import mostrar
from jugada import operar
from jugada import is_over

from colorama import Fore
import timeit

def clear():
    print("\x1b[2J\x1b[H",end="")

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

    F = input(white+"Ingrese FILA: "+blue)
    C = input(white+"Ingrese COLUMNA: "+blue)
    V = input(white+"Ingrese VALOR: "+blue)
    print(white)

    stop = timeit.default_timer()

    msj, ptos = operar(F, C, V, tablero, n, pistas)

    # penalidad por segundo
    PT = 10
    tiempo = round(stop - start, 1)

    return msj, ptos - int(tiempo)*PT, tiempo

def nivel(nivel):
    n = nivel

    green = Fore.GREEN
    white = Fore.WHITE

    tablero, pistas = init(n)
    msj = ""

    puntaje = 0 # Puntaje inicial
    ptos = 0
    tiempo = -1

    while not is_over(tablero):
        msj, ptos,tiempo = turno(tablero, n, msj, pistas, ptos, puntaje, tiempo)
        puntaje += ptos

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
        nuevapartida(error_opcion)

    n = int(n)

    if n == 3:
        pantalla()

    print(blue+'\tSeleccionar nivel:'+white)
    print()
    print("\t["+blue+"1"+white+"]"+green+" Fácil: "+white+"TABLERO 4x4")
    print()
    print("\t["+blue+"2"+white+"]"+green+" Dificil: "+white+"TABLERO 9x9")
    print()
    print("\t["+blue+"3"+white+"]"+blue+" Regresar"+white)

    n = input("Elija opción: ")


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

pantalla()
