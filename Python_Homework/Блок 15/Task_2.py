"""
Дано кубическое уравнение a(x^3)+b(x^2)+cx+d=0 (a≠0).
Известно, что у этого уравнения ровно один корень. Требуется его найти.

Входные данные
Во входных данных через пробел записаны четыре целых числа: −1000≤a,b,c,d≤1000.

Выходные данные
Выведите единственный корень уравнения с точностью не менее 4 знаков после десятичной точки.
"""
def cubic_equation_root(a, b, c, d):

    def cubic_equation(x, a, b, c, d):
        return a * (x**3) + b * (x**2) + c * x + d

    low = -100
    high = 100

    while high - low > 0.0001:
        mid = (low + high) / 2
        value = cubic_equation(mid, a, b, c, d)

        if value == 0:
            return mid

        if value > 0:
            high = mid
        else:
            low = mid

    return (low + high) / 2

def main():
    a, b, c, d = map(int, input().strip().split())
    root = cubic_equation_root(a, b, c, d)
    print(root)

if __name__ == "__main__":
    main()