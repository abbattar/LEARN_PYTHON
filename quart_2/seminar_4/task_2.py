# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
import math

num = int(input('Введите натуральное число: '))
start_num = num

list_multiplier = []
while num % 2 == 0:  # пока num кратен 2, в цикле делим на 2 и печатаем 2
    list_multiplier.append(2)
    num /= 2
    print(num)

for i in range(3, int(math.sqrt(num)) + 1, 2):
    while num % i == 0:  # пока num кратен i, в цикле делим на i и печатаем i
        list_multiplier.append(i)
        num /= i
        print(num)

if num > 2: list_multiplier.append(int(num))

print(f'Список простых множителей числа {start_num}: {list_multiplier}')
