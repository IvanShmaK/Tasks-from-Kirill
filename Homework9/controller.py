# файл, осуществляющий взаимодействие между model.py и view.py
import view
import model
import text_fields as tf


def start():
    model.open_file()  # телефонная книга открывается при запуске программы
    view.print_message(tf.open_successful)
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pb = model.phone_book
                if pb:  # здесь и далее - проверки на то, не пуста ли телефонная книга
                    view.show_contact(pb, '')
                else:
                    view.print_message(tf.no_phone_book)
            case 2:
                new_contact = view.input_contact(tf.new_contact)  # добавить контакт можно, даже если телефонная книга пуста
                model.add_contact(new_contact)
                view.print_message(tf.add_successful)
            case 3:
                pb = model.phone_book
                if pb:
                    key_word = view.search_word()
                    cont = model.search_contact(pb, key_word)
                    view.show_contact(cont, tf.dont_found)
                else:
                    view.print_message(tf.no_phone_book)
            case 4:
                pb = model.phone_book
                if pb:
                    view.show_contact(pb, '')  # показываем список контактов
                    choice = view.input_choice(len(pb), tf.change_choice) - 1  # выбираем, какой контакт изменить
                    change_contact = view.input_contact(tf.change_contact)  # пишем новые данные контакта
                    res = model.change(choice, change_contact)  # заменяем старые данные на новые
                    view.print_message(tf.changed(res['name']))  # пишем, что данный контакт изменен
                else:
                    view.print_message(tf.no_phone_book)
            case 5:
                pb = model.phone_book
                if pb:
                    view.show_contact(pb, '')
                    choice = view.input_choice(len(pb), tf.del_contact) - 1
                    res = model.delete_contact(choice)
                    view.print_message(tf.deleted(res['name']))
                else:
                    view.print_message(tf.no_phone_book)
            case 6:
                model.save_file(pb)
                view.print_message(tf.saved)
            case 7:
                break
