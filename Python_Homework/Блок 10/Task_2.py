"""
Выведите координаты центра тяжести данного множества точек.

Создайте структуру Point и сохраните исходные данные в массиве структур Point.

Входные данные
Программа получает на вход набор точек на плоскости. Сначала задано количество точек n,
затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки.
Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие 10^3.

Выходные данные
Выведите  координаты центра тяжести данного множества точек. Ответ необходимо выводить с точностью в 15 значащих цифр.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"

class PointSet:
    def __init__(self, n):
        self.points = []
        self.n = n
        for _ in range(n):
            x, y = map(int, input().strip().split())
            self.points.append(Point(x, y))

    def center_of_gravity(self):
        # Инициализация переменных для хранения суммы координат
        x_sum = 0
        y_sum = 0

        # Суммирование координат всех точек
        for point in self.points:
            x_sum += point.x
            y_sum += point.y

        # Вычисление координат центра тяжести
        total_mass = self.n  # Предполагаем равномерное распределение массы
        x_gravity = x_sum / total_mass
        y_gravity = y_sum / total_mass

        return Point(x_gravity, y_gravity)

def main():
    # Ввод количества точек
    n = int(input().strip())

    # Создание объекта PointSet и нахождение центра тяжести
    point_set = PointSet(n)
    center_of_gravity = point_set.center_of_gravity()

    # Вывод координат центра тяжести
    print(center_of_gravity)

if __name__ == "__main__":
    main()