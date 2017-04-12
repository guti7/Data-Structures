#!python

def bubble_sort(items):
    sorted_items = items
    n = len(items)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            print(i)
            if sorted_items[i + 1] < sorted_items[i]:
                # swap
                sorted_items[i], sorted_items[i + 1] = sorted_items[i + 1], sorted_items[i]
                swapped = True
    return sorted_items

def test_sorting():
    array = [2, 4, 3, 1, 5]
    print(array)
    print(bubble_sort(array))
    # assert bubble_sort(array) == [1, 2, 3, 4, 5]

if __name__ == '__main__':
    test_sorting()
