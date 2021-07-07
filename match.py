from generador import init
from display import mostrar
from jugada import operar
from jugada import is_over
from colorama import Fore

def clear():
    print("\x1b[2J\x1b[H",end="")

def turno(tablero, n, mensaje, pistas):

    clear()

    blue = Fore.BLUE
    white = Fore.WHITE
    cyan = Fore.CYAN

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

    mostrar(tablero, n, pistas)
    print()

    print(mensaje)

    F = input(white+"Ingrese FILA: "+blue)
    C = input(white+"Ingrese COLUMNA: "+blue)
    V = input(white+"Ingrese VALOR: "+blue)
    print(white)
    return operar(F, C, V, tablero, n, pistas)

def nivel(nivel):
    n = nivel

    tablero, pistas = init(n)
    msj = ""
    print(is_over(tablero))
    while not is_over(tablero):
        msj = turno(tablero, n, msj, pistas)

    clear()
    mostrar(tablero,n,pistas)
    print()
    print("Felicidades te ganaste 1000 soles")

def pantalla(msj=""):

    clear()

    blue = Fore.BLUE
    green = Fore.GREEN
    white = Fore.WHITE
    red = Fore.RED

    error_opcion = red + "Opción inválida, debe escribir 1,2 o 3" + white

    imagen="""                 .___      __
  ________ __  __| _/____ |  | ____ __
 /  ___/  |  \/ __ |/  _ \|  |/ /  |  \ .
 \___ \|  |  / /_/ (  <_> )    <|  |  /
/____  >____/\____ |\____/|__|_ \____/
     \/           \/           \/"""

    print(imagen)
    print()
    print(blue+'Seleccionar dificultad:'+white)
    print()
    print("["+blue+"1"+white+"]"+green+" Fácil: "+white+"TABLERO 4x4")
    print()
    print("["+blue+"2"+white+"]"+green+" Dificil: "+white+"TABLERO 9x9")
    print()
    print("["+blue+"3"+white+"]"+blue+" SALIR"+white)
    print()
    n = 0
    print(msj)
    n = input("Elija opción: ")
    if not n in ['1','2','3']:
        pantalla(error_opcion)
    n = int(n) + 1
    nivel(n)

pantalla()
