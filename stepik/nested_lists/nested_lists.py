# На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

from math import factorial


def pask(n):
    b = []
    for i in range(n + 1):
        b.append(int((factorial(n)) / (factorial(i) * factorial(n - i))))
    return b


# # n = int(input())
# for i in range(n):
#     # print(*pask(i))

# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
# последовательности одинаковых символов заданной строки в подсписки.

# s = list()
# res = [[s[0]]]
# for i in range(2, len(s), 2):
#     if s[i] in res[-1]:
#         res[-1].append(s[i])
#     else:
#         res.append([s[i]])
# print(res)

# На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

def chunked(lis, len_list):
    res = [[]]
    for i in lis.split():
        if len(res[-1]) < int(len_list):
            res[-1].append(i)
        else:
            res.append([i])
    return res


# print(chunked(input(), input()))

# Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. Например, [1],
# [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4]
# не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой список — подсписок
# любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].
# На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу,
# которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

n = input().split()
res = [[]]
for i in range(len(n) + 1):
    for y in range(len(n) + 1):
        if len(n[y:y + i]) >= i and n[y:y + i] != []:
            res.append(n[y:y + i])
print(res)

# Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:
# list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
# print(list1)

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2] += sub_list
# print(list1)

# Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один общий
# максимальный элемент среди всех элементов вложенных списков list1.

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for i in list1:
    if max(i) > maximum:
        maximum = max(i)
# print(maximum)

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in range(len(list1)):
    list1[i].reverse()
# print(list1)

# Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую
# на общее количество всех чисел.

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# print(sum([sum(i) for i in list1]) / sum([len(i) for i in list1]))
