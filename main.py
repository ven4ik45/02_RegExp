import re

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# собираем новый список с нужным форматом телефонных номеров
temp_list = list()
for i in contacts_list:
    temp = list()
    for item in i:
        re_pattern = r"(8|\+7)\s?\(?" \
                             r"(\d+)\)?[\s-]*" \
                             r"(\d+)[\s-]*" \
                             r"(\d+)[\s-]*" \
                             r"(\d+)[\s*]?\(?" \
                             r"(доб.)?\s?" \
                             r"(\d+)?\)?"
        stro = (re.sub(re_pattern, r'+7(\2)\3-\4-\5\6\7', str(item)))
        temp.append(stro)
    temp_list.append(temp)

# приводим список ФИО к единому знаменателю, Ф,И,О
new_list = list()
for index, item in enumerate(temp_list):
    if index == 0:
        new_list.append(item)
    else:
        item1 = " ".join(item[:3]).split(" ")
        while len(item1) > 3:
            item1.pop(-1)

        item1.extend(item[3:])

        new_list.append(item1)

# список для повторов
repeat = []

# создаем корректный список
correct_list = list()

# Пересобираем списки учитывая пробелы в "колонках", дополняем из дублей
for elem1 in new_list:
    elem1_index = new_list.index(elem1)
    for elem2 in new_list:
        elem2_index = new_list.index(elem2)
        if elem1[:2] == elem2[:2] and elem2_index > elem1_index:
            #добавляем индекс повторяющейся записи в переменную
            repeat.append(elem2_index)

            for item in elem2:
                text = item
                indexx = int(elem2.index(item))
                i1_fdsf = elem1[indexx]
                if not elem1[indexx]:
                    new_list[elem1_index][indexx] = elem2[indexx]

for i in new_list:
    if new_list.index(i) not in repeat:
        correct_list.append(i)

pprint(correct_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(correct_list)
