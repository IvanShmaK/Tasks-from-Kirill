import model
import view
import text_fields as tf


def start():
    view.print_message(tf.greeting)  # приветствие в игре
    while True:
        choice_menu = view.print_menu(tf.main_menu)
        el = tf.elements_list
        match choice_menu:  # вывод меню
            case 1:  # игрок против игрока
                view.print_play_field(el)
                model.game(view.Player.human_move, view.Player.human_move, view.Player.human_move,
                           view.Player.human_move, view.Player.human_move, tf.first_player_move, tf.first_player_mark,
                           view.Player.human_move, view.Player.human_move,view.Player.human_move,
                           view.Player.human_move, tf.second_player_move, tf.second_player_mark, model.is_win,
                           view.print_message, tf.win_pl_1, tf.win_pl_2, tf.draw_game)
            case 2:  # игрок против компьютера, легкий уровень
                view.print_message(tf.toss)
                if model.game_toss():
                    view.print_message(tf.human_first)  # первым ходит игрок
                    view.print_play_field(el)
                    model.game(view.Player.human_move, view.Player.human_move, view.Player.human_move,
                               view.Player.human_move, view.Player.human_move, tf.human_move, tf.first_player_mark,
                               view.Player.comp_stupid_move, view.Player.comp_stupid_move, view.Player.comp_stupid_move,
                               view.Player.comp_stupid_move, tf.computer_move, tf.second_player_mark,
                               model.is_win, view.print_message, tf.win_human, tf.win_computer, tf.draw_game)
                else:
                    view.print_message(tf.comp_first)  # первым ходит компьютер
                    model.game(view.Player.comp_stupid_move, view.Player.comp_stupid_move, view.Player.comp_stupid_move,
                               view.Player.comp_stupid_move, view.Player.comp_stupid_move, tf.computer_move,
                               tf.first_player_mark, view.Player.human_move, view.Player.human_move,
                               view.Player.human_move, view.Player.human_move, tf.human_move, tf.second_player_mark,
                               model.is_win, view.print_message, tf.win_computer,
                               tf.win_human, tf.draw_game)
            case 3:  # игрок против компьютера, сложный уровень
                view.print_message(tf.toss)
                if model.game_toss():
                    view.print_message(tf.human_first)  # первым ходит игрок
                    view.print_play_field(el)
                    model.game(view.Player.human_move, view.Player.human_move, view.Player.human_move,
                               view.Player.human_move, view.Player.human_move, tf.human_move, tf.first_player_mark,
                               view.Player.comp_smart_second_move, view.Player.comp_smart_fourth_move,
                               view.Player.comp_smart_sixth_move, view.Player.comp_smart_eighth_move,
                               tf.computer_move, tf.second_player_mark, model.is_win, view.print_message, tf.win_human,
                               tf.win_computer, tf.draw_game)
                else:
                    view.print_message(tf.comp_first)  # первым ходит компьютер
                    model.game(view.Player.comp_smart_first_move, view.Player.comp_smart_third_move,
                               view.Player.comp_smart_fifth_move, view.Player.comp_smart_seventh_move,
                               view.Player.comp_smart_ninth_move, tf.computer_move, tf.first_player_mark,
                               view.Player.human_move, view.Player.human_move, view.Player.human_move,
                               view.Player.human_move, tf.human_move, tf.second_player_mark, model.is_win,
                               view.print_message, tf.win_computer, tf.win_human, tf.draw_game)
            case 4:
                break
