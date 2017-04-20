def merge(list1, list2):
    """Implement merge algorithm that combines two sorted lists into a sorted list"""
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


def merge_sort(items):
    size = len(items)
    if size <= 1:
        return items
    middle = size / 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return merge(left, right)

def test_merge():
    l1 = [2, 4]
    l2 = [5, 6, 8]
    merged = merge(l1, l2)
    print(merged)


def test_merge_sort():
    items = [2, 3, 5, 1, 0, 10, 7]
    sorted_items = merge_sort(items)
    print(sorted_items)

if __name__ == '__main__':
    test_merge()
    test_merge_sort()
