import connect_sqlite as conn
import logger as lg
import sys


def run():
    while True:
        menu()


def menu():
    choice = str(input(
        f'{"*" * 50}\n'
        '\t\tСПИСОК ДЕЙСТВИЙ:\n'
        '\t1. Создать пустую БД\n'
        '\t2. Сгенерировать сотрудников\n'
        '\t3. Показать всех сотрудников\n'
        '\t4. Добавить сотрудника\n'
        '\t5. Отредактировать сотрудника\n'
        '\t6. Удалить сотрудника\n'
        '\t7. Очистить БД\n'
        '\t8. Закрыть программу\n'
        f'{"*" * 50}\n'
        '\tВведите номер действия и нажмите Enter: ')
    # match choise:
        # case '1':
    if choice == '1':
        conn.create()
        # case '2':
    elif choice == '2':
        conn.generation_users()
        # case '3':
    elif choice == '3':
        conn.view_users()
        # case '4':
    elif choice == '4':
        conn.add_user()
        # case '5':
    elif choice == '5':
        conn.edit_user()
        # case '6':
    elif choice == '6':
        conn.delete_user()
        # case '7':
    elif choice == '7':
        conn.delete_all()
        # case '8':
    elif choice == '8':
        lg.logging.info('Программа закрыта. Всего ВАМ ДО! БРО! ГО! )))')
        sys.exit('Программа закрыта. Всего ВАМ ДО! БРО! ГО! )))')
        # case _:
    else:
        print('Что-то пошло не так. Повторите ввод!')
