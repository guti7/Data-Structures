#!python

def bubble_sort(items):
    sorted_items = items
    n = len(items)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if sorted_items[i + 1] < sorted_items[i]:
                # swap
                sorted_items[i], sorted_items[i + 1] = sorted_items[i + 1], sorted_items[i]
                swapped = True
    return sorted_items

def selection_sort(items):

    for i in range(len(items)):  # look into the whole list
        min_index = i  # start with placeholder at first item
        j = i + 1  # compare to the next index
        for j in range(j, len(items)):  # start from the next over index to end of list
            if items[j] < items[min_index]:
                min_index = j
        # if min_index != j:
        items[i], items[min_index] = items[min_index], items[i]
        # print("iteration {}: {}".format(i, items))
    return items

def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items

def test_sorting():
    array = [2, 4, 3, 1, 5]
    print(array)
    # print(bubble_sort(array))
    # assert bubble_sort(array) == [1, 2, 3, 4, 5]
    # print(selection_sort(array))
    print(insertion_sort(array))

if __name__ == '__main__':
    test_sorting()
