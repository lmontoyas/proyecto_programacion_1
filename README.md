![Alt text](images/main.png?raw=true "Title")

# Sudoku | Programación I Lab 303 UTEC 2021

Para jugar el juego ejecute el archivo `sudoku.py`
```
$> python sudoku.py
```

## Tabla de contenido:
1. [Generador](#generador)
2. [Display](#display)
3. [Sudoku](#sudoku)
4. [Jugada](#jugada)
5. [Autores](#autores)

# Módulos
## Generador

En el módulo `generador.py` se encuentran las funciones que generan el tablero inicial de sudoku. La idea principal de este módulo es generar un tablero de sudoku completo y luego retirar elementos para que pueda ser resuelto por el usuario. La estrategía es ir insertando valores fila por fila hasta obtener un tablero válido.

### DFS

Depth Breadth Search (Búsqueda por profundidad), usualmente es un algoritmo recursivo usado para operar sobre estructuras de datos que presentan características de Grafo. Cómo mencionamos anteriormente, vamos a resolver el problema fila por fila. Definimos como `nodo` a un tablero lleno con una cantidad `k` de casilleros y que es válido según las reglas de sudoku. 

![Alt text](images/nodo.jpg?raw=true "Title")

La idea es continuar explorando los posibles nodos que podrían generarse a partir de este. Por ejemplo el siguiente tablero es generado a partir del nodo anterior.

![Alt text](images/vecino.jpg?raw=true "Title")

Dónde `A` es un número de 1 a 9 inclusive. Entonces tenemos 9 tableros que pueden generarse a partir del anterior. Hacemos llamada recursiva a la función con uno de estos nodos y de no encontrar una solución final válida con este, continuamos con el siguiente nodo generado.

```python

# El parámetro 'ans' es la respuesta acumulada con k valores.
# como se explicó arriba, hacemos llamada recursiva a las respuestas de k + 1

def dfs(ans, n):

# n = 2 para fácil
# n = 3 para dificil

    N = n ** 2

# El tablero sería de N x N
  
# Validamos que 'ans' siga las reglas de sudoku
    
    if not validar(ans, n):
        return False
        
# Luego escribimos el caso base.
# El caso base es cuando completamos el tablero.
# Esto se verifica cuando el tamaño de 'ans' es N x N

    if len(ans) == N*N:
        return ans
 
# Luego buscamos el siguiente elemento a llenar el tablero.
# El siguiente elemento debe ser de 1 a 9.
# Pero para evitar que el mismo tablero se genere cada vez,
# definimos una variable 'shift' de forma aleatorea
# Por ejemplo si shift = 4,
# entonces el orden de los elementos a probar será, para N = 9
# 4,5,6,7,8,9,1,2,3 en lugar de 1,2,3,4,5,6,7,8,9
 
    shift = randint(0, N - 1)
    for i in range(N):
        val = shift + i
        val %= N
        val += 1
        newans = ans[:]
        newans.append(val)
        
        # llamada recursiva con el siguiente nodo
        newans = dfs(newans, n)
        
        # si existe una respuesta, se retorna
        if newans:
            return newans
    
# Si se visitó todos los nodos vecinos a este,
# y no se encontró solución por este camino,
# se retorna False, para indicar al nodo padre
# que busque una solución con los otros nodos
    
    return False
```
### Validar

Notar que la representación del tablero en la variable `ans` es una lista de una dimensión. Si el `i-esimo` elemento de `ans` representa un elemento en la matriz, para obtener en que columna y fila se encuentra escribimos la siguiente función:

```python

# 'val' es el índice que tiene el elemento en 'ans'.
# ans llena la matriz por filas, entonces:
# la columna estaría dada por val % N
# y su fila por val // N

def cords(val, N):
    return (val%N, val//N)
```
También podemos obtener en que grilla de `n x n` se encuentra operando `c = x//n + y - y%n`.

```python
def validar(ans, n):
    N = n ** 2
    
    # Para validar a 'ans', creamos subconjuntos que
    # verifiquen que los elementos no se repitan.
    
    # I es el conjunto de filas
    # I[x] es la x-esima fila
    I = [[] for _ in range(N)]
    
    # J es el conjunto de Columnas
    J = [[] for _ in range(N)]
    
    # C es el conjunto de grillas
    C = [[] for _ in range(N)]
    
    # En realidad, el orden de I, J y C no importa,
    # mientras se verifique que no se repitan los elementos.

    for i in range(len(ans)):
    
        # se calcula x,y,c
        
        x,y = cords(i, N)
        c = x//n + y - y%n
        v = ans[i]
        
        # se verifica que v no esté vacía
        if not v:
            continue
        
        # se verifica que no se repita
            
        if v in I[x]:
            return False
        if v in J[y]:
            return False
        if v in C[c]:
            return False
        I[x].append(v)
        J[y].append(v)
        C[c].append(v)

    # De no haber repetidos se retorna True

    return True
```

### Generate

Para crear una matriz vacía simplemente escribimos la siguiente función:

```python
def empty_matrix(N):
    return [[0]*N for _ in range(N)]
```
Para generar la respuesta usamos las funciones anteriormente definidas:

```python

# 'matrix' es la matriz vacía
def generate(matrix, n):
    
    N = n ** 2
    
    # Buscamos una solución,
    # inicialmente 'ans' es una lista vacía
    vals = dfs([], n)

    # Transformamos a 'ans' en una matrix de N*N

    for i in range(N*N):
        val = vals[i]
        x, y = cords(i, N)
        matrix[y][x] = val

    # Dejamos una cantidad de pistas
    # y borramos los demás casilleros

    pistas_size = 17 if n == 3 else 8
    pistas = [randint(0,N**2 - 1) for _ in range(pistas_size)]
    pistas = [cords(elem, N) for elem in pistas]

    for i in range(N):
        for j in range(N):
            matrix[i][j] = matrix[i][j] if (j,i) in pistas else 0

    # se modifica la matriz
    # Y también retornamos las pistas para usarlas luego
    return pistas

# init es la función principal de este módulo,
# retorna matriz inicial y una lista de pistas.
# La lista de pistas se retorna para diferenciarlas
# de las casillas ingresadas por el usuario posteriormente.

def init(n):
    emp = empty_matrix(n**2)
    pistas = generate(emp, n)
    return emp, pistas
```

## Display

![Alt text](images/hardmode.png?raw=true "Title")

El módulo `display.py` contiene funciones para imprimir el tablero como se muestra en la imagen.

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

## Sudoku

El módulo `sudoku.py`, es la función principal y tiene funciones que le permiten al jugador interactuar con el juego.

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

### Menu principal

![Alt text](images/main.png?raw=true "Title")

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

### Partida

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

    # Al acabar el juego se regresa al menú principal,
    # Pero mostrando nuevos mensajes:

    image = """  ________  ________
 /  _____/ /  _____/ .
/   \  ___/   \  ___
\    \_\  \    \_\  \ .
 \______  /\______  / .
        \/        \/ """

    pantalla("", image, puntaje)

```

![Alt text](images/endgame.png?raw=true "Title")

```python
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


## Jugada

El módulo `jugada.py` verifica que una jugada sea válida y le asigna un puntaje dependiendo.

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

## Autores:

Luis Golac  
Jorge Miranda  
Lyam Cáceres  
Leonardo Montoya  
