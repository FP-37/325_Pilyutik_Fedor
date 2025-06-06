"""

Максимальное время работы на одном тесте:	1 секунда
Дана таблица, состоящая из N строк и M столбцов. В каждой клетке таблицы записано одно из чисел: 0 или 1.
Расстоянием между клетками (x1, y1) и (x2, y2) назовем сумму |x1-x2|+|y1-y2|. Вам необходимо построить таблицу,
в клетке (i, j) которой будет записано минимальное расстояние между клеткой (i, j) начальной таблицы и клеткой,
в которой записана 1. Гарантируется, что хотя бы одна 1 в таблице есть.

Входные данные
В первой строке вводятся два натуральных числа N и M, не превосходящих 500.
Далее идут N строк по M чисел - элементы таблицы.

Выходные данные
Требуется вывести N строк по M чисел - элементы искомой таблицы.
"""
from collections import deque

def bfs_min_distance(N, M, grid):
    dist = [[float('inf')] * M for _ in range(N)]

    queue = deque()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j))
                dist[i][j] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == float('inf'):
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

result = bfs_min_distance(N, M, grid)

for row in result:
    print(" ".join(map(str, row)))