"""
Дана строка, состоящая из n цифр (т.е. однозначных чисел), между которыми стоит n−1 знак операции, каждый из которых
может быть либо +, либо -. Вычислите значение данного выражения.

Решение оформите в виде функции Evaluate(S), где S - строка с выражением, а возвращаемое значение функции - результат
вычисления этого выражения.
"""
def Evaluate(S):
    counter = 0
    alg_sum = 0
    while counter <= len(S)-1:
        if S[counter] != "+" and S[counter] != "-":
            if S[counter-1] != "-":
                alg_sum += int(S[counter])
            else:
                alg_sum -= int(S[counter])
        counter += 1
    return alg_sum

our_string = input()
print(Evaluate(our_string))