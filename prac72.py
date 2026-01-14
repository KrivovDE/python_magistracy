def check_point_in_circle(px, py, a, b, r):
    return (px - a) ** 2 + (py - b) ** 2 < r ** 2

a = float(input("Введите a: "))
b = float(input("Введите b: "))
r = float(input("Введите R: "))

p1 = float(input("Введите p1: "))
p2 = float(input("Введите p2: "))
f1 = float(input("Введите f1: "))
f2 = float(input("Введите f2: "))
l1 = float(input("Введите l1: "))
l2 = float(input("Введите l2: "))

points = [(p1, p2, 'P'), (f1, f2, 'F'), (l1, l2, 'L')]
inside_count = 0

for x, y, name in points:
    if check_point_in_circle(x, y, a, b, r):
        print(f"Точка {name} лежит внутри окружности.")
        inside_count += 1
    else:
        print(f"Точка {name} не лежит внутри окружности.")

print(f"Количество точек внутри окружности: {inside_count}")