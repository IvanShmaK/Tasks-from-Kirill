"""Сделать электронный классный журнал в виде словаря, где ключом будет предмет. В значении еще один словарь, где
ключом уже выступает ФИО ученика, а значением - оценки ученика в виде списка. Сделать 3-4 предмета на 3-4 ученика.
Храниться эти данные должны в файле
{физика: {ФИО ученика: [3, 4, 5, 2, 3, 5],
          ФИО ученика: [3, 4, 5, 2, 3, 5],
          ФИО ученика: [3, 4, 5, 2, 3, 5]},
 химия: {ФИО ученика: [3, 4, 5, 2, 3, 5],
          ФИО ученика: [3, 4, 5, 2, 3, 5],
          ФИО ученика: [3, 4, 5, 2, 3, 5]}}"""

# electronic_journal = {'ФИЗИКА': {'Иванов И.И.': [3, 4, 5],     # начальная версия журнала
#                                  'Петров П.П.': [5, 4, 3],
#                                  'Сидоров С.С.': [3, 4, 2],
#                                  'Гаврилов Г.Г.': [5, 5, 5]},
#                       'ХИМИЯ': {'Иванов И.И.': [3, 4, 5],
#                                  'Петров П.П.': [5, 4, 3],
#                                  'Сидоров С.С.': [2, 4, 3],
#                                  'Гаврилов Г.Г.': [5, 5, 5]},
#                       'БИОЛОГИЯ': {'Иванов И.И.': [3, 4, 5],
#                                  'Петров П.П.': [5, 4, 3],
#                                  'Сидоров С.С.': [3, 3, 3],
#                                  'Гаврилов Г.Г.': [5, 5, 5]},
#                       'АЛГЕБРА': {'Иванов И.И.': [3, 4, 5],
#                                  'Петров П.П.': [5, 4, 3],
#                                  'Сидоров С.С.': [3, 5, 3],
#                                  'Гаврилов Г.Г.': [5, 5, 5]}}

with open('Task1_txt_files/Electronic_journal.txt', 'r', encoding='UTF-8') as data_file:
    electronic_journal_str = data_file.read()     # получаем электронный журнал в виде строки

electronic_journal_str = electronic_journal_str.replace('\n        ', ':').replace('\n', ':')  # заменяем ненужные символы на двоеточия
el_jor_list = electronic_journal_str.split(':')                                                # по которым через сплит строку переводим в список список
ratings_list = [item.replace(', ', '').lstrip() for item in el_jor_list if item[-1].isdigit()] # делаем отдельный список оценок
students_list = [item.lstrip() for item in el_jor_list if item.endswith('.')]                  # делаем отдельный список учеников
students_list = students_list[:len(set(students_list))]    # из которого берем только первые четыре, потому что учеников всего четыре
lessons_list = [item for item in el_jor_list if item[-1].isalpha()]                            # делаем отдельный список предметов

def internal_dict(names_list: list, rate_list: list) -> dict:  # функция, которая на вход получает два списка, на выходе выдает словарь
    internal_dict = {}
    for i in range(len(names_list)):        # ключами в словаре являются ученики
        for j in range(len(rate_list)):     # а значениями - их оценки (в виде строки)
            if i == j:
                internal_dict[names_list[i]] = rate_list[j]
    return internal_dict

el_jour_dict = {}           # создаем словарь, в котором ключами будут предметы, а значениями - словари, созданные вышеописанной функцией
ind = 0
while ind < len(ratings_list):
    for item in lessons_list:
        el_jour_dict[item] = internal_dict(students_list, ratings_list[ind:ind + len(students_list)]) # поскольку учеников 4, берем по 4 значения из списка оценок, затем переходим на следующий предмет
        ind += len(students_list)

def input_lesson(les_list: list) -> str:   # функция, которая допускает только правильный ввод названия урока
    while True:
        les = input('Введите название урока: ')
        if les.upper() in les_list:
            return les.upper()
lesson = input_lesson(lessons_list)

def input_student(stud_list: list) -> str:    # функция, которая допускает только правильный ввод ФИО ученика
    while True:
        stud = input('Введите ФИО ученика: ')
        if stud in stud_list:
            return stud
student = input_student(students_list)

def input_score() -> str:    # функция, которая допускает только правильный ввод оценки
    while True:
        stud = input('Введите оценку, которую получил ученик: ')
        if 0 < int(stud) < 6:
            return stud
score = input_score()

el_jour_dict[lesson.upper()][student] = el_jour_dict.get(lesson).get(student) + score  # в выбранном предмете выбранному ученику в список оценок добавляем поставленную нами

el_jor_str = ''
for les in range(len(lessons_list)): # переписываем получившийся словарь в строку так, как было изначально
    el_jor_str += lessons_list[les] + ': '
    for stud in range(len(students_list) - 1):
        el_jor_str += students_list[stud] + ': '
        for i in range(len(el_jour_dict[lessons_list[les]][students_list[stud]]) - 1):
            el_jor_str += el_jour_dict[lessons_list[les]][students_list[stud]][i] + ', '
        el_jor_str += el_jour_dict[lessons_list[les]][students_list[stud]][-1]
        el_jor_str += '\n        '
    el_jor_str += students_list[-1] + ': '
    for i in range(len(el_jour_dict[lessons_list[les]][students_list[-1]]) - 1):
        el_jor_str += el_jour_dict[lessons_list[les]][students_list[-1]][i] + ', '
    el_jor_str += el_jour_dict[lessons_list[les]][students_list[-1]][-1] + '\n'

with open('Task1_txt_files/Electronic_journal.txt', 'w', encoding='UTF-8') as data_file:
    data_file.write(el_jor_str)
