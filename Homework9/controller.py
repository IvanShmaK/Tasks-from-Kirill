# файл, осуществляющий взаимодействие между model.py и view.py
import view
import model
import text_fields as tf


def start():
    pb = model.PhoneBook()
    pb.open_file()  # телефонная книга открывается при запуске программы
    view.print_message(tf.open_successful)
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.show_contact(pb, '')
            case 2:
                new_contact = view.input_contact(tf.new_contact)  # добавить контакт можно, даже если телефонная книга пуста
                pb.add_contact(new_contact)
                view.print_message(tf.add_successful)
            case 3:
                if pb:  # здесь и далее - проверка на то, не пуста ли телефонная книга
                    key_word = view.search_word()
                    cont = pb.search_contact(key_word)
                    view.show_contact(cont, tf.dont_found)
                else:
                    view.print_message(tf.no_phone_book)
            case 4:
                if pb:
                    view.show_contact(pb, '')  # показываем список контактов
                    choice = view.input_choice(pb.size(), tf.change_choice) - 1  # выбираем, какой контакт изменить
                    change_contact = view.input_contact(tf.change_contact)  # пишем новые данные контакта
                    res = pb.change(choice, change_contact)  # заменяем старые данные на новые
                    view.print_message(tf.changed(model.Contact.contact_name(res)))  # пишем, что данный контакт изменен
                else:
                    view.print_message(tf.no_phone_book)
            case 5:
                if pb:
                    view.show_contact(pb, '')
                    choice = view.input_choice(pb.size(), tf.del_contact) - 1
                    res = pb.delete_contact(choice)
                    view.print_message(tf.deleted(model.Contact.contact_name(res)))
                else:
                    view.print_message(tf.no_phone_book)
            case 6:
                pb.save_file()
                view.print_message(tf.saved)
            case 7:
                break
