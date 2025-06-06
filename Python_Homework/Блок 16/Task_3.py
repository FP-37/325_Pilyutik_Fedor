"""
Дано N целых чисел, которые требуется отсортировать в порядке неубывания.
В связи с нормами СЭС среди чисел не будет двух, разница между которыми превышает 10^7.

Входные данные
Первая строка входного файла содержит целое число N. (1 <= N <= 100000),
вторая строка – N целых чисел, не превышающих по модулю 2*10^9. Никакие два не различаются более, чем на 10^7.

Выходные данные
Выведите данные числа в порядке неубывания.

Примечание
Сложность работы программы должна быть O(n). Использование встроенной сортировки(sort, sorted),
алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!
"""
def count_sort_limited_range(arr):
    min_val = min(arr)
    range_size = 10**7 + 1
    count = [0] * range_size

    for num in arr:
        count[num - min_val] += 1

    result = []
    for i in range(range_size):
        result.extend([min_val + i] * count[i])
    return result

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr = count_sort_limited_range(arr)
    print(*arr)

if __name__ == "__main__":
    main()