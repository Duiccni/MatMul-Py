def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]] | None:
    l_size = len(a[0])
    if l_size != len(b):
        return None
    ua = len(a)
    ub = len(b[0])
    ret = [[0.0 for i in range(ub)] for i in range(ua)]
    for xu in range(ua):
        for yu in range(ub):
            for i in range(l_size):
                ret[xu][yu] += a[xu][i] * b[i][yu]
    return ret

a = [[1.0, 4.0],
     [2.0, 5.0],
     [1.0, 7.0]]

b = [[3.0, 7.0, 2.0, 1.0, 11.0],
     [16.0, 22.0, 3.0, 5.0, -1.0]]

def print_matrix(matrix: list[list[float]] | None):
    if matrix == None:
        print("a row-size must be equal b column-size.")
        return
    for elm in matrix:
        print(elm)

c = matmul(a, b)

print_matrix(c)
