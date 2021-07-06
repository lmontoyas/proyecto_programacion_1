from generador import init
from display import mostrar

def turno(tablero):
    a = input()
    b = input()

def nivel(nivel):
    n = 3 if nivel == "dificil" else 2
    tablero = init(n)
    mostrar(tablero, n)

nivel("ez")
