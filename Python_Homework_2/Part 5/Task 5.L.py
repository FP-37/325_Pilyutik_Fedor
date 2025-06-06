"""
На входе программе даются два числа N и P. Программа на выходе должна дать такое максимальное число M, что N!
делится на PM

Входные данные
Дано два числа N и P (2 ≤ N, P ≤ 10^7)

Выходные данные
Выведите число M
"""
def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

def count_factors_in_factorial(n, p):
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

N, P = map(int, input().split())

factors = prime_factors(P)

min_M = float('inf')

for prime, exponent in factors.items():
    count = count_factors_in_factorial(N, prime)
    M = count // exponent
    min_M = min(min_M, M)

print(min_M)