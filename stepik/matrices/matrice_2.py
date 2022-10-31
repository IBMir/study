# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

n, m = int(input()), int(input())
matr = [input().split() for i in range(n)]
max_m, res = matr[0][0], [0, 0]
for i in range(n):
    for j in range(m):
        if int(matr[i][j]) > int(max_m):
            max_m = matr[i][j]
            res = [i, j]
print(*res)

