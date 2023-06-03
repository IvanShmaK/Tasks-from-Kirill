import random
from typing import Callable


def is_win(el: list) -> bool:
    """Данная функция проверяет, победил ли кто-нибудь. Она принимает на вход список (номера позиций на поле игры,
    частично замененные на крестики или нолики). На выходе получаем True, если кто-либо победил, или же False"""
    if (el[0] == el[1] == el[2]) or (el[3] == el[4] == el[5]) or (el[6] == el[7] == el[8]) or \
            (el[0] == el[3] == el[6]) or (el[1] == el[4] == el[7]) or (el[2] == el[5] == el[8]) or \
            (el[0] == el[4] == el[8]) or (el[2] == el[4] == el[6]):
        return True
    return False


def game(func_1: Callable, func_3: Callable, func_5: Callable, func_7: Callable, func_9: Callable, fp_move: str,
         fp_mark: str, func_2: Callable, func_4: Callable, func_6: Callable, func_8: Callable, sp_move: str,
         sp_mark: str, func_10: Callable, func_11: Callable, win_1: str, win_2: str, no_win: str):
    """Данная функция обеспечивает выполнение алгоритма игры. Она принимает на вход функции хода игроков, строки
    (сообщения о том, кто делает ход), строки (крестик и нолик), функцию проверки победителя, функцию печати сообщений о
    победе, строки (сообщения о том, кто победил, либо о ничьей)."""
    el_list = [i for i in range(1, 10)]
    func_1(el_list, fp_move, fp_mark)    # 1 ход
    func_2(el_list, sp_move, sp_mark)  # 2 ход
    func_3(el_list, fp_move, fp_mark)    # 3 ход
    func_4(el_list, sp_move, sp_mark)  # 4 ход
    func_5(el_list, fp_move, fp_mark)    # 5 ход
    if func_10(el_list):  # проверка на победу
        func_11(win_1)  # вывод сообщения, что первый игрок победил
    else:
        func_6(el_list, sp_move, sp_mark)  # 6 ход
        if func_10(el_list):  # проверка на победу
            func_11(win_2)  # вывод сообщения, что второй игрок победил
        else:
            func_7(el_list, fp_move, fp_mark)  # 7 ход
            if func_10(el_list):  # проверка на победу
                func_11(win_1)  # вывод сообщения, что первый игрок победил
            else:
                func_8(el_list, sp_move, sp_mark)  # 8 ход
                if func_10(el_list):  # проверка на победу
                    func_11(win_2)  # вывод сообщения, что второй игрок победил
                else:
                    func_9(el_list, fp_move, fp_mark)  # 9 ход
                    if func_10(el_list):  # проверка на победу
                        func_11(win_1)  # вывод сообщения, что первый игрок победил
                    else:
                        func_11(no_win)  # вывод сообщения о ничьей


def game_toss() -> bool:
    """Данная функция рандомно определяет, кто будет ходить первым, человек или компьютер. Она ничего не принимает на
    вход. На выходе получаем True (в этом случае первым ходит человек), либо False (в этом случае первым ходит
    компьютер)"""
    if random.randint(0, 1):
        return True
    return False


def comp_do_not_want_lose(el: list, mark: str):
    """Данная функция не дает человеку победить, если ему предоставляется такая возможность. Она принимает на вход
    список (номера позиций на поле игры, частично замененные на крестики или нолики) и строку (нолик или крестик).
    Возвращает функция измененный элемент списка, если в ходе выполнения условий элемент изменился, или же False, если
    нет"""
    if str(el[0]).isdigit() and (el[3] == el[6] or el[1] == el[2] or el[4] == el[8]):
        el[0] = mark
        return el[0]
    elif str(el[1]).isdigit() and (el[0] == el[2] or el[4] == el[7]):
        el[1] = mark
        return el[1]
    elif str(el[2]).isdigit() and (el[0] == el[1] or el[5] == el[8] or el[4] == el[6]):
        el[2] = mark
        return el[2]
    elif str(el[3]).isdigit() and (el[0] == el[6] or el[4] == el[5]):
        el[3] = mark
        return el[3]
    elif str(el[4]).isdigit() and (el[0] == el[8] or el[2] == el[6] or el[1] == el[7] or el[3] == el[5]):
        el[4] = mark
        return el[4]
    elif str(el[5]).isdigit() and (el[2] == el[8] or el[3] == el[4]):
        el[5] = mark
        return el[5]
    elif str(el[6]).isdigit() and (el[7] == el[8] or el[3] == el[0] or el[4] == el[2]):
        el[6] = mark
        return el[6]
    elif str(el[7]).isdigit() and (el[8] == el[6] or el[4] == el[1]):
        el[7] = mark
        return el[7]
    elif str(el[8]).isdigit() and (el[7] == el[6] or el[2] == el[5] or el[0] == el[4]):
        el[8] = mark
        return el[8]
    return False


def comp_want_win(self, el: list, mark: str):
    """Данная функция обеспечивает компьютеру победу, как только ему предоставляется такая возможность. Она принимает
    на вход список (номера позиций на поле игры, частично замененные на крестики или нолики) и строку (нолик или
    крестик). Возвращает функция измененный элемент списка, если в ходе выполнения условий элемент изменился, или же
    False, если нет"""
    if str(el[0]).isdigit() and ((el[3] == mark and el[6] == mark) or (el[1] == mark and el[2] == mark) or
                                 (el[4] == mark and el[8] == mark)):
        el[0] = mark
        return el[0]
    elif str(el[1]).isdigit() and ((el[0] == mark and el[2] == mark) or (el[4] == mark and el[7] == mark)):
        el[1] = mark
        return el[1]
    elif str(el[2]).isdigit() and ((el[0] == mark and el[1] == mark) or (el[5] == mark and el[8] == mark) or
                                   (el[4] == mark and el[6] == mark)):
        el[2] = mark
        return el[2]
    elif str(el[3]).isdigit() and ((el[0] == mark and el[6] == mark) or (el[4] == mark and el[5] == mark)):
        el[3] = mark
        return el[3]
    elif str(el[4]).isdigit() and ((el[0] == mark and el[8] == mark) or (el[2] == mark and el[6] == mark) or
                                   (el[1] == mark and el[7] == mark) or (el[3] == mark and el[5] == mark)):
        el[4] = mark
        return el[4]
    elif str(el[5]).isdigit() and ((el[2] == mark and el[8] == mark) or (el[3] == mark and el[4] == mark)):
        el[5] = mark
        return el[5]
    elif str(el[6]).isdigit() and ((el[7] == mark and el[8] == mark) or (el[3] == mark and el[0] == mark) or
                                   (el[4] == mark and el[2] == mark)):
        el[6] = mark
        return el[6]
    elif str(el[7]).isdigit() and ((el[8] == mark and el[6] == mark) or (el[4] == mark and el[1] == mark)):
        el[7] = mark
        return el[7]
    elif str(el[8]).isdigit() and ((el[7] == mark and el[6] == mark) or (el[2] == mark and el[5] == mark) or
                                   (el[0] == mark and el[4] == mark)):
        el[8] = mark
        return el[8]
    return False
