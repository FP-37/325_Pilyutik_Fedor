"""
Максимальное время работы на одном тесте:  	5 секунд
В неориентированном графе требуется найти минимальный путь между двумя вершинами.

Входные данные
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100).
Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра).
Далее задаются номера двух вершин – начальной и конечной.

Выходные данные
Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам путь.
Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.

Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.
"""
from collections import deque

def bfs(graph, start, end):
    queue = deque([start])
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    visited[start] = True

    while queue:
        u = queue.popleft()

        if u == end:
            path = []
            while u != -1:
                path.append(u + 1)
                u = parent[u]
            return len(path) - 1, path[::-1]

        for v in range(len(graph)):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    return -1, []

n = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
start, end = map(int, input().strip().split())
start -= 1
end -= 1

length, path = bfs(graph, start, end)

if length == -1:
    print(-1)
else:
    print(length)
    if length > 0:
        print(" ".join(map(str, path)))