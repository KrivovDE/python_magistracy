N = int(input("\nВведите размер квадратной матрицы N: "))
A = []
for i in range(N):
    row = list(map(int, input(f"Введите {N} элементов {i+1}-й строки через пробел: ").split()))
    A.append(row)

for i in range(N):
    for j in range(N):
        if A[i][j] < 0:
            A[i][j] = 0
        elif A[i][j] > 0:
            A[i][j] = 1

print("\nНижняя треугольная матрица:")
for i in range(N):
    for j in range(i + 1):
        print(A[i][j], end=' ')
    print()