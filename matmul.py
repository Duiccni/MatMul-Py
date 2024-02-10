import math

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

def print_matrix(matrix: list[list[float]] | None, round_n: int = -1) -> None:
    if matrix == None:
        print("a row-size must be equal b column-size.")
        return
    if round_n == -1:
        for elm in matrix:
            print(elm)
        return
    for elm in matrix:
        print("[", end="")
        for val in range(len(elm) - 1):
            print(f"{round(val, round_n)}, ", end="")
        print(f"{round(elm[-1], round_n)}]")

c = matmul(a, b)

print_matrix(c)

def get_2d_rotation_matrix(angle: float) -> list[list[float]]:
    c = math.cos(angle)
    s = math.sin(angle)
    return [[c, -s], [s, c]]

def degree_to_radian(degree: float) -> float:
    return degree / 180 * math.pi

vec2 = [[1.0],
        [0.0]]
angle = degree_to_radian(45.0)
rotation_matrix = get_2d_rotation_matrix(angle)
new_vec2 = matmul(rotation_matrix, vec2)

print()
print_matrix(vec2)
print()
print_matrix(new_vec2, 4)
