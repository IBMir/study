import time

A, B = input(), input()

# starting time
start = time.time()

A, B = [int(i) for i in A], sorted([int(i) for i in B], reverse=True)
print(A, B)
for i in B:
    for y in range(len(A)):
        if i > A[y]:
            A[y] = i
            break

print(''.join(str(i) for i in A))

# end time
end = time.time()

# total time taken
print("Время выполнения программы составляет - ", end - start)

