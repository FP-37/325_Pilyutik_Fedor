"""
Дана строка, в которой буква h встречается как минимум два раза. Повторите последовательность символов,
заключенную между первым и последнием появлением буквы h два раза, сами буквы h повторять не надо.

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

# Извлечение текста до последнего 'h' (не включая его)
if last_index != -1:
    start_index = 0
    end_index = last_index
    before_last_h = input_string[start_index:end_index]
else:
    before_last_h = input_string

# Извлечение текста после первого 'h' (не включая его)
if first_index != -1:
    start_index = first_index + 1
    end_index = None
    after_first_h = input_string[start_index:end_index]
else:
    after_first_h = input_string

# Вывод результата
print(before_last_h + after_first_h)

#Почему в примере теста на выходе не последовательность символов,
#заключенная между первым и последнием появлением буквы h два раза,
#а введённая строка до последнего h + введённая строка после первого h? На какое условие опираться?