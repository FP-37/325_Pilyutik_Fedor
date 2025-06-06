"""
Дан неориентированный невзвешенный граф. Необходимо определить, является ли он деревом.

Входные данные
В первой строке входного файла содержится одно натуральное число N (N ≤ 100) - количество вершин в графе.
Далее в N строках по N чисел - матрица смежности графа: в i-ой строке на j-ом месте стоит 1, если вершины i и j
соединены ребром, и 0, если ребра между ними нет. На главной диагонали матрицы стоят нули.
Матрица симметрична относительно главной диагонали.

Выходные данные
Вывести "YES", если граф является деревом, и "NO" иначе.
"""
def dfs(vertex, visited, graph):
    visited.add(vertex)
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and neighbor not in visited:
            dfs(neighbor, visited, graph)

def is_tree(graph):
    N = len(graph)

    edges_count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if graph[i][j] == 1:
                edges_count += 1

    if edges_count != N - 1:
        return "NO"

    visited = set()
    dfs(0, visited, graph)

    if len(visited) == N:
        return "YES"
    else:
        return "NO"

N = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

result = is_tree(graph)
print(result)