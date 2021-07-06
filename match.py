from generador import init
from display import mostrar

def turno(tablero, n):

    print("\x1b[2J\x1b[H",end="")

    mostrar(tablero, n)
    print()
    a = input("Ingrese Fila: ")
    b = input("Ingrese Columna: ")
    n = input("Ingrese Valor: ")
    print()

def is_fin(tablero):
    return False

def nivel(nivel):
    n = 3 if nivel == "dificil" else 2
    tablero = init(n)
    while not is_fin(tablero):
        turno(tablero, n)

nivel("ez")
