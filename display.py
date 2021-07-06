def separador(n, j):
    return j != n*n - 1 and j % n == n - 1

def format(n, j, sep, esp):
    N = n ** 2
    if separador(n,j):
        print(sep, end="")

def printfila(fila, n, begin, sep, esp):
    print(begin, end="   ")
    N = n ** 2
    for j in range(N):
        if j%n: print(esp, end="")
        print(fila[j] or " ", end="")
        format(n, j, sep, esp)
    print()

def mostrar(matrix, n):
    N = n ** 2
    printfila([chr(ord('A')+i) for i in range(N)],n," ", " ", " ")
    print()
    for i in range(N):
        printfila(matrix[i], n, i + 1, "|", ' ')
        if separador(n, i):
            printfila('-'*N,n, " ", "+", '-')
