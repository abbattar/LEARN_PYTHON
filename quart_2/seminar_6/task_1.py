# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

# решение с eval
# print(f"Результат: {str(eval(input('Введите выражение: ')))}")

# решение с встроенными в python модулями functools м operator
# @ilyagrigoryev telegram-канал https://t.me/pymentor
import re
from functools import reduce
import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

brackets_regex = r"\([^()]+?\)"


def calculate(s):
    tokens = s.strip("() ").split()
    operation = operations[tokens[0]]
    operands = [float(t) for t in tokens[1:]]
    return reduce(operation, operands)


def resolve(s):
    match = re.search(brackets_regex, s)
    while match:
        expression = s[match.span()[0]:match.span()[1]]
        result = calculate(expression)
        s = s.replace(expression, str(result))
        match = re.search(brackets_regex, s)
    return s


print(resolve("( + 1 2 3 )"))  # 1+2+3=6
print(resolve("( * 1 2 3 4 )"))  # 1*2*3*4=24
print(resolve("( + ( * 2 2 ) ( / 6 2 ))"))  # (2*2)+(6/2)=7
