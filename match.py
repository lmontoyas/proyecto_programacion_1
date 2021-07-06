from generador import init
from display import mostrar
from generador import validar
from jugada import operar

def turno(tablero, n, mensaje):

    print("\x1b[2J\x1b[H",end="")

    mostrar(tablero, n)
    print()

    print(mensaje)

    F = input("Ingrese Fila: ")
    C = input("Ingrese Columna: ")
    V = input("Ingrese Valor: ")

    return operar(F, C, V, tablero, n)

def is_fin(tablero):
    return False

def nivel(nivel):
    n = 3 if nivel == "dificil" else 2
    tablero = init(n)
    msj = ""
    while not is_fin(tablero):
        msj = turno(tablero, n, msj)

nivel("dificil")
