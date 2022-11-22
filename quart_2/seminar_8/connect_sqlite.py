import sqlite3 as sl
from sqlite3 import Error

path = 'bd.sqlite'


def create():
    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    create_users_table = """
    CREATE TABLE IF NOT EXISTS USERS (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      gender TEXT
    );
    """

    with connection:
        connection.execute(create_users_table)
        print(f'{"*" * 50}\n\tТАБЛИЦА В БД СОЗДАНА')


def generation_users():
    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    sql = 'INSERT INTO USERS (name, age, gender) values(?, ?, ?)'
    data = [
        ('Алиса', 21, 'female'),
        ('Bob', 22, 'male'),
        ('Chris', 23, 'male')
    ]

    with connection:
        connection.executemany(sql, data)
        print(f'{"*" * 50}\n\tДАННЫЕ ДОБАВЛЕНЫ')


def view_users():
    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        data = connection.execute("SELECT * FROM USERS")
        cur = connection.cursor()
        exist = cur.fetchone()
        if exist is None:
            print(f'{"*" * 50}\n\tПРОСМОТР СОТРУДНИКОВ')
            for row in data:
                print(row)
        else:
            print('БД не содержит записей.')


def add_user():
    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        print(f'{"*" * 50}\n\tДОБАВЛЕНИЕ СОТРУДНИКА')
        name = input('Имя: ')
        age = input('Возраст: ')
        gender = input('Пол: ')
        connection.execute(f"INSERT INTO USERS (NAME, AGE, GENDER) VALUES('{name}', '{age}', '{gender}')")

    print('Данные добавлены.')
    view_users()


def edit_user():

    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        print(f'{"*" * 50}\n\tРЕДАКТИРОВАНИЕ ИНФОРМАЦИИ О СОТРУДНИКЕ')
        user_id = int(input('Введите ID сотрудника для редактирования: '))

        data = connection.execute(f"SELECT * FROM USERS WHERE ID = {user_id}")
        for row in data:
            if len(row) == 0:
                print('В базе данных не найдено.')
            else:
                print(f'Данные сотрудника с ID = {user_id}:\n{row}')

                choice = str(input(
                    f'\t\tЧто желаете изменить?\n'
                    '\t1. Имя\n'
                    '\t2. Возраст\n'
                    '\t3. Пол\n'
                    '\tВведите номер действия и нажмите Enter: '))

                if choice == '1':
                    new_name = str(input('Отредактируйте имя и нажмите Enter: '))
                    connection.execute(f"UPDATE USERS SET NAME = '{new_name}' WHERE ID = '{user_id}'")
                elif choice == '2':
                    new_age = str(input('Отредактируйте возраст и нажмите Enter: '))
                    connection.execute(f"UPDATE USERS SET AGE = '{new_age}' WHERE ID = '{user_id}'")
                elif choice == '3':
                    new_gender = str(input('Отредактируйте пол и нажмите Enter: '))
                    connection.execute(f"UPDATE USERS SET GENDER = '{new_gender}' WHERE ID = '{user_id}'")
                else:
                    print('Что-то пошло не так. Повторите ввод!')

        data = connection.execute(f"SELECT * FROM USERS WHERE ID = {user_id}")
        for row in data:
            print(f'Данные сотрудника с ID = {user_id}:\n{row}')


def delete_user():
    print(f'{"*" * 50}\n\tУДАЛЕНИЕ СОТРУДНИКА ИЗ БД')
    user_id = int(input('Введите ID сотрудника для удаления: '))

    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        connection.execute(f"DELETE FROM USERS WHERE ID = {user_id}")

        print(f'Сотрудник с ID={user_id} удален из базы данных.')


def delete_all():
    connection = None
    try:
        connection = sl.connect(path)
        print("Подключение к базе данных SQLite прошло успешно.")

    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        print(f'{"*" * 50}\n\tОЧИСТКА БД')
        connection.execute("DELETE FROM USERS")

    view_users()
