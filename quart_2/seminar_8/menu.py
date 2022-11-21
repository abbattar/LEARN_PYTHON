import connect_sqlite as conn
import sys

conn.create()


def menu():
    choice = str(input(
        f'{"*" * 50}\n'
        '\t\tСПИСОК ДЕЙСТВИЙ:\n'
        '\t1. Показать всех сотрудников\n'
        '\t2. Создать пустые таблицы\n'
        '\t3. Добавить оотрудника\n'
        '\t4. Отредактировать оотрудника\n'
        '\t5. Удалить сотрудника\n'
        '\t6. Удалить всех сотрудников\n'
        '\t7. Закрыть программу\n'
        f'{"*" * 50}\n'
        '\tВведите номер действия и нажмите Enter: '))

    if choice == '1':
        conn.view_database() # это надо сделать
    elif choice == '2':
        conn.create()  # пока готово только создание таблицы
    elif choice == '3':
        conn.add_new_contact() # это надо сделать
    elif choice == '4':
        conn.edit_contact() # это надо сделать
    elif choice == '5':
        conn.delete_contact() # это надо сделать
    elif choice == '6':
        conn.delete_all()# это надо сделать
    elif choice == '7':
        sys.exit('Программа закрыта. Всего доброго!')
    else:
        print('Что-то пошло не так. Повторите ввод!')
