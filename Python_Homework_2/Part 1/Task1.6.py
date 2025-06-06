"""
По заданной матрице смежности неориентированного графа определите, содержит ли он петли.

Входные данные
На вход программы поступает число n (1≤n≤100) – количество вершин графа, а затем n строк по n чисел, каждое из которых
равно 0 или 1, – его матрица смежности.

Выходные данные
Выведите «YES», если граф содержит петли, и «NO» в противном случае.
"""
n = int(input().strip())
adjacency_matrix = [list(map(int, input().strip().split())) for _ in range(n)]

has_loops = False
for i in range(n):
    if adjacency_matrix[i][i] == 1:
        has_loops = True
        break

if has_loops:
    print("YES")
else:
    print("NO")