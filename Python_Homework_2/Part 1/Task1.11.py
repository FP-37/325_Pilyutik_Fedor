"""
Ориентированный граф задан матрицей смежности, выведите его представление в виде списка ребер.

Входные данные
На вход программы поступает число n (1≤n≤100) – количество вершин графа, а затем n строк по n чисел,
каждое из которых равно 0 или 1, – его матрица смежности.

Выходные данные
Выведите список ребер заданного графа.
"""
n = int(input().strip())

adjacency_matrix = [list(map(int, input().strip().split())) for _ in range(n)]

edges = []

for i in range(n):
    for j in range(n):
        if adjacency_matrix[i][j] == 1:
            edges.append((i + 1, j + 1))

for edge in edges:
    print(edge[0], edge[1])