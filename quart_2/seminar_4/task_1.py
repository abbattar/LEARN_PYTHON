# 1. Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤ 10^(-10)

from math import pi

d =  float(input("Введите число для заданной точности числа π: "))

count_after_dot = len(str(d).split('.')[1])

print(f'при = {d}, π = {round(pi, count_after_dot)}')
