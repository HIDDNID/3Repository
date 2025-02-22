
import math


def triangle_area(a, b, c):
    # Вычисляем полупериметр
    s = (a + b + c) / 2

    # Используем формулу Герона
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


# Пример использования функции
side_a = 3
side_b = 4
side_c = 5

area = triangle_area(side_a, side_b, side_c)
print(f"Площадь треугольника со сторонами {side_a}, {side_b}, {side_c}: {area:.2f}")
