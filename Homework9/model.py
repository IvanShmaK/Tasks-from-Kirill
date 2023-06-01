# файл для функций обработки информации

class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f'{self.name: <20} | {self.phone: <20} | {self.comment: <20}'

    def contact_name(self) -> str:  # функция, которая возвращает имя контакта
        return self.name

    def contact_phone(self) -> str:  # функция, которая возвращает телефон контакта
        return self.phone

    def contact_comment(self) -> str:  # функция, которая возвращает комментарий контакта
        return self.comment


class PhoneBook:
    def __init__(self, path: str = 'Phone_book.txt'):
        self.path = path
        self.contact: list[Contact] = []

    def open_file(self):  # функция, которая извлекает список контактов из файла txt, и формирует список строк-контактов
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        self.contact = [Contact(*list(map(lambda x: x.strip(), contact.split(':')))) for contact in data]

    def size(self):  # функция, определяющая длину списка контактов
        return len(self.contact)

    def __str__(self):  # функция, позволяющая напечатать телефонную книгу с нумерацией контактов
        contact_list = []
        for i, contact in enumerate(self.contact, 1):
            contact_list.append(contact.__str__())
            contact_list[i - 1] = f'{i: ^3} | ' + contact_list[i - 1]
        return '\n'.join(contact_list) if self.contact else ' ' * 24 + 'Телефонная книга пуста!'

    def add_contact(self, data: dict[str, str]):  # функция по добавлению контакта
        self.contact.append(Contact(*[item for item in data.values()]))

    def change(self, ind: int, contact: dict[str, str]) -> Contact:  # функция по изменению контакта
        cur = self.contact[ind]  # из списка контактов выбираем тот, который нужно изменить
        cur_dict = {'name': Contact.contact_name(cur), 'phone': Contact.contact_phone(cur),  # и переводим его в словарь
                    'comment': Contact.contact_comment(cur)}
        cur_dict.update(contact)  # дополняем контакт-словарь новыми данными
        result = self.contact.pop(ind)  # удаляем выбранный контакт из списка
        self.contact.insert(ind, Contact(*[item for item in cur_dict.values()]))  # и заменяем его на измененный
        return result  # возвращаем удаленный контакт

    def delete_contact(self, ind: int):  # функция по удалению контакта
        return self.contact.pop(ind)

    def search_contact(self, word: str):  # функция по поиску контакта
        for cont in self.contact:
            if word.lower() in Contact.contact_name(cont).lower() or \
                    word.lower() in Contact.contact_phone(cont).lower() or \
                    word.lower() in Contact.contact_comment(cont).lower():
                return cont

    def save_file(self):  # функция по сохранению файла
        pb_str = ''
        for cont in self.contact:
            pb_str += Contact.contact_name(cont) + ':' + Contact.contact_phone(cont) + ':' + \
                      Contact.contact_comment(cont) + '\n'
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(pb_str)



