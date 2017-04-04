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
        elements_as_str = ['{}'.format(repr(element)) for element in self.elements()]
        return '{' + ', '.join(elements_as_str) + '}'

    def __repr__(self):
        """Return a string representation of this set."""
        return 'Set({})'.format(repr(self.elements()))

    def elements(self):
        """Return a list of all elements in this set."""
        return self.collection.keys()

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
        # What is the union of two sets?
        # Union is the set of all elements in both sets
        # AuB = {x: x -> A or x -> B}
        # AuB is the set of elements which are in A, in B, or both A and B.
        union = HashSet(self.elements())
        for element in other_set.elements():
            union.add(element)
        return union

    def intersection(self, other_set):
        """Return the intersection of this set and other_set."""
        # What is the intersection of two sets?
        # The new set with elements common to both sets.
        intersection = HashSet()
        for element in other_set.elements():
            if self.contains(element):
                intersection.add(element)
        return intersection

    def difference(self, other_set):
        """Return the difference of this set and other_set."""
        # What is the difference of two sets?
        # Remove the elements of B contained in A.
        # A - B = A \ B = { x E A | x nE B}
        # The new set with elements in this this set, but not in the other.
        difference = HashSet()
        # for element in other_set.elements():
        #     if not self.contains(element):
        #         difference.add(element)
        # return difference
        for element in self.elements():
            if not other_set.contains(element):
                difference.add(element)
        return difference

    def is_subset(self, other_set):
        """Return whether other_set is a subset of this set."""
        # What is a subset of two sets?
        # Tests whether every element in this set is in the other_set
        for element in self.elements():
            if not other_set.contains(element):
                return False
        return True

def test_hash_set():

    # TODO: Test for empty sets combinations and operations
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

    print('Union of sets:')
    set_a = HashSet()
    print('set A: ' + str(set_a))
    set_b = HashSet([1, 2, 5])
    print('set B: ' + str(set_b))
    union = set_a.union(set_b)
    print('AuB = ' + str(union))
    print('size AuB: ' + str(union.size))
    print('*****')
    set_a = HashSet([1, 3, 5, 6])
    print('set A: ' + str(set_a))
    set_b = HashSet([1, 2, 5])
    print('set B: ' + str(set_b))
    union = set_a.union(set_b)
    print('AuB = ' + str(union))
    print('size AuB: ' + str(union.size))

    print('******')
    print('Intersection of sets:')
    set_a = HashSet([1, 3, 5, 6])
    print('set A: ' + str(set_a))
    set_b = HashSet([1, 2, 5])
    print('set B: ' + str(set_b))
    union = set_a.intersection(set_b)
    print('AnB = ' + str(union))
    print('size AuB: ' + str(union.size))

    print('******')
    print('Difference of sets:')
    set_a = HashSet([1, 3, 5, 6])
    print('set A: ' + str(set_a))
    set_b = HashSet([1, 2, 5])
    print('set B: ' + str(set_b))
    union = set_a.difference(set_b)
    print('A\B = ' + str(union))
    print('size A\B: ' + str(union.size))

    print('******')
    print('Subset of sets:')
    set_a = HashSet([1, 2, 3, 5, 6])
    print('set A: ' + str(set_a))
    set_b = HashSet([1, 2, 5])
    print('set B: ' + str(set_b))
    print('A is a subset of B = ' + str(set_a.is_subset(set_b)))
    print('B is a subset of A = ' + str(set_b.is_subset(set_a)))
    print('B is a subset of B = ' + str(set_b.is_subset(set_b)))



if __name__ == '__main__':
    test_hash_set()
