from random import randint

def empty_matrix(N):
    return [[0]*N for _ in range(N)]

def cords(val, N):
    return (val%N, val//N)

def validar(inis, ans, n):
    N = n ** 2
    I = [[] for _ in range(N)]
    J = [[] for _ in range(N)]
    C = [[] for _ in range(N)]

    cl = len(inis)

    for i in range(len(ans)):
        x,y = cords(inis[i], N)
        c = x//n + y - y%n
        v = ans[i]
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

def dfs(inis, ans, n):
    N = n ** 2
    if not validar(inis, ans, n):
        return False
    if len(ans) == len(inis):
        return ans
    shift = randint(0, N - 1)
    for i in range(N):
        val = shift + i
        val %= N
        val += 1
        newans = ans[:]
        newans.append(val)
        newans = dfs(inis, newans, n)
        if newans:
            return newans
    return False

def generate(matrix, n):
    N = n ** 2
    cl = 17 if n == 3 else 5 
    inis = [randint(0,N**2 - 1) for _ in range(cl)]
    vals = dfs(inis, [], n)
    print(vals)

    for i in range(cl):
        ini = inis[i]
        val = vals[i]
        x, y = cords(ini, N)
        matrix[y][x] = val

def show(matrix):
    for row in matrix:
        for col in row:
            print(col, end="")
        print()

#### test

n = 2
emp = empty_matrix(n**2)
show(emp)
generate(emp, n)
print()
show(emp)
