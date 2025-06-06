"""
Дан список из N (N≤2∗10^5) элементов, которые принимают целые значения от 0 до 100.
Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.\
Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.

Примечание
Сложность работы программы должна быть O(n). Использование встроенной сортировки(sort, sorted),
алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!
"""
def CountSort(A):
    k = 101
    count = [0] * k
    output = [0] * len(A)
    for x in A:
        count[x] += 1
    for i in range(1, k):
        count[i] += count[i - 1]

    for i in range(len(A) - 1, -1, -1):
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1

    return output

def main():
    A = list(map(int, input().strip().split()))
    print(*CountSort(A))

if __name__ == "__main__":
    main()