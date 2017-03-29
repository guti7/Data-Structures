#!python


def find(string, pattern):
    """return true if string contains the entire pattern, false otherwise."""
    # implement find_iterative and find_recursive
    # assert isinstance(string, str)
    return find_iterative(string, pattern)
    # return find_recursive(string, pattern)


def find_iterative(string, pattern):
    # loop over the string until the pattern in found
    if string and pattern:
        pat_index = 0
        for char in string:
            if char == pattern[pat_index]:
                pat_index += 1
            else:
                pat_index = 0
            if pat_index == len(pattern):
                return True
    return False


def find_recursive(string, pattern):
    # TODO: implement find_recursive
    pass


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
