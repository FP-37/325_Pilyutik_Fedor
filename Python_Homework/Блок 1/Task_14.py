"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

В этой задаче можно использовать циклы.

Символы строки нумеруются, начиная с нуля.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.
"""
# Ввод строки
input_string = input()

# Счётчик и новая строка
counter = 0
new_string = ""

# Удаление символов по условию
for letter in input_string:
    if counter%3 != 0:
        new_string += letter
    counter += 1

# Вывод результата
print(new_string)