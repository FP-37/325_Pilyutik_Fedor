"""
В подземелье M тоннелей и N перекрестков, каждый тоннель соединяет какие-то два перекрестка.
Мышиный король решил поставить по светофору в каждом тоннеле перед каждым перекрестком. Напишите программу,
которая посчитает, сколько светофоров должно быть установлено на каждом из перекрестков. Перекрестки пронумерованы
числами от 1 до N.

Входные данные
Первая строка входных данных содержит два числа N и M (0 < N ≤ 100, 0 ≤ M ≤ N*(N – 1)/2). В каждой из следующих M строк
записаны по два числа i и j (1 ≤ i,j ≤ N), которые означают, что перекрестки i и j соединены тоннелем.

Выходные данные
Требуется вывести N чисел: k-ое число означает количество светофоров на k-ом перекрестке.

Примечание. Можно считать, что любые два перекрестка соединены не более, чем одним тоннелем. Нет тоннелей от перекрестка
i до него самого.
"""
N, M = map(int, input().strip().split())
sс = [0] * N
for _ in range(M):
    i, j = map(int, input().strip().split())
    sс[i - 1] += 1
    sс[j - 1] += 1

print(" ".join(map(str, sс)))