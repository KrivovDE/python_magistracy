m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = []
for i in range(m):
    row = list(map(int, input(f"Введите {n} элементов {i+1}-й строки через пробел: ").split()))
    matrix.append(row)

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

print("\nСтрока с наибольшей суммой элементов:")
print(f"Строка {max_row_index + 1}: {matrix[max_row_index]}, Сумма = {max_sum}")

print("\nСтрока с наименьшей суммой элементов:")
print(f"Строка {min_row_index + 1}: {matrix[min_row_index]}, Сумма = {min_sum}")