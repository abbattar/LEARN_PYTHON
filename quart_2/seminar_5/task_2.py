# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# man vs smart bot
import random
from random import randint, choice

print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока\n'
    'Первый ход определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры\n'
    'У нас есть некоторое количество конфет\n'
    'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
    'Тот, кому достанется последняя конфета - проиграл\n'
)

messages = ['ваш ход брать конфеты', 'возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'ваш ход']
max_number_move = 0


def introduce_players():
    player1 = input('Первый игрок, представьтесь: ')
    player2 = 'Cool_Bot'
    print(f'{player1}, сегодня Вы играете с роботом {player2}')
    return [player1, player2]


def sweets_game(players):
    global max_number_move
    total_sweets = int(input('Введите cколько всего у нас конфет: '))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет - любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_sweets, max_number_move, int(first)]


max_move = max_number_move


def game_player_vs_smart_bot(sweets, players, messages):
    global max_number_move
    count = sweets[2]

    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] - 1
            print(f'Я забираю {move}')

        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'{player2} забирает {move}.')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


players = introduce_players()
sweets = sweets_game(players)

winner = game_player_vs_smart_bot(sweets, players, messages)
if not winner:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winner}! Ему достаются все конфеты!')
