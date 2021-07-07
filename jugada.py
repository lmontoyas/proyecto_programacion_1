from generador import validar
from colorama import Fore

def parse(F,C,V,N):

    error_casilla= Fore.LIGHTRED_EX + "Ingresar casilla válida" + Fore.WHITE
    error_numero = Fore.LIGHTRED_EX + "Numero fuera de rango" + Fore.WHITE
    error_valor = Fore.LIGHTRED_EX + "Valor no es numerico" + Fore.WHITE

    C = C.upper()
    if len(C) != 1 or ord(C) not in range(ord('A'),ord('Z') + 1):
        return (0,0,0,error_casilla)
    if not F.isnumeric():
        return (0,0,0,error_casilla)
    if not V.isnumeric():
        return (0,0,0,error_valor)

    F = int(F) - 1
    C = ord(C) - ord('A')
    V = int(V)

    if F not in range(N):
        return (0,0,0,error_casilla)
    if C not in range(N):
        return (0,0,0,error_casilla)
    if V not in range(1,N+1):
        return (0,0,0,error_numero)

    return (F,C,V,False)

def operar(F, C, V, tablero, n, pistas):

    error_jugada = Fore.LIGHTRED_EX + "Jugada no valida" + Fore.WHITE

    N = n ** 2

    F,C,V,msj = parse(F,C,V,N)

    if msj: return msj

    if (C,F) in pistas:
        return error_jugada

    rama = []
    for row in tablero:
        rama += row[:]

    rama[F*N+C] = V

    if not validar(rama, n):
        return error_jugada

    tablero[F][C] = V

    return Fore.GREEN + "Jugada válida ✓" + Fore.WHITE

def is_over(tablero):
    for row in tablero:
        for val in row:
            if val == 0:
                return False
    return True
