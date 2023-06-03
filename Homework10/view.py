import text_fields as tf
import random
import model


def print_message(message: str):  # функция печати сообщения
    print(message)


def print_menu(menu: list) -> int:  # функция печати меню
    print(*menu, sep='\n')
    return input_choice(len(menu) - 1, tf.input_choice)


def input_choice(size: int, message: str):  # функция по выбору позиции меню
    while True:
        number = input(message)
        if number.isdigit() and 0 < int(number) < size + 1:
            return int(number)
        else:
            print(tf.wrong_choice(size))


def print_play_field(el: list):
    """Данная функция выводит на экран игровое поле в соответствии с заданным списком элементов"""
    print('-' * 13)
    print(f'| {el[0]} | {el[1]} | {el[2]} |')
    print('-' * 4 + '+' + '-' * 3 + '+' + '-' * 4)
    print(f'| {el[3]} | {el[4]} | {el[5]} |')
    print('-' * 4 + '+' + '-' * 3 + '+' + '-' * 4)
    print(f'| {el[6]} | {el[7]} | {el[8]} |')
    print('-' * 13)


class Player:
    def __init__(self, elem_list: list[str], move: str, mark: str):
        self.elem_list = elem_list
        self.move = move
        self.mark = mark

    def human_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает ходы человека. Она принимает на вход список (номера позиций на поле игры, частично
        замененные на крестики или нолики), строку (сообщение о том, что ходит компьютер), и строку (крестик или нолик). На
        выходе получаем измененный список, в соответствии с которым распечатывается поле игры со сделанными ходами"""
        num = input_choice(9, move)
        if num in el:
            for i in range(len(el)):
                if el[i] == num:
                    el[i] = mark
        else:
            print_message(tf.occupied)
            return self.human_move(el, move, mark)
        print_play_field(el)

    def comp_stupid_move(self, el: list, move: str, mark: str):
        """Данная функция выполняет ходы глупого компьютера. Она принимает на вход список (номера позиций на поле игры,
        частично замененные на крестики или нолики), строку (сообщение о том, что ходит компьютер), и строку (крестик или
        нолик). На выходе получаем измененный список, в соответствии с которым распечатывается поле игры со сделанными
        ходами. Компьютер рандомом ставит свой знак на любую свободную клетку"""
        print_message(move)
        num = random.choice([i for i in el if str(i).isdigit()])
        for i in range(len(el)):
            if el[i] == num:
                el[i] = mark
        print_play_field(el)

    def comp_smart_first_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает первый ход умного компьютера (первый ход по ходу игры). Она принимает на вход список
        (номера позиций на поле игры, частично замененные на крестики или нолики), строку (сообщение о том, что ходит
        компьютер), и строку (крестик). На выходе получаем измененный список, в соответствии с которым распечатывается поле
        игры со сделанными ходами. Компьютер всегда ставит крестик в центр поля"""
        print_message(move)
        el[4] = mark
        print_play_field(el)

    def comp_smart_third_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает второй ход умного компьютера, когда он ходит первым (третий ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (крестик). На выходе получаем измененный список, в соответствии
        с которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if str(el[1]).isalpha() or str(el[3]).isalpha() or str(el[5]).isalpha() or str(el[7]).isalpha():
            num = random.choice([1, 3, 7, 9])  # если человек поставил нолик на сторону, комп ставит крестик в любой угол
            for i in range(len(el)):
                if el[i] == num:
                    el[i] = mark
        else:  # если человек поставил нолик в угол, комп ставит крестик в противоположный угол
            if str(el[0]).isalpha():
                el[8] = mark
            elif str(el[2]).isalpha():
                el[6] = mark
            elif str(el[6]).isalpha():
                el[2] = mark
            else:
                el[0] = mark
        print_play_field(el)

    def comp_smart_fifth_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает третий ход умного компьютера, когда он ходит первым (пятый ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (крестик). На выходе получаем измененный список, в соответствии
        с которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if model.comp_want_win(el, mark):
            pass
        elif model.comp_do_not_want_lose(el, mark):
            pass
        elif el[1] == 'O' or el[7] == 'O':
            if el[0] == mark:
                el[6] = mark
            elif el[2] == mark:
                el[8] = mark
            elif el[6] == mark:
                el[0] = mark
            else:
                el[2] = mark
        elif el[3] == 'O' or el[5] == 'O':
            if el[0] == mark:
                el[2] = mark
            elif el[2] == mark:
                el[0] = mark
            elif el[6] == mark:
                el[8] = mark
            else:
                el[6] = mark
        elif el[0] == 'O':
            if el[5] == 'O':
                el[6] = mark
            else:
                el[2] = mark
        elif el[2] == 'O':
            if el[3] == 'O':
                el[8] = mark
            else:
                el[0] = mark
        elif el[8] == 'O':
            if el[3] == 'O':
                el[2] = mark
            else:
                el[6] = mark
        else:
            if el[5] == 'O':
                el[0] = mark
            else:
                el[8] = mark
        print_play_field(el)

    def comp_smart_seventh_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает четвертый ход умного компьютера, когда он ходит первым (седьмой ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (крестик). На выходе получаем измененный список, в соответствии
        с которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if model.comp_want_win(el, mark):
            pass
        elif model.comp_do_not_want_lose(el, mark):
            pass
        elif el[0] == 'O':
            if el[6] == 'O':
                el[1] = mark
            else:
                el[3] = mark
        elif el[2] == 'O':
            if el[0] == 'O':
                el[5] = mark
            else:
                el[1] = mark
        elif el[8] == 'O':
            if el[6] == 'O':
                el[5] = mark
            else:
                el[7] = mark
        else:
            if el[0] == 'O':
                el[7] = mark
            else:
                el[3] = mark
        print_play_field(el)

    def comp_smart_ninth_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает пятый ход умного компьютера, когда он ходит первым (девятый ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (крестик). На выходе получаем измененный список, в соответствии
        с которым распечатывается поле игры со сделанными ходами. Компьютер просто ставит крестик в оставшуюся свободную
        клетку"""
        print_message(move)
        for i in range(len(el)):
            if str(el[i]).isdigit():
                el[i] = mark
        print_play_field(el)

    def comp_smart_second_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает первый ход умного компьютера, когда он ходит вторым (второй ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (нолик). На выходе получаем измененный список, в соответствии
        с которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if el[4] != 'X':  # если центральное поле не занято, комп ставит туда нолик
            el[4] = mark
        else:  # иначе комп ставит нолик в любой угол
            num = random.choice([1, 3, 7, 9])
            for i in range(len(el)):
                if el[i] == num:
                    el[i] = mark
        print_play_field(el)

    def comp_smart_fourth_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает второй ход умного компьютера, когда он ходит вторым (четвертый ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (нолик). На выходе получаем измененный список, в соответствии с
        которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if model.comp_do_not_want_lose(el, mark):  # компьютер не дает человеку победить на следующем ходу
            pass
        elif el[4] == 'X' and \
                ((str(el[0]).isalpha() and str(el[8]).isalpha()) or (str(el[2]).isalpha() and str(el[6]).isalpha())):
            num = random.choice([i for i in [el[0], el[2], el[6], el[8]] if str(i).isdigit()])
            for i in range(len(el)):  # если в центре стоит крестик и по любой диагонали поля заняты,
                if el[i] == num:      # комп ставит нолик в любой свободный угол
                    el[i] = mark
        else:  # варианты оставшихся ходов для компьютера, когда нолик в центре (варианты, когда в центре крестик,
            if (el[1] == 'X' and el[7] == 'X') or (el[3] == 'X' and el[5] == 'X'):  # учтены в двух предыдущих условиях)
                num = random.choice([1, 3, 7, 9])
                for i in range(len(el)):  # если по любой линии центрального перекрестья поля заняты,
                    if el[i] == num:      # комп ставит нолик в любой свободный угол
                        el[i] = mark
            elif (el[0] == 'X' and el[8] == 'X') or (el[2] == 'X' and el[6] == 'X'):
                num = random.choice([i for i in [el[1], el[3], el[5], el[7]]])
                for i in range(len(el)):  # если в центре стоит нолик и по любой диагонали поля заняты,
                    if el[i] == num:      # комп ставит нолик на среднюю клетку любой стороны
                        el[i] = mark
            elif el[1] == 'X' and el[3] == 'X':
                el[0] = mark
            elif el[1] == 'X' and el[5] == 'X':
                el[2] = mark
            elif el[7] == 'X' and el[3] == 'X':
                el[6] = mark
            elif el[5] == 'X' and el[7] == 'X':
                el[8] = mark
            elif (el[6] == 'X' and el[5] == 'X') or (el[3] == 'X' and el[8] == 'X'):
                el[1] = mark
            elif (el[2] == 'X' and el[7] == 'X') or (el[1] == 'X' and el[8] == 'X'):
                el[3] = mark
            elif (el[0] == 'X' and el[7] == 'X') or (el[1] == 'X' and el[6] == 'X'):
                el[5] = mark
            else:
                el[7] = mark
        print_play_field(el)

    def comp_smart_sixth_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает третий ход умного компьютера, когда он ходит вторым (шестой ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (нолик). На выходе получаем измененный список, в соответствии с
        которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if model.comp_want_win(el, mark):
            pass
        elif model.comp_do_not_want_lose(el, mark):
            pass
        elif el[4] == 'X':  # варианты, когда в центре крестик
            if (el[8] == 'X' and el[0] == mark and el[1] == 'X' and el[7] == mark) or \
                    (el[0] == 'X' and el[3] == mark and el[5] == 'X' and el[8] == mark):
                el[6] = mark
            elif (el[8] == 'X' and el[0] == mark and el[3] == 'X' and el[5] == mark) or \
                    (el[0] == 'X' and el[1] == mark and el[7] == 'X' and el[8] == mark):
                el[2] = mark
            elif (el[6] == 'X' and el[2] == mark and el[5] == 'X' and el[3] == mark) or \
                    (el[7] == 'X' and el[6] == mark and el[2] == 'X' and el[1] == mark):
                el[0] = mark
            elif (el[6] == 'X' and el[2] == mark and el[1] == 'X' and el[7] == mark) or \
                    (el[2] == 'X' and el[5] == mark and el[3] == 'X' and el[6] == mark):
                el[8] = mark
        else:  # варианты, когда в центре нолик
            if (el[0] == 'X' and el[2] == 'X' and el[7] == 'X' and el[1] == mark) or \
                    (el[1] == 'X' and el[6] == 'X' and el[8] == 'X' and el[7] == mark):
                el[3] = mark
            elif (el[0] == 'X' and el[5] == 'X' and el[6] == 'X' and el[3] == mark) or \
                    (el[2] == 'X' and el[3] == 'X' and el[8] == 'X' and el[5] == mark):
                el[1] = mark
            elif (el[1] == 'X' and el[3] == 'X' and el[8] == 'X' and el[0] == mark) or \
                    (el[0] == 'X' and el[5] == 'X' and el[7] == 'X' and el[8] == mark):
                el[2] = mark
            else:
                el[0] = mark
        print_play_field(el)

    def comp_smart_eighth_move(self, el: list, move: str, mark: str):
        """Данная функция обеспечивает четвертый ход умного компьютера, когда он ходит вторым (восьмой ход по ходу игры).
        Она принимает на вход список (номера позиций на поле игры, частично замененные на крестики или нолики), строку
        (сообщение о том, что ходит компьютер), и строку (нолик). На выходе получаем измененный список, в соответствии с
        которым распечатывается поле игры со сделанными ходами"""
        print_message(move)
        if model.comp_want_win(el, mark):
            pass
        elif model.comp_do_not_want_lose(el, mark):
            pass
        else:
            num = random.choice([i for i in el if str(i).isdigit()])
            for i in range(len(el)):  # если не отработали предыдущие функции, комп ставит нолик в любую свободную клетку
                if el[i] == num:      # (это все равно приведет к ничьей)
                    el[i] = mark
        print_play_field(el)
