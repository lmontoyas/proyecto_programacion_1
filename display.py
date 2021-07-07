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
