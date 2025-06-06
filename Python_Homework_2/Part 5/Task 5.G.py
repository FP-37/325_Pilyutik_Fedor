"""
По введенному натуральному числу K, не превосходящему 1 000 000, выдать K-ое по счету простое число.

Входные данные
Во входном файле находится одно натуральное число K.

Выходные данные
В выходной файл выведите K-е простое число.
"""
def nth_prime_sieve(k):
    import math
    if k < 6:
        upper = 15
    else:
        upper = int(k * math.log(k) + k * math.log(math.log(k))) + 10

    sieve = [True] * (upper + 1)
    sieve[0:2] = [False, False]
    primes = []

    for i in range(2, upper + 1):
        if sieve[i]:
            primes.append(i)
            if len(primes) == k:
                return i
            for j in range(i * i, upper + 1, i):
                sieve[j] = False

with open('input.txt', 'r') as f:
    k = int(f.read().strip())

prime = nth_prime_sieve(k)

with open('output.txt', 'w') as f:
    f.write(str(prime))
