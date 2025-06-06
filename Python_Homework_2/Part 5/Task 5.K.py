"""
Выведите все числа в диапазоне от 2 до N, у которых есть хотя бы три различных простых делителя.

Входные данные
Вводится одно натуральное число N, не превосходящее 100000.

Выходные данные
Выведите через пробел в возрастающем порядке все искомые числа.
"""
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    primes = []
    is_prime[0] = is_prime[1] = False

    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    return primes

def count_unique_prime_factors(limit):
    prime_count = [0] * (limit + 1)

    primes = sieve_of_eratosthenes(limit)

    for prime in primes:
        for multiple in range(prime, limit + 1, prime):
            prime_count[multiple] += 1

    return prime_count

N = int(input())

unique_prime_factors_count = count_unique_prime_factors(N)

result = [i for i in range(2, N + 1) if unique_prime_factors_count[i] >= 3]

print(" ".join(map(str, result)))