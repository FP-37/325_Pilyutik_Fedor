"""
Проверьте, является ли число простым.

Входные данные
Вводится одно натуральное число n не превышающее 2000000000 и не равное 1.

Выходные данные
Необходимо вывести  строку prime, если число простое, или composite, если число составное.
"""
import math

n = int(input())

if n <= 1:
    print("composite")
elif n == 2:
    print("prime")
elif n % 2 == 0:
    print("composite")
else:
    is_prime = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime")
    else:
        print("composite")