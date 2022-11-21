import sqlite3 as sl
from sqlite3 import Error

path = 'bd.sqlite'


def create():
    connection = None

    try:
        connection = sl.connect(path)
        print("Подключение к базе данных SQLite прошло успешно")

    except Error as e:
        print(f"Произошла ошибка '{e}'")

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      gender TEXT,
      nationality TEXT
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


create()
