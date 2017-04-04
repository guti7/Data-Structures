#!python

from hashset import HashSet
import unittest

class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet()
        assert hs.size == 0
        # TODO: Test elements sequence
        elements = [0, 1, 2, 1, 0]
        hs = HashSet()
        assert hs.size == 3

    def test_size(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add(1)
        assert hs.size == 1
        hs.add(2)
        assert hs.size == 2
        hs.add(3)
        assert hs.size == 3


    def test_add(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add(2)
        assert hs.size == 1
        hs.add(2)
        assert hs.size == 1
        hs.add(3)
        assert hs.size == 2

    def test_remove(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add(0)
        hs.add(1)
        hs.add('zero')
        hs.add('one')
        assert hs.size == 4
        hs.remove(0)
        assert hs.size == 3
        hs.remove(1) == 2
        hs.remove('zero') == 1
        with self.assertRaises(KeyError):
            ht.remove('zero')
        with self.assertRaises(KeyError):
            ht.remove('0')
        # assert hs.remove('0') == None

    def test_contains(self):
        hs = HashSet()
        hs.add(0)
        hs.add(1)
        hs.add('zero')
        hs.add('one')
        assert hs.contains(0) is True
        assert hs.contains('zero') is True
        assert hs.contains('0') is False
        assert hs.contains(2) is False

    def test_union(self):
        # TODO: complete this test
        hash_set1 = hs.HashSet([1, 2, 3])
        hash_set2 = hs.HashSet([4, 5, 6])
        assert hash_set1.union(hash_set2) == [1, 2, 3, 4, 5, 6]

    def test_intersection(self):
        # TODO: complete this test
        assert self.fail('Implement')
        pass

    def test_difference(self):
        # TODO: complete this test
        pass

    def test_is_subset(self):
        # TODO: complete this test
        pass
