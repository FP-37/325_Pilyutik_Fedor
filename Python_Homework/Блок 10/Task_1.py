"""
Выведите координаты наиболее удаленной от начала координат точки.

Входные данные
Программа получает на вход набор точек на плоскости.
Сначала задано количество точек n, затем идет последовательность из n строк,
каждая из которых содержит два числа: координаты точки. Величина n не превосходит 100,
все исходные координаты – целые числа, не превосходящие 10^3 по абсолютной величине.

Выходные данные
Выведите  координаты точки, наиболее удаленной от начала координат.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

class PointSet:
    def __init__(self, n):
        self.points = []
        self.n = n
        for _ in range(n):
            x, y = map(int, input().strip().split())
            self.points.append(Point(x, y))

    def find_furthest_point(self):
        furthest_point = self.points[0]
        for point in self.points:
            if point.get_distance() > furthest_point.get_distance():
                furthest_point = point
        return furthest_point

def main():
    # Ввод количества точек
    n = int(input().strip())

    # Создание объекта PointSet и нахождение наиболее удаленной точки
    point_set = PointSet(n)
    furthest_point = point_set.find_furthest_point()

    # Вывод координат наиболее удаленной точки
    print(furthest_point.x, furthest_point.y)

if __name__ == "__main__":
    main()