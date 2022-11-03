#На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

# n, m = int(input()), int(input())
# matr = [input().split() for i in range(n)]
# i, j = map(int, input().split())
# for a in range(n):
#     matr[a][i], matr[a][j] = matr[a][j], matr[a][i]
#     print(*matr[a])

# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы
# построчно через пробел.

# matr = [input().split() for i in range(int(input()))]
# res = 'YES'
# for i in range(len(matr)):
#     if res == 'YES':
#         for j in range(len(matr)):
#             if i < j and matr[i][j] != matr[j][i]:
#                 res = 'NO'
#     else:
#         break
# print(res)

# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

# n, m = int(input()), int(input())
# matr = [input().split() for i in range(n)]
# max_m, res = matr[0][0], [0, 0]
# for i in range(n):
#     for j in range(m):
#         if int(matr[i][j]) > int(max_m):
#             max_m = matr[i][j]
#             res = [i, j]
# print(*res)

# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной
# диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
# элемент на главной диагонали и на побочной диагонали).

n = int(input())
matr = [input().split() for i in range(n)]
i, j, a, b, = 0, 0, n - 1, 0
while i < n:
    matr[i][j], matr[a][b] = matr[a][b], matr[i][j]
    i, j, a, b, = i + 1, j + 1, a - 1, b + 1
[print(*i) for i in matr]