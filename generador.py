from random import randint
from random import shuffle

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

def generate(matrix, n, m):
    N = n ** 2
    vals = dfs([], n)

    for i in range(N*N):
        val = vals[i]
        x, y = cords(i, N)
        matrix[y][x] = val

    #show(matrix)
    #print()

    pistas = {
        (2, 1): 8,
        (2, 2): 6,
        (2, 3): 4,

        (3, 1): 40,
        (3, 2): 30,
        (3, 3): 17
    }

    pistas_size = pistas[(n, m)]
    pistas = list(range(N**2))
    shuffle(pistas)
    pistas = [cords(elem, N) for elem in pistas[:pistas_size]]

    for i in range(N):
        for j in range(N):
            matrix[i][j] = matrix[i][j] if (j,i) in pistas else 0
    return pistas

def show(matrix):
    for row in matrix:
        for col in row:
            print(col if col else ' ', end="")
        print()

#### test

def init(n, m):
    emp = empty_matrix(n**2)
    pistas = generate(emp, n, m)
    return emp, pistas

def test(n):
    emp = empty_matrix(n**2)

    generate(emp, n)
    show(emp)

def main():
    test(3)
