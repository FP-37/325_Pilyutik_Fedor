"""
Простой неориентированный граф задан списком ребер, выведите его представление в виде матрицы смежности.

Входные данные
На вход программы поступают числа n (1≤n≤100) – количество вершин в графе и m (1≤m≤n(n−1)/2) – количество ребер.
Затем следует m пар чисел – ребра графа.

Выходные данные
Выведите матрицу смежности заданного графа.
"""
n, m = map(int, input().strip().split())

adjacency_matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().strip().split())
    adjacency_matrix[u - 1][v - 1] = 1
    adjacency_matrix[v - 1][u - 1] = 1

for row in adjacency_matrix:
    print(' '.join(map(str, row)))