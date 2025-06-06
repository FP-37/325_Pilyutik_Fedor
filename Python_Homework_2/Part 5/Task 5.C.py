"""
Выведите все натуральные делители числа x в порядке возрастания (включая 1 и само число).

Входные данные
Вводится натуральное число x

Выходные данные
Выведите все делители числа x
"""
import math

x = int(input())
divisors = []

for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        divisors.append(i)
        if i != x // i:
            divisors.append(x // i)

divisors.sort()
print(" ".join(map(str, divisors)))