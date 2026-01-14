with open("DMO_группа_vvod.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

# Задание 1: Прямоугольная матрица
lines = [line.strip() for line in data if line.strip()]
current_line = 0
m, n = map(int, lines[current_line].split())
current_line += 1

matrix = []
for _ in range(m):
    matrix.append(list(map(int, lines[current_line].split())))
    current_line += 1
max_sum = float('-inf')
min_sum = float('inf')
max_row_index = -1
min_row_index = -1

for i in range(m):
    row_sum = sum(matrix[i])
    if row_sum > max_sum:
        max_sum = row_sum
        max_row_index = i
    if row_sum < min_sum:
        min_sum = row_sum
        min_row_index = i

# Задание 2: Квадратная матрица
N = int(lines[current_line].strip())
current_line += 1
A = []
for _ in range(N):
    A.append(list(map(int, lines[current_line].split())))
    current_line += 1

for i in range(N):
    for j in range(N):
        if A[i][j] < 0:
            A[i][j] = 0
        elif A[i][j] > 0:
            A[i][j] = 1
with open("DMO_группа_vivod.txt", "w", encoding="utf-8") as file:
    file.write("Результаты:\n\n")

    file.write("1. Прямоугольная матрица:\n")
    for row in matrix:
        file.write(" ".join(map(str, row)) + "\n")

    file.write(f"\nСтрока с наибольшей суммой (индекс {max_row_index}): {matrix[max_row_index]}\n")
    file.write(f"Сумма элементов: {max_sum}\n")

    file.write(f"\nСтрока с наименьшей суммой (индекс {min_row_index}): {matrix[min_row_index]}\n")
    file.write(f"Сумма элементов: {min_sum}\n")

    file.write("\n\n2. Квадратная матрица после преобразования:\n")
    for row in A:
        file.write(" ".join(map(str, row)) + "\n")

    file.write("\nНижняя треугольная матрица:\n")
    for i in range(N):
        for j in range(i + 1):
            file.write(f"{A[i][j]} ")
        file.write("\n")

print("Результаты записаны в файл DMO_группа_vivod.txt")
