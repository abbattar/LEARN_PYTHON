import datetime
# import pathlib
import random
# from pathlib import Path
from random import randint
# import pyodbc          # не сработала, хотя pip install pyodbc делал, для работы с .access

# try:
#     con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:/Moi_Dokumenty/Practics/Python/HW_7/phonebook.accdb;'
#     conn = pyodbc.connect(con_string)
#     print("Connected To Database")
#
# except pyodbc.Error as e:
#     print("Error in Connection", e)

path = 'phonebook.csv'      # path = Path('phonebook.csv')
# path2 = Path('phonebook.accdb')   # попытался поработать с форматом .accdb

def counter_lines_csv():
    with open(path, 'r', encoding='utf-8') as f:
        return str(len(f.readlines()))

def generate_fake_contact():
    print('*' * 35)
    print('\tГЕНЕРАЦИЯ КОНТАКТОВ ДЛЯ ОЗНАКОМЛЕНИЯ С ПРОГРАММОЙ')
    # dir_path = pathlib.Path.cwd() #
    # работает не верно ==> возращает E:\\Moi_Dokumenty\\Practics...,
    # т.е. вместо "\" -> "\\" пришлось указывать напрямую
    for _ in range(30):
        name = random.choice(open('E:/Moi_Dokumenty/Practics/Python/CW_9/Seminar_8/LEARN_PYTHON/quart_2/seminar_8/fake_data/names.txt', encoding='utf-8').readlines()).strip()
        surname = random.choice(open('E:/Moi_Dokumenty/Practics/Python/CW_9/Seminar_8/LEARN_PYTHON/quart_2/seminar_8/fake_data/surnames.txt', encoding='utf-8').readlines()).strip()
        birthday = datetime.date(randint(1950, 2000), randint(1, 12), randint(1, 28)).strftime("%d.%m.%Y")
        work = random.choice(open('E:/Moi_Dokumenty/Practics/Python/CW_9/Seminar_8/LEARN_PYTHON/quart_2/seminar_8/fake_data/companies.txt', encoding='utf-8').readlines()).strip()
        phonenum = '+' + str(random.randint(79000000000, 80000000000))
        u_data = [name, surname, birthday, work, phonenum]

        with open(path, 'a', encoding='utf-8') as f:
            line = ';'.join(u_data)
            f.write(counter_lines_csv() + ';' + line + '\n')

    print('Сгенерировано 30 фейковых аккаунтов.')