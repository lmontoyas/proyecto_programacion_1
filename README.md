# Sudoku | Programación I Lab 303 UTEC 2021

## Tabla de contenido:
1. [Crear tablero](#crear-tablero)
2. [Display](#display)
3. [Menu](#menu)
4. [Puntaje](#puntaje)
5. [Verificador](#verificador)
6. [Ejecutable / Main](#ejecutable-/-main)

## Estructura
### Modulos:
#### Crear tablero

Crear el tablero dependiendo del nivel:

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

Crear los valor random predeterminados dependiendo del nivel:

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

![Alt text](images/main.png?raw=true "Title")

#### Display
Mostrar menu /
Mostrar el tablero /
Mostrar puntajes /
Mostrar tiempos
#### Menu
Controlador del menu /
Ingresar posiciones /
Ingresar numero

![Alt text](images/hardmode.png?raw=true "Title")
![Alt text](images/ezmode.png?raw=true "Title")

#### Puntaje
Tiempo /
Controlador del puntaje
#### Verificador
Controla las celdas /
Controla las filas /
Controla columnas
#### Ejecutable / Main

![Alt text](images/endgame.png?raw=true "Title")

## Participantes:
Luis Golac  
Jorge Miranda  
Lyam Cáceres  
Leonardo Montoya  
