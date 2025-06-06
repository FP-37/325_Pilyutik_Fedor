"""
Дано N чисел, требуется выяснить, сколько среди них различных.

Входные данные
В первой строке дано число N – количество чисел. (1 <= N <= 100000)
Во второй строке даны через пробел N чисел, каждое не превышает 2*10^9 по модулю.

Выходные данные
Выведите число, равное количеству различных чисел среди данных.
"""
def main():
    N = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    numbers.sort()
    unique_numbers = []
    for num in numbers:
        if not unique_numbers or num > unique_numbers[-1]:
            unique_numbers.append(num)
    distinct_numbers = len(unique_numbers)
    print(distinct_numbers)

if __name__ == "__main__":
    main()