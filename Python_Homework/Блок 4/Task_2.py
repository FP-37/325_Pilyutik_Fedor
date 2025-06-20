"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."
(каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива,
средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать
изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""
def main():
    n = int(input())
    array = [['.'] * n for _ in range(n)]

    # Заполним строки звёздочками
    mid_row = n // 2
    mid_col = n // 2
    for i in range(n):
        array[mid_row][i] = "*"
        array[mid_row][i] = "*"
        array[i][mid_col] = "*"
        array[i][i] = "*"
        array[i][n - i - 1] = "*"

    # Вывод массива с разделением элементов пробелами
    for row in array:
        print(' '.join(row))

if __name__ == "__main__":
    main()