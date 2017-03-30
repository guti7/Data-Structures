#!python

# Checks whether a string conatins ANY lowercase letters.
# Assume s is a string
# fix errors

def any_lowercase(s):
    for c in s:
        print(c),
        if c.islower():
            return True
        # else:
        #     return False
    print('')
    return False


def any_lowercase2(s):
    pass


def any_lowercase3(s):
    pass


def any_lowercase4(s):
    pass


def any_lowercase5(s):
    pass


def main():

    print('***************************')

    s_all_caps = 'ANLKSGNW'
    s = 'ANlKSgNW'
    result = any_lowercase(s_all_caps)
    print('string:{} {}: {}'.format(s_all_caps, any_lowercase.__name__, result))
    result = any_lowercase2(s_all_caps)
    print('string:{} {}: {}'.format(s_all_caps, any_lowercase2.__name__, result))
    result = any_lowercase3(s_all_caps)
    print('string:{} {}: {}'.format(s_all_caps, any_lowercase3.__name__, result))
    result = any_lowercase4(s_all_caps)
    print('string:{} {}: {}'.format(s_all_caps, any_lowercase4.__name__, result))
    result = any_lowercase5(s_all_caps)
    print('string:{} {}: {}'.format(s_all_caps, any_lowercase5.__name__, result))

    print('*********')
    result = any_lowercase(s)
    print('string:{} {}: {}'.format(s, any_lowercase.__name__, result))
    result = any_lowercase2(s)
    print('string:{} {}: {}'.format(s, any_lowercase2.__name__, result))
    result = any_lowercase3(s)
    print('string:{} {}: {}'.format(s, any_lowercase3.__name__, result))
    result = any_lowercase4(s)
    print('string:{} {}: {}'.format(s, any_lowercase4.__name__, result))
    result = any_lowercase5(s)
    print('string:{} {}: {}'.format(s, any_lowercase5.__name__, result))


if __name__ == '__main__':
    main()
