"""
Отсортируйте данный массив, используя сортировку слиянием.

Входные данные
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 10^5. Далее идет N целых чисел,
не превосходящих по абсолютной величине 10^9.

Выходные данные
Выведите эти числа в порядке неубывания.
"""
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def main():
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    sorted_arr = merge_sort(arr)
    print(*sorted_arr)

if __name__ == "__main__":
    main()