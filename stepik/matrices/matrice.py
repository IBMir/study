# На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в
# матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала
# первой строки, затем второй, и т.д.
# Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

# n, m = int(input()), int(input())
# text = [input() for _ in range(n * m)]
# for i in range(n):
#     for j in range(m):
#         print(text.pop(0), end=' ')
#     print()

# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую
# строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый
# столбец, и так далее.

# n, m = int(input()), int(input())
# text = [[input() for _ in range(m)] for _ in range(n)]
# for i in text:
#     print(*i)
# print()
# for _ in range(len(text[0])):
#     for i in text:
#         print(i.pop(0), end=' ')
#     print()

# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.

# n = int(input())
# print(sum([int(input().split()[i]) for i in range(n)]))

# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического
# элементов данной строки.

# n = int(input())
# for i in [[int(i) for i in input().split()] for i in range(n)]:
#     sr = sum(i) / len(i)
#     count = 0
#     for y in i:
#         if y > sr:
#             count += 1
#     print(count)

# n = int(input())
# matr = [[int(i) for i in input().split()] for i in range(n)]
# res = matr[0][0]
# for i in range((len(matr) + 2) // 2):
#     for y in range(i + 1):
#         if max(matr[i][y], matr[- i - 1][y], matr[i][- y - 1], matr[- i - 1][- y - 1]) > res:
#             res = max(matr[i][y], matr[- i - 1][y], matr[i][- y - 1], matr[- i - 1][- y - 1])
# print(res)

# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

n = int(input())
matr = [[int(i) for i in input().split()] for i in range(n)]
quarters = [0, 0, 0, 0]
for i in range(n):
    for j in range(n):
        if i < j:
            if i + j < n - 1:
                quarters[0] += matr[i][j]
            elif i + j >= n:
                quarters[1] += matr[i][j]
        elif i > j:
            if i + j < n - 1:
                quarters[3] += matr[i][j]
            elif i + j >= n:
                quarters[2] += matr[i][j]
print(f'''Верхняя четверть: {quarters[0]}
Правая четверть: {quarters[1]}
Нижняя четверть: {quarters[2]}
Левая четверть: {quarters[3]}''')