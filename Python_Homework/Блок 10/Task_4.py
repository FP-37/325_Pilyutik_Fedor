"""
Выведите все исходные точки в порядке возрастания их расстояний от начала координат.

Создайте структуру Point и сохраните исходные данные в массиве структур Point.

Входные данные
Программа получает на вход набор точек на плоскости. Сначала задано количество точек n,
затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки.
Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие 10^3.

Выходные данные
Необходимо вывести все исходные точки в порядке возрастания их расстояний от начала координат.
Программа выводит только координаты точек, их количество выводить не надо.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

class PointSet:
    def __init__(self, n):
        self.points = []
        self.n = n
        for _ in range(n):
            x, y = map(int, input().strip().split())
            self.points.append(Point(x, y))

    def sort_points_by_distance(self):
        # Инициализация списка расстояний
        distances = []

        # Вычисление расстояний от начала координат до каждой точки
        for point in self.points:
            distances.append(point.get_distance_from_origin())

        # Сортировка списка точек по расстоянию
        sorted_points = sorted(self.points, key=lambda point: point.get_distance_from_origin())

        # Вывод отсортированных точек
        for point in sorted_points:
            print(f"{point.x} {point.y}")

def main():
    # Ввод количества точек
    n = int(input().strip())

    # Создание объекта PointSet и сортировка точек по расстоянию
    point_set = PointSet(n)
    point_set.sort_points_by_distance()

if __name__ == "__main__":
    main()