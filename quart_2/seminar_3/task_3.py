# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

import random

num = 5  # num = int(input('Введите натуральное число: '))

list_float_numbers = []  # объявили список для вещественных чисел
max_data = 0
min_data = 1

for _ in range(num):  # Получаем сгенерированный список из рандомных num чисел
    number_for_list = round(random.uniform(0, 100), 2)
    list_float_numbers.append(number_for_list)  # добавили вещественное число число в список

    number_for_list = str(number_for_list).split('.')  # разрезали вещественное число по точке
    finish_number = float('0.' + number_for_list[1])  # взяли часть после точки

    if finish_number > max_data: max_data = finish_number
    if finish_number < min_data: min_data = finish_number

difference = round(max_data - min_data, 2)
print(f'{list_float_numbers} => {difference}')
