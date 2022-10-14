import time

# starting time
start = time.time()


def sum_num(x):
    sum = 0
    while (x != 0):
        sum += x % 10
        x //= 10
    return sum


massif = [34, 908475, 72652537, 610, 4, 1121, 90, 100000, 363647, 1100011]
res = {}
for i in massif:
    res[i] = sum_num(i)
massif = [i[0] for i in sorted(res.items(), key=lambda x: x[1])]
print(massif)

# end time
end = time.time()

# total time taken
print("Время выполнения программы составляет - ", end - start)
