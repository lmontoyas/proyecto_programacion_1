def parse(F,C,V,N):

    error_casilla= "Ingresar casilla válida"
    error_numero = "Numero fuera de rango"
    error_valor = "Valor no es numerico"

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

def operar(F, C, V, tablero, n):

    error_jugada = "Jugada no valida"

    N = n ** 2

    F,C,V,msj = parse(F,C,V,N)

    if msj: return msj

    return "Todo good"
