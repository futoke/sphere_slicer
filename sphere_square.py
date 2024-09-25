import numpy as np
import matplotlib.pyplot as plt

# Функция для расчета площади второй сферы через площадь первой
def sphere_area_ratio(S1, R1, l):
    return S1 * (1 + 2 * l / R1 + (l / R1)**2)

# Задаем параметры
S1 = 12.566  # Площадь первой сферы (пример, для радиуса 1, так как S = 4*pi*1^2)
R1 = 1  # Радиус первой сферы
l_values = np.linspace(-0.9, 2, 400)  # Разница в радиусах (l), от -0.9 до 2 (допустим l > -R1)

# Рассчитываем площади второй сферы
S2_values = sphere_area_ratio(S1, R1, l_values)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(l_values, S2_values, label='S2 через S1')
plt.xlabel('Разница в радиусах (l), мм')
plt.ylabel('Площадь второй сферы (S2)')
plt.title('Зависимость площади второй сферы от разницы радиусов (l)')
plt.grid(True)
plt.legend()
plt.show()