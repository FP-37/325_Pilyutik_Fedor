"""
Дана строка, в которой буква h встречается минимум два раза.
Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.
"""
# Ввод строки
input_string = input()

# Поиск индексов первого и последнего вхождения буквы 'h'
first_index = input_string.find('h')
last_index = input_string.rfind('h')

# Удаление первого вхождения и всех символов между ним и последним вхождением
input_string = input_string.replace(input_string[first_index:last_index + 1], '', 1)

# Удаление последнего вхождения
input_string = input_string.replace('h', '', last_index)

# Удаление первого вхождения, если оно осталось после предыдущего шага
input_string = input_string.replace('h', '', first_index)

# Вывод результата
print(input_string)