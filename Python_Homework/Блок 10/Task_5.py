"""
Среди исходных точек найдите три, образующие треугольник с максимальным периметром. Выведите данный периметр.

Входные данные
Программа получает на вход набор точек на плоскости. Сначала задано количество точек n (2<n<101),
затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки.
Все исходные координаты – целые числа, не превосходящие 10^3.

Выходные данные
Необходимо вывести найденный периметр с точностью в 15 значащих цифр.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_from_other_point(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_perimeter(self):
        a = self.p1.get_distance_from_other_point(self.p2)
        b = self.p2.get_distance_from_other_point(self.p3)
        c = self.p3.get_distance_from_other_point(self.p1)
        return a + b + c

class PointSet:
    def __init__(self, n):
        self.points = []
        self.n = n
        for _ in range(n):
            x, y = map(int, input().strip().split())
            self.points.append(Point(x, y))

    def find_max_perimeter_triangle(self):
        # Инициализация переменных для хранения треугольника с максимальным периметром
        max_triangle = Triangle(self.points[0], self.points[1], self.points[2])
        max_perimeter = max_triangle.get_perimeter()

        # Поиск всех возможных комбинаций трёх точек и вычисление периметров треугольников
        for i in range(self.n - 2):
            for j in range(i + 1, self.n - 1):
                for k in range(j + 1, self.n):
                    triangle = Triangle(self.points[i], self.points[j], self.points[k])
                    perimeter = triangle.get_perimeter()
                    if perimeter > max_perimeter:
                        max_triangle = triangle
                        max_perimeter = perimeter

        # Вывод периметра треугольника с максимальным периметром
        print(max_perimeter)

def main():
    # Ввод количества точек
    n = int(input().strip())

    # Создание объекта PointSet и нахождение треугольника с максимальным периметром
    point_set = PointSet(n)
    point_set.find_max_perimeter_triangle()

if __name__ == "__main__":
    main()