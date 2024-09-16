import numpy as np
from stl import mesh
from collections import defaultdict

# Загрузка модели STL
your_mesh = mesh.Mesh.from_file('models/cat-2.stl')

# Функция для получения рёбер треугольника в виде кортежей
def get_edges(triangle):
    p1, p2, p3 = triangle
    return [(tuple(sorted((tuple(p1), tuple(p2)))), 
             tuple(sorted((tuple(p2), tuple(p3)))), 
             tuple(sorted((tuple(p3), tuple(p1)))))]

# Инициализируем словарь для подсчета количества рёбер
edges_count = defaultdict(int)

# Проходим по всем треугольникам модели и собираем рёбра
for triangle in your_mesh.vectors:
    edges = get_edges(triangle)
    for edge in edges[0]:
        edges_count[edge] += 1

# Проверка, что каждое ребро встречается ровно два раза
watertight = all(count == 2 for count in edges_count.values())

if watertight:
    print("Модель является watertight (замкнутой).")
else:
    print("Модель НЕ является watertight (имеет отверстия).")