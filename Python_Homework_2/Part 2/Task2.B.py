"""
Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.

Входные данные
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны
по два числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.

Выходные данные
В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности
в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.
"""
def dfs(vertex, component, visited, graph):
    stack = [vertex]
    visited[vertex] = True
    component.append(vertex)

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                component.append(neighbor)

def find_connected_components(N, edges):
    graph = [[] for _ in range(N + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    components = []

    for vertex in range(1, N + 1):
        if not visited[vertex]:
            component = []
            dfs(vertex, component, visited, graph)
            components.append(component)

    return components

N, M = map(int, input().strip().split())
edges = [tuple(map(int, input().strip().split())) for _ in range(M)]

components = find_connected_components(N, edges)

print(len(components))
for component in components:
    print(len(component))
    print(" ".join(map(str, component)))