"""
Найдите такое число x, что x^2+√x=C, с точностью не менее 6 знаков после точки.

Входные данные
В единственной строке содержится вещественное число 1.0≤C≤1010.

Выходные данные
Выведите одно число — искомый x.
"""
import math

def solve_equation(C):
    if C < 0:
        return None

    low = 0.0
    high = max(1.0, C)

    while high - low > 1e-7:
        mid = (low + high) / 2
        f_mid = mid**2 + math.sqrt(mid) - C

        if f_mid == 0:
            return mid
        elif f_mid < 0:
            low = mid
        else:
            high = mid

    return (low + high) / 2

def main():
    C = float(input())
    solution = solve_equation(C)
    print(f"{solution:.8f}")

if __name__ == "__main__":
    main()