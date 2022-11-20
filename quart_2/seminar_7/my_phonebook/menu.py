import csv_action as ca
import sys


def menu():
    choice = str(input(
        f'{"*" * 50}\n'
        '\t\tСПИСОК ДЕЙСТВИЙ:\n'
        '\t1. Показать все контакты\n'
        '\t2. Сгенерировать контакты\n'
        '\t3. Добавить контакт\n'
        '\t4. Удалить все контакты\n'
        '\t5. Закрыть программу\n'
        f'{"*" * 50}\n'
        '\tВведите номер действия и нажмите Enter: '))

    if choice == '1':
        ca.view_csv()
    elif choice == '2':
        ca.generate_fake_contact()
    elif choice == '3':
        ca.add_new_contact()
    elif choice == '4':
        ca.delete_all()
    elif choice == '5':
        sys.exit('Программа закрыта. Всего доброго!')
    else:
        print('Что-то пошло не так. Повторите ввод!')
