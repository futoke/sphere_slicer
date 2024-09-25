import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

# Задаем параметры спирали
r = 3  # Радиус
num_turns = 10
num_points = 10000


# Параметрическая функция спирали
def spiral(t):
    a_max = 2 * np.pi * num_turns
    a = a_max * t
    b = -np.pi/2 + (a * np.pi) / a_max
    x = (r / 2) * np.cos(a) * np.cos(b)
    y = (r / 2) * np.sin(a) * np.cos(b)
    z = -(r / 2) * np.sin(b)
    return np.array([x, y, z])


# Производные спирали
def spiral_derivative(t):
    h = 1e-5  # Шаг для численного дифференцирования
    return (spiral(t + h) - spiral(t)) / h


# Функция для расчета длины дуги
def arc_length(t):
    dx, dy, dz = spiral_derivative(t)
    return np.sqrt(dx**2 + dy**2 + dz**2)

# Общая длина спирали
total_length, _ = quad(arc_length, 0, 1)

# Целевая длина каждого отрезка
N = 50  # Количество отрезков
segment_length = total_length / N

# Поиск параметров t_i для разбиения
def find_t_for_segment(t_prev, target_length):
    def equation(t):
        segment, _ = quad(arc_length, t_prev, t)
        return segment - target_length
    t_next = fsolve(equation, t_prev + 0.01)
    return t_next[0]

# Нахождение точек разбиения
t_values = [0]
for i in range(1, N + 1):
    t_next = find_t_for_segment(t_values[-1], segment_length)
    t_values.append(t_next)

# Вычисление координат точек разбиения
points = np.array([spiral(t) for t in t_values])

# Визуализация спирали и точек разбиения
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = spiral(np.linspace(0, 1, num_points))

for point in points:
    # Вектор нормали направлен от центра сферы к точке на поверхности
    # normal = np.array([points[0], points[1], points[2]])
    normal = point / np.linalg.norm(point)  # Нормализуем вектор нормали
    
    # Рисуем векторы нормалей
    # ax.quiver(point[0], point[1], point[2], normal[0], normal[1], normal[2], color='g', length=0.5, normalize=True)

# Добавляем векторы нормалей в каждой n-й точке
# for i in range(0, len(x), int(segment_length)):
#     # Вектор нормали направлен от центра сферы к точке на поверхности
#     normal = np.array([x[i], y[i], z[i]])
#     normal = normal / np.linalg.norm(normal)  # Нормализуем вектор нормали
    
#     # Рисуем векторы нормалей
#     ax.quiver(x[i], y[i], z[i], normal[0], normal[1], normal[2], color='g', length=0.2, normalize=True)


ax.plot(x, y, z, label='Сферическая спираль')

# Отображение точек разбиения
# ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='r', label='Точки разбиения')

# Настройки графика
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
