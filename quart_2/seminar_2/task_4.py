# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint  # импортировали модуль

with open('file.txt', 'r') as file:  # работа с файлом
    data = [row.strip() for row in file]  # создали массив из строк файла file.txt
    number_of_rows = len(data)  # посчитали количество строк в файле

N = int(input(f'Введите целое число в диапазоне от 1 до {number_of_rows}: '))

if 0 < N <= number_of_rows:  # проверка числа на соответствие требованиям
    numbers = []  # объявили список
    for _ in range(N):
        numbers.append(randint(-N, N))  # заполнили список рандомными числами из промежутка [-N, N]
    print(numbers)  # вывели список индексов, начиная с 0

    multi = 1

    for i in numbers:  # цикл индексов в file.txt. они могут быть отрицательными (начало с конца массива).
        print(i, end=' -> ')  # вывели индекс (элементы с этим индексом будем искать в file.txt).
        if i == number_of_rows:
            print(f'1 (Элемента с индексом {number_of_rows} нет в file.txt. Присвоим элементу значение = 1 для умножения)')
            multi *= 1
        else:
            data_element = data[i]
            print(data_element)  # вывели элемент на этой позиции в file.txt.
            multi *= int(data_element)  # умножаем значение на текущий элемент списка

    print(f'Произведение элементов: {multi}')
else:
    print('Некорректный ввод данных!')
