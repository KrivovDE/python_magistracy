arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

odd_numbers = []
for num in arr:
    if num % 2 != 0:  # Проверка на нечетность
        odd_numbers.append(num)

if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Массив нечетных чисел в порядке убывания:", odd_numbers)
else:
    print("Нечетных чисел в исходном массиве нет")
