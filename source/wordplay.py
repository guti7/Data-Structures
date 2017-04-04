#!python

# Case study: Word Play
# Based on chapter 9 from Think Python: How to think like a computer scientist
# by Allen B. Downey


# Searching Patterns
def has_no_e(word):
    """Return True if the given word doesn't have the letter "e"."""
    for letter in word:
        if letter == 'e':
            return False
    return True
    # return 'e' in word


def avoids(forbidden, word):
    """Return True if the word doesn't use any of the forbidden letter."""
    for letter in word:
        if letter in forbidden:
            return False
    return True


def uses_only(available, word):
    """Return True if the word only uses the available letters."""
    for letter in word:
        if letter not in available:
            return False
    return True


def uses_all(required, word):
    """Return true if the word uses all the required letters at least once."""
    for letter in required:
        if letter not in word:
            return False
    return True
    # return uses_only(word, required)


def is_abecedarian(word):
    """Returns True if the letters in a word appear in alphabetical order."""
    return is_abecedarian_iterative(word)
    # return is_abecedarian_recursive(word)


def is_abecedarian_iterative(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

    # using while loop
    # i = 0
    # while i < len(word) - 1:
    #     if word[i + 1)] < word[i]:
    #         return False
    #     i += 1
    # return True

def is_abecedarian_recursive(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recursive(word[1:])

def test_wordplay():
    # e_word = 'e'
    # no_e_word = 'book'
    print('no e: ' + str(has_no_e('e')))
    print('with e: ' + str(has_no_e('book')))


if __name__ == '__main__':
    test_wordplay()
