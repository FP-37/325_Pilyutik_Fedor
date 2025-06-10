import os
import random
import math

def generate_primes(limit=10**6, filename="primes.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return [int(line.strip()) for line in f if line.strip().isdigit()]

    # Генерация простых чисел решетом Эратосфена
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    with open(filename, "w") as f:
        for p in primes:
            f.write(f"{p}\n")

    return primes


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0


def generate_keypair(primes):
    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi) != 1:
        e = random.choice(range(3, phi, 2))

    d = modinv(e, phi)
    return ((e, n), (d, n))


def encrypt(message, pub_key):
    e, n = pub_key
    return [pow(ord(char), e, n) for char in message]


def decrypt(cipher, priv_key):
    d, n = priv_key
    return ''.join([chr(pow(c, d, n)) for c in cipher])
