"""
По заданной квадратной матрице n×n из нулей и единиц определите, может ли данная матрица быть матрицей смежности
простого неориентированного графа.

Входные данные
На вход программы поступает число n
 (1≤n≤100)
  – размер матрицы, а затем n строк по n
 чисел, каждое из которых равно 0 или 1, – сама матрица.

Выходные данные
Выведите «YES», если приведенная матрица может быть матрицей смежности простого неориентированного графа, и «NO» в
противном случае.
"""
def find_adjacency_matrix(n, matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return "NO"
    for i in range(n):
        if matrix[i][i] != 0:
            return "NO"
    return "YES"
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(find_adjacency_matrix(n, matrix))