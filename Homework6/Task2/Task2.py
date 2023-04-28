"""выдать топ 5 самых встречаемы слов в Алисе длинна которых не меньше 5 букв
так же можете собрать еще какую-то статистику (не обязательное задание на фантазию) :)"""

with open('Alice in Wonderland.txt', 'r', encoding='UTF-8') as user_file:
    alice_string = user_file.read()

# import string                   
# for letter in string.punctuation:                    # хотел убрать знаки препинания данным методом, но не убрались кавычки и тире почему-то(((
#     alice_string = alice_string.replace(letter, '')

alice_string_mod = ''            # убираем из текста все, кроме букв и пробелов
for i in alice_string:
    if i.isalpha() or i == ' ':
        alice_string_mod += i

alice_list = alice_string_mod.lower().split()          # переводим все буквы в нижний регистр, переводим строку в список

alice_list_long = [item for item in alice_list if len(item) > 4] # создаем новый список из слов длиной 5 символов и более

alice_uniq_words_dict = dict.fromkeys(set(alice_list_long))      # создаем словарь, в котором ключами будут неповторяющиеся слова длиной более 4 символов

for word in alice_list_long:                    # к ключам в словаре добавляем значения - сколько раз данное слово встречается в книге
    for key in alice_uniq_words_dict:
        if key == word:
            alice_uniq_words_dict[key] = alice_list_long.count(word)

num_list = [val for val in alice_uniq_words_dict.values()]    # создаем список из значений словаря

def get_key(dictionary: dict, value: int) -> str:   # функция по извлеканию ключа по значению
    for k, v in dictionary.items():
        if v == value:
            return k

top_count = 0
max_number = 0
top_count_index = 0
top_word = ''
top_words_list = []          # список с топовыми словами в порядке убывания их количества в книге
top_numbers_list = []        # список с количествами упоминаний топовых слов в тексте в порядке убывания

while top_count_index < 5:                                   # цикл, в котором мы формируем два вышеперечисленных списка 
    max_number = max(num_list)                               
    top_count = num_list.count(max_number)
    top_word = get_key(alice_uniq_words_dict, max_number)
    top_words_list.append(top_word)
    top_numbers_list.append(max_number)
    num_list.remove(max_number)
    top_count_index += top_count

# print(top_words_list)      # ['алиса', 'сказала', 'сказал', 'только', 'очень']
# print(top_numbers_list)    # [403, 126, 100, 87, 71]

#print(f"Топ 5 самых встречаемы слов в Алисе в стране чудес, длинна которых не меньше 5 букв: \n{top_words_list[0]} - {top_numbers_list[0]} раз, \n{top_words_list[1]} - {top_numbers_list[1]} раз, \n{top_words_list[2]} - {top_numbers_list[2]} раз, \n{top_words_list[3]} - {top_numbers_list[3]} раз, \n{top_words_list[4]} - {top_numbers_list[4]} раз.")

print('Топ 5 самых встречаемы слов в Алисе в стране чудес, длинна которых не меньше 5 букв:')
for i in range(len(top_words_list)):
    for j in range(len(top_numbers_list)):
        if i == j:
            print(f'{top_words_list[i]} - {top_numbers_list[j]} раз')