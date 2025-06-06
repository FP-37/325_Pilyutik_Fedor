"""
Дано выражение одно из следующих видов: “A+B”, “A-B” или “A*B”, где A и B - целые числа от 0 до 10^9.
Определите значение этого выражения.

Решение оформите в виде функции Eval(S).
"""
def Eval(S):

    if "+" in S:
        plus_index = S.find("+")
        result = int(S[:plus_index]) + int(S[plus_index+1:])
    elif "-" in S:
        minus_index = S.find("-")
        result = int(S[:minus_index]) - int(S[minus_index+1:])
    else:
        multi_index = S.find("*")
        result = int(S[:multi_index]) * int(S[multi_index+1:])

    return result

our_string = input()

print(Eval(our_string))