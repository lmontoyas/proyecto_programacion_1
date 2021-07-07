# Sudoku | Programación I Lab 303 UTEC 2021

## Tabla de contenido:
1. [Crear tablero](#crear-tablero)
2. [Display](#display)
3. [Menu](#menu)
4. [Puntaje](#puntaje)
5. [Verificador](#verificador)
6. [Main](#main)

## Estructura
### Modulos:
#### Crear tablero

Crear el tablero dependiendo del nivel:
```python
    def empty_matrix(N):
        return [[0]*N for _ in range(N)]

    def cords(val, N):
        return (val%N, val//N)

    def validar(ans, n):
        N = n ** 2
        I = [[] for _ in range(N)]
        J = [[] for _ in range(N)]
        C = [[] for _ in range(N)]

        for i in range(len(ans)):
            x,y = cords(i, N)
            c = x//n + y - y%n
            v = ans[i]
            if not v:
                continue
            if v in I[x]:
                return False
            if v in J[y]:
                return False
            if v in C[c]:
                return False
            I[x].append(v)
            J[y].append(v)
            C[c].append(v)

    return True
```

Crear los valor random predeterminados dependiendo del nivel:

```python
def dfs(ans, n):
    N = n ** 2
    if not validar(ans, n):
        return False
    if len(ans) == N*N:
        return ans
    shift = randint(0, N - 1)
    for i in range(N):
        val = shift + i
        val %= N
        val += 1
        newans = ans[:]
        newans.append(val)
        newans = dfs(newans, n)
        if newans:
            return newans
    return False

def generate(matrix, n):
    N = n ** 2
    vals = dfs([], n)

    for i in range(N*N):
        val = vals[i]
        x, y = cords(i, N)
        matrix[y][x] = val

    #show(matrix)
    #print()

    pistas_size = 17 if n == 3 else 8
    pistas = [randint(0,N**2 - 1) for _ in range(pistas_size)]
    pistas = [cords(elem, N) for elem in pistas]

    for i in range(N):
        for j in range(N):
            matrix[i][j] = matrix[i][j] if (j,i) in pistas else 0
    return pistas

def show(matrix):
    for row in matrix:
        for col in row:
            print(col if col else ' ', end="")
        print()

def init(n):
    emp = empty_matrix(n**2)
    pistas = generate(emp, n)
    return emp, pistas
```

![Alt text](images/main.png?raw=true "Title")

#### Display
Mostrar menu /
Mostrar el tablero /

```python
from colorama import Fore, Back, Style

def separador(n, j):
    return j != n*n - 1 and j % n == n - 1

def format(n, j, sep, esp):
    N = n ** 2
    if separador(n,j):
        print(sep, end="")

def printfila(fila, n, begin, sep, esp, i = -1, pistas=[]):
    print(begin, end=" ")
    N = n ** 2
    for j in range(N):
        color = Fore.WHITE
        if i != -1 and not (j,i) in pistas:
            color = Fore.GREEN
        if j%n: print(esp, end="")
        print(color + str(fila[j] or " "), end="")
        print(Fore.WHITE, end="")
        format(n, j, sep, esp)
    print()

def mostrar(matrix, n, pistas):
    N = n ** 2
    printfila([chr(ord('A')+i) for i in range(N)],n," ", " ", " ")
    print()
    for i in range(N):
        printfila(matrix[i], n, i + 1, "|", ' ', i, pistas)
        if separador(n, i):
            printfila('-'*N,n, " ", "+", '-')
```

#### Menu

Ingresar posiciones /
Ingresar numero

```python
from generador import init
from display import mostrar
from jugada import operar
from jugada import is_over
from colorama import Fore

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

def turno(tablero, n, mensaje, pistas, ptos, puntaje):

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

    print(mensaje)

    F = input(white+"Ingrese FILA: "+blue)
    C = input(white+"Ingrese COLUMNA: "+blue)
    V = input(white+"Ingrese VALOR: "+blue)
    print(white)
    return operar(F, C, V, tablero, n, pistas)
```

### Mostrar puntajes:

```python
def nivel(nivel):
    n = nivel

    green = Fore.GREEN
    white = Fore.WHITE

    tablero, pistas = init(n)
    msj = ""

    puntaje = 0 # Puntaje inicial
    ptos = 0

    while not is_over(tablero):
        msj, ptos = turno(tablero, n, msj, pistas, ptos, puntaje)
        puntaje += ptos

    image = """  ________  ________
 /  _____/ /  _____/ .
/   \  ___/   \  ___
\    \_\  \    \_\  \ .
 \______  /\______  / .
        \/        \/ """

    pantalla("", image, puntaje)

def pantalla(msj="", image=False, ganaste=False):


    clear()

    blue = Fore.BLUE
    green = Fore.GREEN
    white = Fore.WHITE
    red = Fore.RED

    if ganaste:
        print(green+"¡Hiciste "+ str(ganaste) +" puntos!. ¿Jugar de nuevo?"+white)

    error_opcion = red + "Opción inválida, debe escribir 1,2 o 3" + white
```

### Controlador del menu:

```python
    imagen=image or """                 .___      __
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
        pantalla(error_opcion, image, ganaste)
    n = int(n) + 1
    if n != 4:
        nivel(n)

pantalla()
```

![Alt text](images/hardmode.png?raw=true "Title")
![Alt text](images/ezmode.png?raw=true "Title")

#### Puntaje
Tiempo /
Controlador del puntaje
#### Verificador
Controla las celdas /
Controla las filas /
Controla columnas
#### Main

```python
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

    # El puntaje es proporcional al valor ingresado
    # Valor * Po puntos ganados
    # Si ingresa un valor erroneo pierde Pe puntos

    Pe = -200 #Puntaje de penalidad
    Po = 100 #Puntaje obtenido

    error_jugada = Fore.LIGHTRED_EX + "Jugada no valida" + Fore.WHITE

    N = n ** 2

    F,C,V,msj = parse(F,C,V,N)

    if msj: return msj, Pe

    if (C,F) in pistas:
        return error_jugada, Pe

    rama = []
    for row in tablero:
        rama += row[:]

    rama[F*N+C] = V

    if not validar(rama, n):
        return error_jugada, Pe

    # Si ya había un elemento antes en
    # el tablero, se calcula como la diferencia
    # este valor puede ser negativo

    Po = Po*(V - tablero[F][C])

    tablero[F][C] = V

    return Fore.GREEN + "Jugada válida ✓" + Fore.WHITE, Po

def is_over(tablero):
    for row in tablero:
        for val in row:
            if val == 0:
                return False
    return True
```

![Alt text](images/endgame.png?raw=true "Title")

## Participantes:
Luis Golac  
Jorge Miranda  
Lyam Cáceres  
Leonardo Montoya  
