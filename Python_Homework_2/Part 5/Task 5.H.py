"""
Вывести все простые числа от M до N включительно.

Входные данные
В первой строке находятся разделённые пробелом M и N. 2 <= M <= N <= 300 000.

Выходные данные
Вывести числа в порядке возрастания, по одному в строке. Если между M и N включительно нет простых - вывести "Absent".
"""
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]

M, N = map(int, input().split())

primes = sieve_of_eratosthenes(N)

filtered_primes = [p for p in primes if M <= p <= N]

if filtered_primes:
    for prime in filtered_primes:
        print(prime)
else:
    print("Absent")