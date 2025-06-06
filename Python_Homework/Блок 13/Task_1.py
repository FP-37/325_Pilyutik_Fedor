"""
Реализуйте алгоритм бинарного поиска.

Входные данные
В первой строке входных данных содержатся натуральные числа N и K (0<N,K≤100000).
Во второй строке задаются N элементов первого массива, отсортированного по возрастанию,
а в третьей строке – K элементов второго массива. Элементы обоих массивов - целые числа, каждое из которых
по модулю не превосходит 10^9.

Выходные данные
Требуется для каждого из K чисел вывести в отдельную строку "YES", если это число встречается в первом массиве,
и "NO" в противном случае.
"""
def binary_search(n, k, arr):

    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            return True
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return False

def main():
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    for query in map(int, input().strip().split()):
        if binary_search(n, query, arr):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()