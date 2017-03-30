#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string
import re


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    text = re.sub(r"[^A-Za-z]*", '', text)  # remove all non-letters
    text = text.lower()
    # return text == text[::-1]

    # if len(text) <= 1:
    #     return True
    # if text[0] != text[-1]:
    #     return False
    # return is_palindrome(text[1:-1])

    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively

    text = re.sub(r"[^A-Za-z]*", '', text)  # remove all non-letters
    if len(text) <= 1:
        return True
    text = text.lower()  # change to lowercase
    for index, ch in enumerate(text):
        if ch is not text[len(text) - 1 - index]:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively.
    if not left:
        left = 0
        text = re.sub(r"[^A-Za-z]*", '', text)  # remove all non-letters
        text = text.lower()
    if not right:
        right = -1

    if abs(right) >= len(text):
        return True
    if text[left] != text[right]:
        return False
    return is_palindrome_recursive(text, left + 1, right - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
