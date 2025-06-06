"""
Даны две рациональные дроби: a/b и c/d. Сложите их и результат представьте в виде несократимой дроби m/n.

Входные данные
Программа получает на вход 4 натуральных числа a, b, c, d, не превосходящих 100.

Выходные данные
Программа должна вывести 2 натуральных числа m и n такие, что m/n=a/b+c/d и дробь m/n – несократима.
"""
import math

def add_fractions(a, b, c, d):
    common_denominator = b * d
    numerator = a * d + c * b

    gcd = math.gcd(numerator, common_denominator)

    m = numerator // gcd
    n = common_denominator // gcd

    return m, n

a, b, c, d = map(int, input().split())

m, n = add_fractions(a, b, c, d)

print(m, n)