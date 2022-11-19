# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

numbers_list = [1, 2, 3, 5, 1, 5, 3, 10]

list_uniq = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
list_no_uniq = list(set(filter(lambda a: numbers_list.count(a) > 1, numbers_list)))
list_no_duplicates = list(set(numbers_list))

print(list_uniq, list_no_uniq, list_no_duplicates, sep='\n')
