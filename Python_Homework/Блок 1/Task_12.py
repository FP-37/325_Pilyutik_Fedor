"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.
"""
# Ввод строки
input_string = input()

# Добавим счётчик символов и строку, которую в дальнейшем будем выводить
counter = 0
new_string = ""

# Первое вхождение буквы h
first_index = input_string.find('h')

# Последнее вхождение буквы h
last_index = input_string.rfind('h')

# Замена всех вхождений h на H, кроме первого и последнего
for letter in input_string:
    if counter > first_index and counter < last_index:
        if letter == "h":
            letter = "H"
    new_string += letter
    counter += 1

# Вывод результата
print(new_string)