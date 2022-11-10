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

# n = int(input())
# matr = [input().split() for i in range(n)]
# i, j, a, b, = 0, 0, n - 1, 0
# while i < n:
#     matr[i][j], matr[a][b] = matr[a][b], matr[i][j]
#     i, j, a, b, = i + 1, j + 1, a - 1, b + 1
# [print(*i) for i in matr]

# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

# matr = [input().split() for i in range(int(input()))]
# for i in matr[::-1]:
#     print(i)
#
# # Напишите программу, которая поворачивает квадратную матрицу чисел на 90 грудусов по часовой стрелке.
#
# n = int(input())
# matr = [input().split() for i in range(n)]
# for i in range(n):
#     for j in range(n - 1, -1, -1):
#         print(matr[j][i], end=' ')
#     print()

# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые
# бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *,
# остальные клетки заполните точками.

# chess_board = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [1, 2, 3, 4, 5, 6, 7, 8]]
# n = input()
# n = [chess_board[0].index(n[0]), int(n[1]) - 1]
# knights_move = []
# for i in [-2, 2]:
#     for j in [-1, 1]:
#         if 0 <= n[0] + i <= 7 and 0 <= n[1] + j <= 7:
#             knights_move.append([n[0] + i, n[1] + j])
#         if 0 <= n[0] + j <= 7 and 0 <= n[1] + i <= 7:
#             knights_move.append([n[0] + j, n[1] + i])
# for i in range(7, -1, -1):
#     for j in range(8):
#         if [j, i] in knights_move:
#             print('*', end=' ')
#         elif [j, i] == n:
#             print('N', end=' ')
#         else:
#             print('.', end=' ')
#     print()

# Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1, 2, 3, n ** 2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
# которая проверяет, является ли заданная квадратная матрица магическим квадратом.

# n = int(input())
# matr = [[int(i) for i in input().split()] for i in range(n)]
# summa = sum(matr[0])
# res = 'YES'
# lis = list()
# for i in matr:
#     for j in i:
#         lis.append(j)
# for i in range(1, n ** 2 + 1):
#     if i not in lis:
#         res = 'NO'
#         break
# if res == 'YES':
#     for i in matr[1:]:
#         if summa != sum(i):
#             res = 'NO'
#             break
# if res == 'YES':
#     summa_dlp, summa_dpl = 0, 0
#     for i in range(n):
#         summa_st = 0
#         for j in range(n):
#             summa_st += matr[j][i]
#             if i == j:
#                 summa_dlp += matr[j][i]
#             if i + j == n - 1:
#                 summa_dpl += matr[j][i]
#         if summa != summa_st:
#             res = 'NO'
#             break
#     if summa != summa_dlp or summa != summa_dpl:
#         res = 'NO'
# print(res)