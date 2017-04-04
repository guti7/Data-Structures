#!python

from hashset import HashSet
import unittest

class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet()
        assert hs.size == 0
        # Test elements with given sequence
        elements = [0, 1, 2, 1, 0]
        hs = HashSet(elements)
        assert hs.size == 3
        assert str(hs) == '{0, 1, 2}'

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
            hs.remove('zero')
        with self.assertRaises(KeyError):
            hs.remove('0')

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
        set_a = HashSet([1, 2, 3])
        set_b = HashSet([4, 5, 6])
        assert set_a.union(set_b).elements() == [1, 2, 3, 4, 5, 6]
        set_c = HashSet([1, 1, 1])
        assert set_a.union(set_c).elements() == [1, 2, 3]

    def test_intersection(self):
        set_a = HashSet([1, 2, 3])
        set_b = HashSet([4, 2, 3])
        assert set_a.intersection(set_b).elements() == [2, 3]
        set_c = HashSet([1])
        assert set_a.intersection(set_c).elements() == [1]

    def test_difference(self):
        set_a = HashSet([1, 2, 3])
        set_b = HashSet([4, 2, 3])
        assert set_a.difference(set_b).elements() == [1]
        set_c = HashSet([1])
        assert set_a.difference(set_c).elements() == [2, 3]

    def test_is_subset(self):
        set_a = HashSet([1, 2, 3])
        set_b = HashSet([4, 2, 3])
        assert set_a.is_subset(set_b) is False
        assert set_b.is_subset(set_a) is False
        set_c = HashSet([1])
        assert set_a.is_subset(set_c) is False
        assert set_c.is_subset(set_a) is True
        set_d = HashSet([2, 3])
        assert set_d.is_subset(set_a) is True
        assert set_d.is_subset(set_b) is True
