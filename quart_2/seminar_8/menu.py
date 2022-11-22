import connect_sqlite as conn
import sys


def menu():
    choice = str(input(
        f'{"*" * 50}\n'
        '\t\tСПИСОК ДЕЙСТВИЙ:\n'
        '\t1. Показать всех сотрудников\n'
        '\t2. Создать пустую БД\n'
        '\t3. Добавить сотрудников\n'
        '\t4. Отредактировать сотрудника\n'
        '\t5. Удалить сотрудника\n'
        '\t6. Очистить БД\n'
        '\t7. Закрыть программу\n'
        f'{"*" * 50}\n'
        '\tВведите номер действия и нажмите Enter: '))

    if choice == '1':
        conn.view_users()  # СДЕЛАНО
    elif choice == '2':
        conn.create()  # СДЕЛАНО
    elif choice == '3':
        conn.add_user()  # СДЕЛАНО
    elif choice == '4':
        conn.edit_user()  # это надо сделать
    elif choice == '5':
        conn.delete_user()  # СДЕЛАНО
    elif choice == '6':
        conn.delete_all()  # СДЕЛАНО
    elif choice == '7':
        sys.exit('Программа закрыта. Всего доброго!')
    else:
        print('Что-то пошло не так. Повторите ввод!')
