"""
Вывести в порядке возрастания все несократимые дроби, заключённые между 0 и 1, знаменатели которых не превышают N.

Входные данные
В первой строке находится единственное число N. 2 <= N <= 255.

Выходные данные
В каждой строке выводится дробь.
"""
import math

def find_irreducible_fractions(N):
    fractions = []

    for b in range(2, N + 1):
        for a in range(1, b):
            if math.gcd(a, b) == 1:
                fractions.append((a, b))

    fractions.sort(key=lambda x: x[0] / x[1])

    return fractions

N = int(input())

result_fractions = find_irreducible_fractions(N)

for numerator, denominator in result_fractions:
    print(f"{numerator}/{denominator}")