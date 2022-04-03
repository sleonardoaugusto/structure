def bubble_sort(items):
    for length in range(len(items) - 1, 0, -1):
        for idx in range(length):
            if items[idx] > items[idx + 1]:
                temp = items[idx]
                items[idx] = items[idx + 1]
                items[idx + 1] = temp
    return items
