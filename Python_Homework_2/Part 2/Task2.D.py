"""
На банкет были приглашены N Очень Важных Персон (ОВП). Были поставлены 2 стола. Столы достаточно большие,
чтобы все посетители банкета могли сесть за любой из них. Проблема заключается в том, что некоторые ОВП не ладят друг
с другом и не могут сидеть за одним столом. Вас попросили определить, возможно ли всех ОВП рассадить за двумя столами.

Входные данные
В первой строке входных данных содержатся два числа: N и M (1 <= N,M <= 100), где N – количество ОВП, а M – количество
пар ОВП, которые не могут сидеть за одним столом. В следующих M строках записано по 2 числа – пары ОВП, которые
не могут сидеть за одним столом.

Выходные данные
Если способ рассадить ОВП существует, то  выведите YES в первой строке и номера ОВП, которых необходимо
посадить за первый стол, во второй строке. В противном случае в первой и единственной строке выведите NO.
"""
def can_be_bipartite(graph, N):
    color = [-1] * N

    for start in range(N):
        if color[start] == -1:
            stack = [start]
            color[start] = 0

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False, []

    group1 = [i + 1 for i in range(N) if color[i] == 0]
    return True, group1

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

is_bipartite, group1 = can_be_bipartite(graph, N)

if is_bipartite:
    print("YES")
    print(" ".join(map(str, group1)))
else:
    print("NO")