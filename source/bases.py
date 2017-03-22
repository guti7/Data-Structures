#!python

import string

ALPHA = "0123456789abcdefghijklmnopqrstuv"

def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    result = 0
    for index, char in enumerate(reversed(list(str_num))):
        next_digit = to_digit(char)
        result += base ** index * next_digit
    return result



def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    result = ''
    while num > 0:
        digit = get_digit_string(num, base)
        result = digit + result
        num = num / base
    return result


def get_digit_string(num, base):
    """
    Get the next digit in the encoding for the given base.
    num -- the number in base 10
    base -- base to convert to
    """
    remainder = num % base
    if base == 16 or base == 32:
        return to_char(remainder)
    else:
        return str(remainder)


def to_char(num):
    """
    Covert number to alphanumberic representation.
    num -- number to convert
    """
    return ALPHA[num]

def to_digit(char):
    return ALPHA.index(char)


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    str_num -- string representation of number in given base
    base1 -- base of given number
    base2 -- base to convert to
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    return encode(decode(str_num, base1), base2)


def main():
    """
    Main.
    """
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num,
                                                      base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
