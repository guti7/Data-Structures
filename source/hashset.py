#!python

from hashtable import HashTable


class HashSet(object):
    """Implement set class with a hash table."""

    def __init__(self, elements=None):
        """Initialize the empty Set, and add each element a if sequence is given."""
        self.set = HashTable()
        self.size = 0  # Tracks the number of elements in constant time
        if elements:
            for element in elements:
                self.add(element)

    def add(self, element):
        """Add element to this set, if not present already."""
        # TODO: What to return? Nothing?
        pass

    def remove(self, element):
        """Remove element from this set, if present."""
        # TODO: Do we return the element? what if it's not found??
        pass

    def contains(self, element):
        """Return true if element is in this set, false Otherwise."""
        pass

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


if __name__ == '__main__':
    test_hash_set()
