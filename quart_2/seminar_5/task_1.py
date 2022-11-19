# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".
# Пример:
# Входные данные: 'бываав лповап абвцукв алоавбав ываываыв'
# Выходные данные: 'лповап ываываыв'
# Входные и выходные данные хранятся в отдельных текстовых файлах

with open('text1_task_1.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    print(f'Строка из файла: {txt}')

find_a, find_b, find_v = 'а', 'б', 'в'
txt_2 = ''

for i in txt.split():
    count = 0
    if (find_a in i): count += 1
    if (find_b in i): count += 1
    if (find_v in i): count += 1
    if count < 3: txt_2 = txt_2 + i + ' '

txt_2 = txt_2[:-1]

with open('text2_task_1.txt', 'w', encoding='utf-8') as f:
    f.write(txt_2)
    print(f'Слова, в которых нет всех букв: {txt_2}')
