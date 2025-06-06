"""
Дано два массива. Для каждого элемента второго массива определите, сколько раз он встречается в первом массиве.

Входные данные
Первая строка входных данных содержит одно число N (1 ≤ N ≤ 10^5) – количество элементов в первом массиве.
Далее идет N целых чисел, не превосходящих по модулю 10^9 – элементы первого массива.
Далее идет количество элементов M во втором массиве и M элементов второго массива с такими же ограничениями.

Выходные данные
Выведите M чисел: для каждого элемента второго массива выведите,
сколько раз такое значение встречается в первом массиве.
"""
def binary_search_first(arr, x):
    low, high = 0, len(arr) - 1
    first_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            first_index = mid
            high = mid - 1
    return first_index

def binary_search_last(arr, x):
    low, high = 0, len(arr) - 1
    last_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
            last_index = mid
        else:
            high = mid - 1
    return last_index


def count_occurrences(arr, x):
    first_index = binary_search_first(arr, x)
    if first_index == -1:
        return 0
    last_index = binary_search_last(arr, x)
    return last_index - first_index + 1

def main():
    N = int(input())
    first_array = list(map(int, input().split()))
    M = int(input())
    second_array = list(map(int, input().split()))

    first_array.sort()

    result = []
    for x in second_array:
        result.append(count_occurrences(first_array, x))

    print(*result)

if __name__ == "__main__":
    main()