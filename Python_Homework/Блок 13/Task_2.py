"""
Входные данные
В первой строке входных данных содержатся числа N и K (0<N,K<100001).
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию,
а в третьей строке – K чисел второго массива. Каждое число в обоих массивах по модулю не превосходит 2⋅10^9.

Выходные данные
Для каждого из K чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному.
Если таких несколько, выведите меньшее из них.
"""
def approximate_binary_search(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = left+(right-left)//2
        if array[mid] == target:
            return array[mid]
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1

    if left > len(array)-1:
        return array[-1]
    elif left == 0:
        return array[0]
    elif target - array[left-1] <= array[left]-target:
        return array[left-1]
    else:
        return array[left]


def main():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    for query in queries:
        closest_value = approximate_binary_search(array, query)
        print(closest_value)

if __name__ == "__main__":
    main()