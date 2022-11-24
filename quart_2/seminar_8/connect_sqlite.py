import datetime
import sqlite3 as sl
import logger as lg
import csv
import db_action
# from dateutil.parser import parse   # pip install python-dateutil
# import sys
# import os

path = 'phonebook.csv'
con = sl.connect('./phonebook.db')
cur = con.cursor()
# print(type(cur))

def initial():
    global con
    global cur

def db_connect():

    try:
        con
    except sl.Error as e:
        print(f'Произошла ошибка: {e}')
        con.close()

def create():
    lg.logging.info('Cоздание таблицы в бд')
    db_connect()

    create_users_table = """
    CREATE TABLE IF NOT EXISTS USERS (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      surname TEXT NOT NULL,
      birthday DATE NOT NULL,
      workplace TEXT NOT NULL,
      phonenum INTEGER,
    )
    """

    with con:
        con.execute(create_users_table)

    con.commit()

    print(f'{"*" * 50}\n\tТАБЛИЦА В БД СОЗДАНА')


def generation_users():

    lg.logging.info('Генерация пользователей')
    db_connect()
    cur.execute("""CREATE TABLE IF NOT EXISTS USERS
    ( id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      surname TEXT NOT NULL,
      birthday DATE NOT NULL,
      workplace TEXT NOT NULL,
      phonenum INTEGER,
    )""")

    db_action.generate_fake_contact()

    with open(path,'a', encoding="utf8") as phone:
        dr = csv.reader(phone, delimiter=";")
        to_db = [(i['ID'], i['ИМЯ'], i['ФАМИЛИЯ'],
                   i['ДАТА РОЖДЕНИЯ'], i['МЕСТО РАБОТЫ'], i['НОМЕРА ТЕЛЕФОНОВ']) for i in dr]
    cur.executemany("INSERT INTO t (ID, name, surname, birthday, workplace, phonenum) VALUES (?, ?, ?, ?, ?, ?);", to_db)

    con.commit()

    print(f'{"*" * 50}\n\tДАННЫЕ ДОБАВЛЕНЫ')
    
    con.close()


def view_users():
    lg.logging.info('просмотр юзеров')

    print(f'{"*" * 50}\n\tПРОСМОТР СОТРУДНИКОВ:')

    db_connect()

    with con:
        data = con.execute("SELECT * FROM ID")

    for row in data:
        print(row)

    con.close()

# def birth_date():
#     try:
#         value = parse(input('День рожденья: '))
#     except ValueError:
#         sys.exit('Пиши нормальное представление даты: ГГ-ММ-ДД')
        
#     return value


def add_user():
    lg.logging.info('добавление юзера')
    
    db_connect()
    dr = datetime()
    
    print(f'{"*" * 50}\n\tДОБАВЛЕНИЕ СОТРУДНИКА')
    id_user = int(input('Идентификационный номер: '))
    name = input('Имя: ')
    surname = input('Фамилия: ')
    workplace = input('Место работы: ')
    birthday = str(input(f'ДР: {dr}'))
    phonenum = int(input('Номер телефона: '))

    with con:
        con.execute(f"INSERT INTO USERS (ID, NAME, SURNAME, BIRTHDAY, WORKPLACE, PHONENUM) VALUES('{id_user}', '{name}', '{surname}', '{birthday}, '{workplace}', '{phonenum}')")

    con.commit()

    print('Данные добавлены.')
    
    con.close()


def edit_user():
    lg.logging.info('редактирование юзера')

    db_connect()

    print(f'{"*" * 50}\n\tРЕДАКТИРОВАНИЕ ИНФОРМАЦИИ О СОТРУДНИКЕ')
    user_id = int(input('Введите ID сотрудника для редактирования: '))

    with con:
        data = con.execute(f"SELECT * FROM USERS WHERE ID = {user_id}")

    for row in data:
        print(f'Данные сотрудника с ID = {user_id}:\n{row}')
        choice = str(input(
            f'\t\tЧто желаете изменить?\n'
            '\t1. Имя\n'
            '\t2. Фамилию\n'
            '\t3. День рождения\n'
            '\t4. Место работы\n'
            '\t5. Телефоны\n'
            '\tВведите номер действия и нажмите Enter: '))
        match choice:
            case '1':
                new_name = str(input('Отредактируйте имя и нажмите [Enter]: '))
                con.execute(f"UPDATE USERS SET NAME = '{new_name}' WHERE ID = '{user_id}'")
            case '2':
                new_surname = str(input('Отредактируйте Фамилию [Enter]: '))
                con.execute(f"UPDATE USERS SET SURNAME = '{new_surname}' WHERE ID = '{user_id}'")
            case '3':
                new_birthday = str(input('Отредактируйте телефон [Enter]: '))
                con.execute(f"UPDATE USERS SET BIRTHDAY = '{new_birthday}' WHERE ID = '{user_id}'")
            case '4':
                new_workplace = str(input('Отредактируйте место работы [Enter]: '))
                con.execute(f"UPDATE USERS SET WORKPLACE = '{new_workplace}' WHERE ID = '{user_id}'")
            case '5':
                new_phonenum = str(input('Отредактируйте телефон [Enter]: '))
                con.execute(f"UPDATE USERS SET PONENUM = '{new_phonenum}' WHERE ID = '{user_id}'")
            case _:
                print('Что-то пошло не так. Повторите ввод!')

    con.commit()

    data = con.execute(f"SELECT * FROM USERS WHERE ID = {user_id}")
    for row in data:
        print(f'Данные сотрудника с ID = {user_id}:\n{row}')
    
    con.close()


def delete_user():
    lg.logging.info('удаление юзера')

    print(f'{"*" * 50}\n\tУДАЛЕНИЕ СОТРУДНИКА ИЗ БД')
    user_id = int(input('Введите ID сотрудника для удаления: '))

    db_connect()

    with con:
        con.execute(f"DELETE FROM USERS WHERE ID = {user_id}")

    con.commit()

    print(f'Сотрудник с ID={user_id} удален из базы данных.')
    con.close()


def delete_all():
    lg.logging.info('удаление всех юзеров')
    print(f'{"*" * 50}\n\tОЧИСТКА БД')

    db_connect()

    with con:
        con.execute("DELETE FROM USERS")

    con.commit()
    con.close()