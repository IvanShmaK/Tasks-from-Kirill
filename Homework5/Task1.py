"""написать две функции - шифратор и дешифратор Цезаря"""

from typing import Callable

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

user_key = int(input('Введите ключ к шифру: '))
user_text = input('Введите текст: ')

user_list = list(user_text.upper())

encrypted_user_list = []
for item in user_list:                    # цикл по шифровке текста. Шифруются только буквы, знаки препинания и цифры остаются неизменными
    if not item.isalpha():
        encrypted_user_list.append(item)
    for j in range(len(alphabet)):
        if j + user_key > len(alphabet):
            j = j + user_key - len(alphabet)
        if item == alphabet[j]:
            encrypted_user_list.append(alphabet[j + user_key])
encrypted_user_text = ''.join(encrypted_user_list).lower()
print(encrypted_user_text.capitalize())       


excrypted_user_list = []
for item in user_list:                    # цикл по расшифровке текста. 
    if not item.isalpha():
        excrypted_user_list.append(item)
    for j in range(len(alphabet)):
        if j < user_key:
            j = len(alphabet) - user_key
        if item == alphabet[j]:
            excrypted_user_list.append(alphabet[j - user_key])
excrypted_user_text = ''.join(excrypted_user_list).lower()
print(excrypted_user_text.capitalize())       