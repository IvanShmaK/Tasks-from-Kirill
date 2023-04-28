"""написать программу, которая прочитает этот файл. после этого
надо изменить текст, чтобы каждое предложение было записано
с большой букы (после точки большая буква). и записать текст
обратно в этот файл. скинуть на репозиторий этот файл и файл
с самой программой."""

with open('sample.txt', 'r', encoding='UTF-8') as user_file:
    data_str = user_file.read()

data_list = data_str.split('. ')

data_str_mod = '. '.join([data_list[i].capitalize() for i in range(len(data_list))])

with open('sample.txt', 'w', encoding='UTF-8') as user_file:
    user_file.write(data_str_mod)