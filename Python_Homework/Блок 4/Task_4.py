"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д.
"""
# Функция заполнения массива нулями
def arr_zeros(how_big):
    row = []
    for _ in range(how_big):
        row.append(0)
    return row

# Основная функция программы
def main():

    # Ввод размера списка и добавление пустого массива
    n = int(input().strip())
    array = []

    # Создание двумерного списка
    for _ in range(n):
        array.append(arr_zeros(n))

    # Реализация логики заполнения ячеек и вывод результата
    for index_1, row in enumerate(array):
        for index_2, column in enumerate(row):
            column = abs(index_2-index_1)
            row[index_2] = column
        print(*row)

if __name__ == "__main__":
    main()