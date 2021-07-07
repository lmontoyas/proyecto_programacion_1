from generador import init
from display import mostrar
from jugada import operar
from jugada import is_over

def clear():
    print("\x1b[2J\x1b[H",end="")

def turno(tablero, n, mensaje):

    clear()

    mostrar(tablero, n)
    print()

    print(mensaje)

    F = input("Ingrese Fila: ")
    C = input("Ingrese Columna: ")
    V = input("Ingrese Valor: ")

    return operar(F, C, V, tablero, n)

def nivel(nivel):
    n = 3 if nivel == "dificil" else 2
    tablero = init(n)
    msj = ""
    print(is_over(tablero))
    while not is_over(tablero):
        msj = turno(tablero, n, msj)

def pantalla():

    clear()

    #print(imagen)
    print('Seleccionar dificultad:')
    print("1. Fácil: Tablero 4x4")
    print("2. Dificil: Tablero 9x9")
    n = 0
    while not n in ['1','2']:
        n = input("Nivel(1/2): ")
    n = int(n) + 1
    nivel(n)

pantalla()
