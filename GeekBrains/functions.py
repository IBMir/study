def filter(numbers, function):
    result = []
    for i in numbers:
        if function(i):
            result.append(i)
    return result

def even(i):
    return i % 2 == 0

def odd(i):
    return i % 2 != 0

def more4(i):
    return i > 4

if __name__ == '__main__':
    s = [2, 5, 6, 76, 545, 3, 467, 4, 43, 2]
    print(filter(s, even))
    print(filter(s, odd))
    print(filter(s, more4))
    print(filter(s, lambda i: i < 4))
