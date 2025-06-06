"""
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка.
"""
def main():
    # Ввод размеров массива
    n, m = map(int, input().strip().split())

    # Создание и заполнение двумерного массива
    chessboard = [["*" for j in range(m)] for i in range(n)]

    # Проверка, является ли сумма индексов строки и столбца четной
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                chessboard[i][j] = "."

    # Вывод массива
    for row in chessboard:
        print(" ".join(row))

if __name__ == "__main__":
    main()