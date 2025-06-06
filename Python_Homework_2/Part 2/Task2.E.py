"""
Из прямоугольного листа клетчатой бумаги (M строк, N столбцов) удалили некоторые клетки.
На сколько кусков распадётся оставшаяся часть листа? Две клетки не распадаются, если они имеют общую сторону.

Входные данные
В первой строке находятся числа M и N, в следующих M строках - по N символов.
Если клетка не была вырезана, этому соответствует знак #, если вырезана - точка. 1 <= M, N <= 100.

Выходные данные
Вывести одно число.
"""
def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))

M, N = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(M)]

visited = [[False] * N for _ in range(M)]
components_count = 0

for i in range(M):
    for j in range(N):
        if grid[i][j] == '#' and not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            components_count += 1

print(components_count)