"""
Вывести все простые числа от M до N включительно.

Входные данные
В первой строке находятся разделённые пробелом M и N. 2 <= M <= N <= 1 000 000.

Выходные данные
Вывести числа в порядке возрастания, по одному в строке. Если между M и N включительно нет простых - вывести "Absent".
"""
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return is_prime

M, N = map(int, input().split())

is_prime = sieve_of_eratosthenes(N)

primes_in_range = [i for i in range(M, N + 1) if is_prime[i]]

if primes_in_range:
    for prime in primes_in_range:
        print(prime)
else:
    print("Absent")