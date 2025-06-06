"""
Дан неориентированный невзвешенный граф. Для него вам необходимо найти количество вершин,
лежащих в одной компоненте связности с данной вершиной (считая эту вершину).

Входные данные
В первой строке входных данных содержатся два числа: N и S (1 ≤ N ≤ 100; 1 ≤ S ≤ N), где N – количество вершин графа,
а S – заданная вершина. В следующих N строках записано по N чисел – матрица смежности графа, в которой 0 означает
отсутствие ребра между вершинами, а 1 – его наличие. Гарантируется, что на главной диагонали матрицы всегда стоят нули.

Выходные данные
Выведите одно целое число – искомое количество вершин.
"""
def count_connected_components(adj_matrix, start_vertex):
    N = len(adj_matrix)
    visited = [False] * N
    stack = [start_vertex]
    visited[start_vertex] = True
    count = 1

    while stack:
        vertex = stack.pop()
        for neighbor in range(N):
            if adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count += 1

    return count

N, S = map(int, input().split())
S -= 1
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

result = count_connected_components(adj_matrix, S)
print(result)