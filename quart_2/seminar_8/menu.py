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
        '\t8. Сгенерировать БД\n'
        '\t9. Закрыть программу\n'
        f'{"*" * 50}\n'
        '\tВведите номер действия и нажмите Enter: '))
    match choice:
        case '1':
            conn.create()
        case '2':
            conn.generation_users()
        case '3':
            conn.view_users()
        case '4':
            conn.add_user()
        case '5':
            conn.edit_user()
        case '6':
            conn.delete_user()
        case '7':
            conn.delete_all()
        case '8':
            conn.generation_users()
        case '9':
            lg.logging.info('Программа закрыта.')
            sys.exit('Программа закрыта.')
        case _:
            print('Что-то пошло не так. Повторите ввод!')
