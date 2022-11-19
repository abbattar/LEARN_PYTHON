# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# https://ru.wikipedia.org/wiki/Негафибоначчиn = int(input('Введите число: '))

k = int(input('Введите целое число > 2: '))
if k > 2:
    negafibo_list = [-1, 1, 0, 1, 1]

    for _ in range(3, k+1):
        negafibo_list.append(negafibo_list[-2] + negafibo_list[-1])
        negafibo_list.insert(0, negafibo_list[1] - negafibo_list[0])

    print(negafibo_list)

else:
    print('Введены некорректные данные!')
