import math

diameter = float(input("Введите диаметр окружности: "))
radius = diameter / 2
area = math.pi * (radius ** 2)

perimeter = math.pi * diameter

print(f"Площадь окружности:", area)
print(f"Периметр окружности:", perimeter)