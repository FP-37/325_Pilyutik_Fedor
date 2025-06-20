"""
Дана дробь a/b.
Требуется ее сократить, то есть записать это же число в виде c/d,
где c — целое число, d — натуральное число и d минимальное возможное.

Входные данные
Вводятся два целых числа a и b (–100≤a≤100, 0<b≤100).

Выходные данные
Выведите два числа c и d.

Оценка задачи

1 балл получат программы, правильно решающие задачу для случая положительного числа a.
"""
import math

def simplify_fraction(a, b):
    g = math.gcd(a, b)

    c = a // g
    d = b // g

    if d < 0:
        c = -c
        d = -d

    return c, d

a, b = map(int, input().split())

c, d = simplify_fraction(a, b)

print(c, d)