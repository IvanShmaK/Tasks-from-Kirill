# файл для функций обработки информации

phone_book: list[dict[str, str]] = []
PATH = 'Phone_book.txt'


def open_file():  # функция, которая извлекает список контактов из файла txt, и формирует список строк-контактов
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        contact = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(contact)
    return phone_book


def add_contact(contact: dict[str, str]):  # функция по добавлению контакта
    phone_book.append(contact)


def change(ind: int, contact: dict[str, str]) -> dict[str, str]:  # функция по изменению контакта
    cur = phone_book[ind]
    cur.update(contact)
    result = phone_book.pop(ind)
    phone_book.insert(ind, cur)
    return result


def delete_contact(ind: int):  # функция по удалению контакта
    result = phone_book.pop(ind)
    return result


def search_contact(contacts: list[dict[str, str]], word: str) -> list[dict[str, str]]:  # функция по поиску контакта
    one_contact = []
    for cont in contacts:
        if word.lower() in cont['name'].lower() or word in cont['phone'].lower() or word in cont['comment'].lower():
            one_contact.append(cont)
            return one_contact


def save_file(contacts: list[dict[str, str]]):  # функция по сохранению файла
    pb_str = ''
    for cont in contacts:
        pb_str += cont['name'] + ':' + cont['phone'] + ':' + cont['comment'] + '\n'
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(pb_str)



