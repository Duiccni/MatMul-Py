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

def get_2d_rotation_matrix(angle: float) -> list[list[float]]:
    c = math.cos(angle)
    s = math.sin(angle)
    return [[c, -s], [s, c]]

def degree_to_radian(degree: float) -> float:
    return degree / 180 * math.pi

'''
a = [[1.0, 4.0],
     [2.0, 5.0],
     [1.0, 7.0]]

b = [[3.0, 7.0, 2.0, 1.0, 11.0],
     [16.0, 22.0, 3.0, 5.0, -1.0]]

c = matmul(a, b)

print_matrix(c)
'''

'''
vec2 = [[1.0],
        [0.0]]
angle = degree_to_radian(45.0)
rotation_matrix = get_2d_rotation_matrix(angle)
new_vec2 = matmul(rotation_matrix, vec2)

print_matrix(vec2)
print_matrix(new_vec2, 4)
'''

def z_rot(z: float) -> list[list[float]]:
    c = math.cos(z)
    s = math.sin(z)
    return [[c, -s, 0],
            [s, c, 0],
            [0, 0, 1]]

def y_rot(y: float) -> list[list[float]]:
    c = math.cos(y)
    s = math.sin(y)
    return [[c, 0, s],
            [0, 1, 0],
            [-s, 0, c]]

def x_rot(x: float) -> list[list[float]]:
    c = math.cos(x)
    s = math.sin(x)
    return [[1, 0, 0],
            [0, c, -s],
            [0, s, c]]

# Proof that 3d-rotation-matrix that apply twice equals one apply with twice the 3d-rotation-value

vec3 = [[1.0],
        [0.0],
        [0.0]]

rot3 = (degree_to_radian(0.0),
        degree_to_radian(30.0),
        degree_to_radian(30.0))

print_matrix(vec3, 4)
print(rot3)

x_matrix = x_rot(rot3[0])
y_matrix = y_rot(rot3[1])
z_matrix = z_rot(rot3[2])

print()
step1 = matmul(z_matrix, vec3)
if step1:
    step2 = matmul(x_matrix, step1)
    if step2:
        front = matmul(y_matrix, step2)
        print_matrix(front, 4)

rot3 = (degree_to_radian(0.0),
        degree_to_radian(15.0),
        degree_to_radian(15.0))

x_matrix = x_rot(rot3[0])
y_matrix = y_rot(rot3[1])
z_matrix = z_rot(rot3[2])

step1 = matmul(z_matrix, vec3)
step2 = matmul(x_matrix, step1)
front = matmul(y_matrix, step2)
print()
print_matrix(front, 4)
print()
step1 = matmul(z_matrix, front)
if step1:
    step2 = matmul(x_matrix, step1)
    if step2:
        front = matmul(y_matrix, step2)
        print_matrix(front, 4)
