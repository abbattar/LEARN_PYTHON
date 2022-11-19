# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

num = int(input('Введите натуральное число: '))

if num % 2 == 0:  # вычисляем количество элементов в списке с произведением чисел
    quantity_elements_in_second_list = int(num / 2)
else:
    quantity_elements_in_second_list = int(num / 2) + 1

if num > 0:  # проверка числа на соответствие требованиям

    list_numbers = []  # объявили список чисел
    for i in range(num):  # Получаем сгенерированный список из рандомных num чисел
        number_for_list = randint(1, num)  # рандомное число в диапазоне от 1 до num
        list_numbers.append(number_for_list)  # добавили рандомное число в список

    list_multi = []  # объявили список для произведений чисел
    for i in range(quantity_elements_in_second_list):  # Получаем список с произведением чисел
        multi = list_numbers[i] * list_numbers[-(i + 1)]
        list_multi.append(multi)  # добавили произведение в список

    print(f'{list_numbers} => {list_multi}')

else:
    print('Введены некорректные данные!')
