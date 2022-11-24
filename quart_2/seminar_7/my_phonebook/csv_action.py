import os
import random
from random import randint
import menu

path = 'phonebook.csv'

def counter_lines():
    with open(path, 'r', encoding='utf-8') as f:
        return str(len(f.readlines()))


def generate_fake_contact():
    print('*' * 35)
    print('\tГЕНЕРАЦИЯ КОНТАКТОВ ДЛЯ ОЗНАКОМЛЕНИЯ С ПРОГРАММОЙ')
    import datetime

    for _ in range(30):
        name = random.choice(open(r'fake_data\names.txt', encoding='utf-8').readlines()).strip()
        surname = random.choice(open(r'fake_data\surnames.txt', encoding='utf-8').readlines()).strip()
        birthday = datetime.date(randint(1950, 2000), randint(1, 12), randint(1, 28)).strftime("%d.%m.%Y")
        work = random.choice(open(r'fake_data\companies.txt', encoding='utf-8').readlines()).strip()
        phonenum = '+' + str(random.randint(79000000000, 80000000000))
        u_data = [name, surname, birthday, work, phonenum]

        with open(path, 'a', encoding='utf-8') as f:
            line = ';'.join(u_data)
            f.write(counter_lines() + ';' + line + '\n')

    print('Сгенерировано 30 фейковых аккаунтов.')

def add_new_contact():
    print('*' * 35)
    print('\tДОБАВЛЕНИЕ НОВОГО КОНТАКТА')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birthday = input('Дата рождения: ')
    work = input('Место работы: ')
    phonenum = input('Введите номер телефона. Если номеров несколько - разделяйте их запятыми: ')
    u_data = [name, surname, birthday, work, phonenum]

    with open(path, 'a', encoding='utf-8') as f:
        line = ';'.join(u_data)
        f.write(counter_lines() + ';' + line + '\n')
        print('*' * 35)

    print('Новый контакт добавлен в справочник.')


def view_csv():
    print('*' * 35)
    if os.path.isfile(path):
        print('\tПРОСМОТР ВСЕХ КОНТАКТОВ')
        if int(counter_lines()) < 2:
            print('В справочнике нет контактов.')
        else:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    print(line, end='')
    else:
        print('В справочнике нет контактов.')
        book_title()


def book_title():
    u_data = ['ID', 'ИМЯ', 'ФАМИЛИЯ', 'ДАТА РОЖДЕНИЯ', 'МЕСТО РАБОТЫ', 'НОМЕРА ТЕЛЕФОНОВ']
    with open(path, 'w', encoding='utf-8') as f:
        line = ';'.join(u_data)
        f.write(line + '\n')


def delete_all():
    print('*' * 35)
    print('\tУДАЛЕНИЕ ВСЕХ КОНТАКТОВ')
    open(path, 'w', encoding='utf-8').close()
    book_title()
    print('Все контакты удалены.')
    yes_or_no = input('Если желаете добавить новый контакт - нажмите Enter.\n'
                      'Для возврата в меню введите любой символ и нажмите Enter: ')
    if yes_or_no == '':
        add_new_contact()
    else:
        menu.menu()
