import math

import matplotlib.pyplot as plt
import numpy as np

def merge_points(points, tolerance=20):
    dist = 0
    res = np.empty((0, 3))
    res = np.append(res, points[0].reshape((1, 3)), axis=0)
    # res = np.append(res, points[0], axis=0)
    
    for idx, _ in enumerate(points):
        if idx + 1 < len(points):
            dist += np.linalg.norm(points[idx] - points[idx + 1])
            if dist > tolerance:
                res = np.append(res, points[idx + 1].reshape((1, 3)), axis=0)
                dist = 0
    
    return res


# Входные данные
LEANING_ANGLE = 0 # угол положения
RADIUS = 70 # радиус
ROTCOUNT = 100 # число витков
FINENESS = 0.25 # шаг

# Расчёт вертикального и горизонтального углов
v_angle_unit = math.pi / RADIUS / 2
h_angle_unit = math.pi / RADIUS * ROTCOUNT * FINENESS

xr = LEANING_ANGLE / 180 * math .pi
xrc = math.cos(xr)
xrs = math.sin(xr)
points = []
total_rot = 0
flg = -1

# генерация точек кривой
i = -RADIUS
while i <= RADIUS :
    x = math.cos(i * v_angle_unit) * RADIUS
    y = math.sin(i * v_angle_unit) * RADIUS
    v = [x* math.cos(total_rot), y, x*math.sin(total_rot)]
    
    pnt_y = v[1]*xrc - v[2]*xrs
    pnt_z = v[2]*xrc + v[1]*xrs
    
    points.append ([v[0], pnt_y, pnt_z])
    total_rot += h_angle_unit
    
    i += FINENESS

# вывод графика
ax = plt.figure().add_subplot(projection='3d')
n = len(points)

X = np.zeros(n)
Y = np.zeros(n)
Z = np.zeros(n)

for i in range (n):
    for j in range (3):
        if j == 0:
            Z[i] = points[i][j]
        elif j == 1:
            Y[i] = points[i][j]
        else :
            X[i] = points[i][j]

points = np.array([X, Y, Z]).transpose()
points = merge_points(points)

X, Y, Z = points[:, 0], points[:, 1], points[:, 2]
ax.plot(X, Y, Z)

# Добавляем векторы нормалей в каждой n-й точке
for i in range(0, len(X), 1):
    # Вектор нормали направлен от центра сферы к точке на поверхности
    normal = np.array([X[i], Y[i], Z[i]])
    normal = normal / np.linalg.norm(normal)  # Нормализуем вектор нормали

    # Рисуем векторы нормалей
    ax.quiver(X[i], Y[i], Z[i], normal[0], normal[1], normal[2], color='g', length=10, normalize=True)

plt.show()

# процедура группировки координат
def make_path(points, group):
    if points.length > 0:
        if(points.length > 1):
            points = [points.pop(), points.pop()].reverse ()
        else:
            points = [points.pop()]
    return points