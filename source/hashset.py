#!python

from hashtable import HashTable


class HashSet(object):
    """Implement set class with a hash table."""

    def __init__(self, elements=None):
        """Initialize the empty Set, and add each element a if sequence is given."""
        self.collection = HashTable()
        self.size = 0  # Tracks the number of elements in constant time
        if elements:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this set."""
        elements = ['{}'.format(repr(key)) for key, element in self.elements()]
        return '{' + ', '.join(elements) + '}'

    def __repr__(self):
        """Return a string representation of this set."""
        return 'Set({})'.format(repr(self.elements()))

    def elements(self):
        """Return a list of all elements in this set."""
        return self.collection.items()

    def add(self, element):
        """Add element to this set, if not present already."""
        # TODO: What to return? Nothing?
        self.collection.set(element, 0)
        self.size = self.collection.size
        # self.size += 1

    def remove(self, element):
        """Remove element from this set, if present."""
        # TODO: Do we return the element? what if it's not found??
        self.collection.delete(element)
        self.size = self.collection.size
        # self.size -= 1
        # try:
        #     self.collection.delete(element)
        # except KeyError as error:
        #     print('do something with the error')

    def contains(self, element):
        """Return true if element is in this set, false Otherwise."""
        return self.collection.contains(element)

    def union(self, other_set):
        """Return the union of this set and other_set."""
        # TODO: What is the union of two sets?
        pass

    def intersection(other_set):
        """Return the intersection of this set and other_set."""
        # TODO: What is the intersection of two sets?
        pass

    def difference(other_set):
        """Return the difference of thi sest and other_set."""
        # TODO: What is the difference of two sets?
        pass

    def is_subset(other_set):
        """Return whether other_set is a subset of this set."""
        # TODO: What is a subset of two sets?
        pass

def test_hash_set():
    hs = HashSet()
    print('HashSet: ' + str(hs))
    print('HashSet: ' + repr(hs))
    print('size: ' + str(hs.size))

    print('Adding elements:')
    hs.add(5)
    print('add(5): ' + str(hs))
    hs.add(3)
    print('add(3): ' + str(hs))
    print('size: ' + str(hs.size))
    print(hs.elements())

    print('Checking entries:')
    print('contains(5): ' + str(hs.contains(5)))
    print('contains(3): ' + str(hs.contains(3)))
    print('contains(0): ' + str(hs.contains(0)))

    print('Removing entries:')
    hs.remove(5)
    print('remove(5): ' + str(hs))
    hs.remove(3)
    print('remove(3): ' + str(hs))
    print('contains(5): ' + str(hs.contains(5)))
    print('contains(3): ' + str(hs.contains(3)))
    print('size: ' + str(hs.size))


if __name__ == '__main__':
    test_hash_set()
