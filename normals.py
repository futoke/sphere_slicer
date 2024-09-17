import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Задаем параметры спирали
r = 1  # Радиус
num_turns = 10
num_points = 10000
normal_step = 100


# Параметрическая функция спирали
def create_helix(t):
    a_max = 2 * np.pi * num_turns
    a = a_max * t
    b = -np.pi/2 + (a * np.pi) / a_max
    x = (r / 2) * np.cos(a) * np.cos(b)
    y = (r / 2) * np.sin(a) * np.cos(b)
    z = -(r / 2) * np.sin(b)
    return np.array([x, y, z])

x, y, z = create_helix(np.linspace(0, 1, num_points))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Добавляем векторы нормалей в каждой n-й точке
for i in range(0, len(x), normal_step):
    # Вектор нормали направлен от центра сферы к точке на поверхности
    normal = np.array([x[i], y[i], z[i]])
    normal = normal / np.linalg.norm(normal)  # Нормализуем вектор нормали
    print(normal)
    
    # Рисуем векторы нормалей
    ax.quiver(x[i], y[i], z[i], normal[0], normal[1], normal[2], color='g', length=0.2, normalize=True)

# Визуализация спирали и точек разбиения
ax.plot(x, y, z, label='Сферическая спираль')

plt.show()