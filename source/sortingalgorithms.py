#!python

from binarysearchtree import BinarySearchTree

def bubble_sort(items):
    #  TODO: passed by value
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
        # TODO: j could be named more explicitly : offset?
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

def tree_sort(items):
    tree = BinarySearchTree(items)
    return tree.items_in_order()

def counting_sort(items):
    length = len(items)

    # Count the number of distinct keys(items) in a histogram
    k = max(items) + 1
    count = [0 for _ in range(k)]

    for i in range(length):  # 0 to
        value = items[i]
        count[value] += 1
    print('Counts: {}'.format(count))

    # Sum up counts to calculate the actual ordered position for each key
    for i in range(1, k):
        count[i] += count[i - 1]
    print('Sum: {}'.format(count))

    output = [0 for _ in items]
    for i in range(length):
        count_index = items[i]
        position = count[count_index] - 1
        output[position] = items[i]
        count[count_index] -= 1

    return output

def human_sort(orig):
    source = orig[:]  # create shallow copy
    sorted_items = []       # init sorted array
    source_len = len(source)
    for _ in range(source_len):         # repeat for every elem
        min_idx = 0
        for j in range(len(source)):    # find min in source
            compare = source[min_idx]   # elem to compare against
            current = source[j]         # current elem in iteration
            if current < compare:
                min_idx = j
        sorted_items.append(source[min_idx])  # add min to sorted
        del source[min_idx]             # remove from source
    return sorted_items

def test_sorting():
    array = [2, 1, 5, 2, 2, 1, 4, 0]
    print(array)
    # print(bubble_sort(array))
    # assert bubble_sort(array) == [1, 2, 3, 4, 5]
    # print(selection_sort(array))
    # print(insertion_sort(array))
    # print(tree_sort(array))
    # print(human_sort(array))
    print('test: {}.'.format(counting_sort(array)))

if __name__ == '__main__':
    test_sorting()
