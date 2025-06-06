"""
Назовем натуральное число почти простым, если оно раскладывается на произведение каких-нибудь двух неравных простых.

Входные данные
Дано одно натуральное число n (2 ≤ n ≤ 2*10^9).

Выходные данные
Выведите «YES», если n почти простое. Иначе выведите «NO»
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

def is_almost_prime(n):
    limit = int(n**0.5) + 1
    primes = sieve_of_eratosthenes(limit)

    for p in primes:
        if n % p == 0:
            quotient = n // p
            if quotient != p and is_prime(quotient):
                return "YES"
    return "NO"

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

result = is_almost_prime(n)
print(result)