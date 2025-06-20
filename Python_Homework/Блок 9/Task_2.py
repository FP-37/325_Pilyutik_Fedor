"""
Требуется отсортировать массив по неубыванию методом "выбор максимума".

Входные данные
В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива.
Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести получившийся массив.
"""
def main():
    # Ввод размера массива
    n = int(input().strip())

    # Ввод элементов массива
    array = list(map(int, input().strip().split()))

    # Сортировка массива методом выбора максимума
    for i in range(n-1, 0, -1):
        max_index = i
        for j in range(0, i):
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]

    # Выводим получившийся массив
    print(*array)

if __name__ == "__main__":
    main()