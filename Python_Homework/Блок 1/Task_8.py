"""
Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
заключенную между первым и последнием появлением буквы h, в противоположном порядке.

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

# Извлечение подстроки между первым и последним вхождением
substring = input_string[first_index + 1:last_index]

# Разворот подстроки
reversed_substring = substring[::-1]

# Замена подстроки развернутой версией
input_string = input_string.replace(substring, reversed_substring)

# Вывод результата
print(input_string)