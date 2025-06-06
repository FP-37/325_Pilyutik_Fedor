"""
Выведите диаметр данного множества – максимальное расстояние между любыми двумя точками.

Создайте структуру Point и сохраните исходные данные в массиве структур Point.

Входные данные
Программа получает на вход набор точек на плоскости. Сначала задано количество точек n,
затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки.
Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие 10^3.

Выходные данные
Необходимо вывести диаметр данного множества с точностью в 15 значащих цифр.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class PointSet:
    def __init__(self, n):
        self.points = []
        self.n = n
        for _ in range(n):
            x, y = map(int, input().strip().split())
            self.points.append(Point(x, y))

    def calculate_diameter(self):
        # Инициализация переменных для хранения минимального и максимального расстояния
        max_dist = self.points[0].get_distance(self.points[1])

        # Вычисление расстояний между всеми парами точек
        for i, p1 in enumerate(self.points):
            for p2 in self.points[i+1:]:
                dist = p1.get_distance(p2)
                if dist > max_dist:
                    max_dist = dist

        return max_dist

def main():
    # Ввод количества точек
    n = int(input().strip())

    # Создание объекта PointSet и нахождение диаметра
    point_set = PointSet(n)
    diameter = point_set.calculate_diameter()

    # Вывод диаметра
    print(diameter)

if __name__ == "__main__":
    main()