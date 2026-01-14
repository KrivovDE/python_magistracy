import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))

# Вычисление выражения s = |cos x - cos y|^(1 + 2*sin^2 y) * (1 + z + z^2/2 + z^3/3 + z^4/4)
numerator = math.fabs(math.cos(x) - math.cos(y))
power = 1 + 2 * (math.sin(y) ** 2)
polynomial = 1 + z + (z**2)/2 + (z**3)/3 + (z**4)/4

s = math.pow(numerator, power) * polynomial

print("s ", s)