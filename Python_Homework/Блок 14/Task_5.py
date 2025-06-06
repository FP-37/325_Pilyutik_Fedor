"""
Сегодня утром жюри решило добавить в вариант олимпиады еще одну, Очень Легкую Задачу.
Ответственный секретарь Оргкомитета напечатал ее условие в одном экземпляре,
и теперь ему нужно до начала олимпиады успеть сделать еще N копий. В его распоряжении имеются два ксерокса,
один из которых копирует лист за х секунд, а другой – за y.
(Разрешается использовать как один ксерокс, так и оба одновременно.
Можно копировать не только с оригинала, но и с копии.)
Помогите ему выяснить, какое минимальное время для этого потребуется.

Входные данные
На вход программы поступают три натуральных числа N, x и y, разделенные пробелом (1 ≤ N ≤ 2∙10^8, 1 ≤ x, y ≤ 10).

Выходные данные
Выведите одно число – минимальное время в секундах, необходимое для получения N копий.
"""
def can_make_copies_in_time(n, x, y, time_limit):
    copies = 0
    while time_limit > 0:
        copies_x = time_limit // x
        copies_y = time_limit // y
        copies += copies_x + copies_y
        time_limit -= copies_x * x + copies_y * y
        if copies >= n:
            return True
    return copies >= n

def min_time(n, x, y):
    left, right = 1, n * min(x, y)
    while left < right:
        mid = (left + right) // 2
        if can_make_copies_in_time(n, x, y, mid):
            right = mid
        else:
            left = mid + 1
    return left

def main():
    n, x, y = map(int, input().strip().split())
    print(min_time(n, x, y))

if __name__ == "__main__":
    main()