"""
Простой неориентированный граф задан матрицей смежности, выведите его представление в виде списка ребер.

Входные данные
Входные данные включают число n (1≤n≤100) – количество вершин в графе, а затем n строк по n чисел,
каждое из которых равно 0 или 1, – его матрицу смежности.

Выходные данные
Выведите  список ребер заданного графа (в любом порядке).
"""
n = int(input().strip())
adjacency_matrix = [list(map(int, input().strip().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i + 1, n):
        if adjacency_matrix[i][j] == 1:
            edges.append((i + 1, j + 1))
for edge in edges:
    print(edge[0], edge[1])