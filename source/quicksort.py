def partition(items):
    """Chooses a pivot and segments a list into sublists.
    Returns a pair of lists containing all elements less than or equal to pivot
    in small and all elements greater than pivot in large.
    """
    pivot = items[len(items) - 1]
    i = 0
    print('pivot: {}'.format(pivot))
    for j in range(len(items)):
        if items[j] <= pivot:
            i += 1
            swap(items, i, j)
    swap(items, i + 1, len(items) - 1)
    return (items[:i], items[i + 1:])


def swap(items, a, b):
    items[a], items[b] = items[b], items[a]


if __name__ == '__main__':
    a = [8, 2, 4, 1]
    print(a)
    result = partition(a)
    print(a)
    print(result[0])
    print(result[1])
