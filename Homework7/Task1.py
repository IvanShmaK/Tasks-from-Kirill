"""1. Реализовать алгоритм RLE (упрощенный - это на случай вдруг вы полезете в Wiki) что такое RLE? алгоритм сжатия данных, например
ssssdddfffffgggggggghhkkk -> 4s3d5f8g2h3k
запаковка и распаковка в обратную сторону делаем файл с рандомно созданными строками (как запакованными, так и распакованными)
считываем файл функция определяет - запакована строка или распакована и выполнить соответствующий алгоритм - результаты записать в новый файл"""


with open('Files for Task1/Start file.txt', 'r', encoding='UTF-8') as data_file:
    user_start_file = data_file.readlines()   # делаем список из строк начального файла

def is_string_compressed(string: str) -> bool:    # функция, которая определяет, сжата строка, или нет
    if string[0].isdigit():
        return True         # строка сжата
    return False            # строка не сжата

def compress_string(uncompressed_str: str, count: int = 1, compressed_str: str = '') -> str:   # функция по запаковке строки
    uncompressed_str = uncompressed_str + ' '     # прибавляем пробел в конце, чтобы не выходить за пределы строки                                             
    for i in range(len(uncompressed_str) - 1):
        if uncompressed_str[i] == uncompressed_str[i + 1]:
            count += 1
        else:
            compressed_str += str(count) + uncompressed_str[i]
            count = 1
    return compressed_str

def uncompress_string(compressed_str: str, uncompressed_str: str = '', count: str = '') -> str:   # функция по распаковке строки
    compressed_str = compressed_str + ' '   # прибавляем пробел в конце, чтобы не выходить за пределы строки
    for i in range(len(compressed_str) - 1):
        if compressed_str[i].isdigit():
            count += compressed_str[i]
        else:
            uncompressed_str += int(count) * compressed_str[i]
            count = '' 
    return uncompressed_str

user_finish_file = []     # создаем список, куда будем добавлять переделанные строки

for item in user_start_file:     # сжатые строки распаковываем, и наоборот, после чего добавляем в созданный список
    if is_string_compressed(item.rstrip()):
        user_finish_file.append(uncompress_string(item.rstrip()) + '\n')
    else:
        user_finish_file.append(compress_string(item.rstrip()) + '\n')

with open('Files for Task1/Finish file.txt', 'w', encoding='UTF-8') as data_1_file:
    for item in user_finish_file:   # поочерезно записываем переделанные строки в финальный файл
        data_1_file.write(item)