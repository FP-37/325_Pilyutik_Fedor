"""
Многоугольник на плоскости задан целочисленными координатами своих N вершин в декартовой системе координат.
Требуется найти количество точек с целочисленными координатами, лежащих на границе многоугольника.
Стороны многоугольника друг с другом не соприкасаются (за исключением соседних - в вершинах) и не пересекаются.

Ограничения: 3 <= N <= 100 000, координаты вершин целые и по модулю не превосходят 1 000 000 000.

Входные данные
В первой строке содержится число N, в следующих N строках - пары чисел - координаты точек.
Если соединить точки в данном порядке, а также соединить первую и последнюю точки, получится заданный многоугольник.

Выходные данные
Вывести одно число - количество точек с целочисленными координатами на границе многоугольника.
"""
import sys
import math

def count_integer_points_on_polygon_boundary(vertices):
    total_points = 0
    N = len(vertices)

    for i in range(N):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % N]
        total_points += math.gcd(abs(x2 - x1), abs(y2 - y1))

    return total_points

def main():
    input = sys.stdin.read
    data = input().strip().splitlines()

    N = int(data[0])
    vertices = []

    for i in range(1, N + 1):
        x, y = map(int, data[i].split())
        vertices.append((x, y))

    result = count_integer_points_on_polygon_boundary(vertices)
    print(result)

if __name__ == "__main__":
    main()