def mostrar(matrix, n):
    N = n ** 2
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end="")
            if j and not (j+1) % n:
                print("|", end="")
        print()
