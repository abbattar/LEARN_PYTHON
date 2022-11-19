# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

num = int(input('Введите натуральное число: '))

list_numbers = []  # объявили список
sum = 0
elements = ''

for i in range(num):
    number_for_list = randint(-num, num)  # рандомное число из промежутка [-num, num]
    list_numbers.append(number_for_list)  # добавили рандомное число в список

    if i % 2 == 1:
        sum += number_for_list
        elements = elements + ', ' + str(number_for_list)

print(f'{list_numbers} -> на нечётных позициях элементы {elements[2:]}. Ответ: {sum}')
