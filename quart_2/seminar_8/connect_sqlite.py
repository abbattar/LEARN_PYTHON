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

    view_users()


def view_users():
    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        data = connection.execute("SELECT * FROM USERS")

    for row in data:
        print(row)


def add_user():
    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    sql = 'INSERT INTO USERS (id, name, age, gender) values(?, ?, ?, ?)'
    data = [
        ('1', 'Алиса', 21, 'female'),
        ('2', 'Bob', 22, 'male'),
        ('3', 'Chris', 23, 'male')
    ]

    with connection:
        connection.executemany(sql, data)
        print('Данные добавлены:')

    view_users()


def delete_user():
    user_id = int(input('Введите ID сотрудника для удаления: '))

    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        connection.execute(f"DELETE FROM USERS WHERE ID = {user_id}")

        print(f'Сотрудник с ID={user_id} удален из базы данных.')

    view_users()


def delete_all():
    connection = None
    try:
        connection = sl.connect(path)
        print("Подключение к базе данных SQLite прошло успешно.")

    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
        connection.execute("DELETE FROM USERS")

    view_users()


def edit_user():
    user_id = int(input('Введите ID сотрудника для редактирования: '))

    connection = None
    try:
        connection = sl.connect(path)
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    with connection:
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
            if len(row) == 0:
                print('В базе данных не найдено.')
            else:
                print(f'Данные сотрудника с ID = {user_id}:\n{row}')
