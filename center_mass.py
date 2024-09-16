import numpy as np
from stl import mesh

# Загрузка модели STL
your_mesh = mesh.Mesh.from_file('models/cat-2.stl')

# Инициализация переменных для расчета центра масс
total_area = 0
center_of_mass = np.zeros(3)

# Функция для вычисления площади треугольника
def triangle_area(p1, p2, p3):
    return 0.5 * np.linalg.norm(np.cross(p2 - p1, p3 - p1))

# Проходим по каждому треугольнику модели
for triangle in your_mesh.vectors:
    p1, p2, p3 = triangle[0], triangle[1], triangle[2]
    area = triangle_area(p1, p2, p3)  # Площадь треугольника
    centroid = (p1 + p2 + p3) / 3  # Центр масс треугольника
    
    # Взвешиваем центр масс по площади треугольника
    center_of_mass += area * centroid
    total_area += area

# Расчет геометрического центра (центра масс) модели
center_of_mass /= total_area

print(f'Геометрический центр модели (центр масс): {center_of_mass}')
