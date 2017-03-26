#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):  # use enumarate to have index value
        if item == value:
            return index  # found
    return None  # not found if you get to the end of the list


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below
    # index - has default value of 0 is none is given

    # check for None list and if you are at the end of the array
    if array is None or len(array) == index:
        return None
    if array[index] == item:  # check if you have found the item
        return index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """Return the index of item in sorted array or None if item is not found."""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here

    # check for None list and if you are at the end of the array
    if not array:
        return None

    array.sort()
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if array[middle] < item:
            left = middle + 1
        elif array[middle] > item:
            right = middle - 1
        else:  # array(index) == item , item found
            return middle
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
