# файл для функций ввода и вывода
import text_fields as tf
import model


def main_menu() -> int:  # функция по выводу меню
    print(*tf.menu, sep='\n')
    return input_choice(len(tf.menu) - 1, tf.input_choice)


def input_choice(size: int, message: str):  # функция по выбору позиции меню
    while True:
        number = input(message)
        if number.isdigit() and 0 < int(number) < size + 1:
            return int(number)
        else:
            print(tf.wrong_choice(size))


def show_contact(book: model.PhoneBook | list[str], message: str):  # функция по выводу контактов
    if book:
        print('\n' + '=' * 72)
        print(book)
        print('=' * 72 + '\n')
    else:
        print(message)


def print_message(message: str):  # функция по выводу сообщения
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def input_contact(message: list[str]) -> dict[str, str]:  # функция по вводу данных для изменения контакта
    contact = {}
    name = input(message[0])
    phone = input(message[1])
    comment = input(message[2])
    if name:
        contact['name'] = name
    if phone:
        contact['phone'] = phone
    if comment:
        contact['comment'] = comment
    return contact


def search_word() -> str:  # функция по вводу слова для поиска
    word = input(tf.search_key)
    return word
