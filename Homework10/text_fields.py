main_menu = ['Главное меню:',
             '\t1. Игрок против игрока',
             '\t2. Игрок против компьютера (легко)',
             '\t3. Игрок против компьютера (сложно)',
             '\t4. Выход\n']

input_choice = 'Выберите режим игры: '
greeting = '\nПриветствую в игре крестики-нолики!\n'


def wrong_choice(limit: int):
    return f'Вы ввели неверное число! Надо от 1 до {limit}'


elements_list = [i for i in range(1, 10)]

first_player_move = 'Ход игрока 1. Выберите клетку: '
second_player_move = 'Ход игрока 2. Выберите клетку: '
computer_move = 'Ход компьютера'
human_move = 'Ваш ход. Выберите клетку: '

first_player_mark = 'X'
second_player_mark = 'O'

occupied = 'Данная клетка уже занята!'

win_pl_1 = 'Игрок 1 победил!\n'
win_pl_2 = 'Игрок 2 победил!\n'
draw_game = 'Ничья!\n'
win_human = 'Вы победили!\n'
win_computer = 'Компьютер победил!\n'

toss = '\nИдет жеребьевка...\n'

human_first = 'Вы делаете первый ход\n'
comp_first = 'Первым ходит компьютер\n'
