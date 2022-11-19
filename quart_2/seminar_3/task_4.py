# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input('Введите десятичное число: '))

binary_number = ''

while decimal_number > 0:
    binary_number = str(decimal_number % 2) + binary_number  # дописываем в начало строки
    decimal_number //= 2

print(f'{int(binary_number, 2)} -> {binary_number}')  # исходное число вывели функцией int()
