"""
Дана строка, возможно, содержащая пробелы. Определите количество слов в этой строке. Слово — это несколько (>0)
подряд идущих букв латинского алфавита (как заглавных, так и строчных).

Решение оформите в виде функции CountWords (S), возвращающее значение типа int. При решении этой задачи нельзя
пользоваться дополнительными строками и списками.
"""
def CountWords(S):
    counter = 0
    i = 0
    flag = 0
    while i < len(S):
        if flag == 0 and ((ord(S[i]) >= 65 and ord(S[i]) <= 90) or (ord(S[i]) >= 97 and ord(S[i]) <= 122)):
            flag = 1
            counter += 1
        elif S[i] == " ":
            flag = 0
        i += 1
    return  counter

our_string = input()

print(CountWords(our_string))