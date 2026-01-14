s = input("Введите строку: ")
total_symbols = len(s)
count_a = s.count('а')
s_replaced = s.replace('а', 'о')

print("Строка после замены:", s_replaced)
print("Количество замен:", count_a)
print("Количество символов в строке:", total_symbols)
