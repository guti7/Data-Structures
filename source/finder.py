#!python


def find(string, pattern):
    """return true if string contains the entire pattern, false otherwise."""
    # implement find_iterative and find_recursive
    # assert isinstance(string, str)
    return find_iterative(string, pattern)
    # return find_recursive(string, pattern)


def find_iterative(string, pattern):
    # loop over the string until the pattern in found
    if not string or not pattern:
        return False
    pat_index = 0
    for char in string:
        if char == pattern[pat_index]:
            pat_index += 1
        else:
            pat_index = 0
        if pat_index == len(pattern):
            return True
    return False


def find_recursive(string, pattern, str_index=0, ptr_index=0):
    # implement find_recursive
    if not string or not pattern:
        return False
    if ptr_index == len(pattern):
        return True
    if str_index == len(string):
        return False
    if string[str_index] == pattern[ptr_index]:
        return find_recursive(string, pattern, str_index + 1, ptr_index + 1)
    return find_recursive(string, pattern, str_index + 1, 0)


def find_index(string, pattern):
    """
    Return the starting index of the first occurence of the pattern,
    and None if not found.
    """
    # implement find_index_iterative and find_index_recursive
    return find_index_iterative(string, pattern)
    # return find_index_recursive(string, pattern)


def find_index_iterative(string, pattern):
    # TODO: implement
    pass


def find_index_recursive(string, pattern):
    # TODO: implement
    pass


# STRETCH:
def find_all_indexes(string, pattern):
    """Returns a list of the starting indexes of all ocurrences of pattern."""
    # implement find_all_indexes_iterative and find_all_indexes_recursive
    return find_all_indexes_iterative(string, pattern)
    # return find_all_indexes_recursive(string, pattern)


def find_all_indexes_iterative(string, pattern):
    # TODO: implement
    pass


def find_all_indexes_recursive(string, pattern):
    # TODO: implement
    pass


if __name__ == '__main__':
    # print(find('', ''))
    print(find_recursive('', ''))
