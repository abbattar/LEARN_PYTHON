import sqlite3 as sl
from sqlite3 import Error

path = 'bd.sqlite'


def connect():
    pass


def create():  # создаем пустую базу

    connection = None

    try:
        connection = sl.connect(path)
        print("Подключение к базе данных SQLite прошло успешно.")

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

    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts(
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      title TEXT NOT NULL, 
      description TEXT NOT NULL, 
      user_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      text TEXT NOT NULL, 
      user_id INTEGER NOT NULL, 
      post_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
    );
    """

    create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      user_id INTEGER NOT NULL, 
      post_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
    );
    """

    with connection:
        connection.execute(create_users_table)
        connection.execute(create_posts_table)
        connection.execute(create_comments_table)
        connection.execute(create_likes_table)

    print('Пустые таблицы созданы.')


def view_users():
    connection = None

    try:
        connection = sl.connect(path)
        print("Подключение к базе данных SQLite прошло успешно.")

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
        print("Подключение к базе данных SQLite прошло успешно.")

    except Error as e:
        print(f"Произошла ошибка '{e}'")

    sql = 'INSERT INTO USERS (id, name, age, gender) values(?, ?, ?, ?)'
    data = [
        (1, 'Алиса', 21, 'female'),
        (2, 'Bob', 22, 'male'),
        (3, 'Chris', 23, 'male')
    ]

    with connection:
        connection.executemany(sql, data)

    print('Данные добавлены.')
