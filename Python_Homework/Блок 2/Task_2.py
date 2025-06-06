"""
Дана строка, возможно, содержащая пробелы. Извлеките из этой строки все символы, являющиеся цифрами и составьте
из них новую строку. Решение оформите в виде функции ExtractDigits (S)

Входные данные
Программа получает на вход исходную строку S

Выходные данные
Требуется вывести новую строку, содержащую только цифры данной строки.
"""
def ExtractDigits(S):
    new_string = ""
    for sim in S:
        for digit in "0123456789":
            if sim == digit:
                new_string += sim
    return new_string

our_string = input()

print(ExtractDigits(our_string))