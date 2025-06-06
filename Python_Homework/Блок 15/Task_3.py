"""
Найдите корень уравнения sin(x)=a на отрезке [-π/2,π/2].

Входные данные
Вводится одно вещественное число а, по модулю не превосходящее 1.

Выходные данные
Выведите корень уравнения с точностью не менее 5 знаков после запятой.
"""
import math

def binary_search(a):
    if abs(a) > 1:
        return None

    left = -math.pi / 2
    right = math.pi / 2

    while right - left > 1e-6:
        mid = (left + right) / 2
        # Я старался избегать модуля math из-за незнания, можно ли его использовать
        # Но при появлении синуса уже точно надо
        if math.sin(mid) < a:
            left = mid
        else:
            right = mid

    return (left + right) / 2

def main():
    a = float(input().strip())
    root = binary_search(a)
    print(root)

if __name__ == "__main__":
    main()