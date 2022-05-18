def binary_search(list, item):
    start = 0
    stop = len(list) - 1

    while start <= stop:
        mid = int((start + stop) / 2)
        if item == list[mid]:
            return mid
        elif list[mid] > item:
            stop = mid - 1
        else:
            start = mid + 1
    return 'Такого значения нет в списке.'