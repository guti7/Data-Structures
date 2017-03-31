#!python

from doublylinkedlist import DoublyLinkedList, BinaryNode
import unittest


class BinaryNodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = BinaryNode(data)
        assert node.data is data
        assert node.next is None
        assert node.previous is None


class DoublyLinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = DoublyLinkedList()
        assert ll.head is None
        assert ll.tail is None
        assert ll.size == 0

    def test_init_with_list(self):
        ll = DoublyLinkedList(['A', 'B', 'C'])
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'
        assert ll.size == 3

    def test_items(self):
        ll = DoublyLinkedList()
        assert ll.items() == []
        ll.append('A')
        assert ll.items() == ['A']
        ll.append('B')
        assert ll.items() == ['A', 'B']
        ll.append('C')
        assert ll.items() == ['A', 'B', 'C']

    def test_length(self):
        ll = DoublyLinkedList()
        assert ll.length() == 0
        ll.append('A')
        assert ll.length() == 1
        ll.append('B')
        assert ll.length() == 2
        ll.append('C')
        assert ll.length() == 3

    def test_size(self):
        ll = DoublyLinkedList()
        assert ll.size == 0
        ll.append('A')
        assert ll.size == 1
        ll.append('B')
        assert ll.size == 2
        ll.append('C')
        assert ll.size == 3

    def test_get_at_index(self):
        ll = DoublyLinkedList(['A', 'B', 'C'])
        assert ll.get_at_index(0) == 'A'
        assert ll.get_at_index(1) == 'B'
        assert ll.get_at_index(2) == 'C'
        with self.assertRaises(ValueError):
            ll.get_at_index(3)
            ll.get_at_index(-1)

    def test_insert_at_index(self):
        ll = DoublyLinkedList()
        ll.insert_at_index(0, 'B')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'B'
        assert ll.size == 1
        ll.insert_at_index(1, 'C')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        assert ll.size == 2
        ll.insert_at_index(0, 'A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'
        assert ll.size == 3
        with self.assertRaises(ValueError):
            ll.insert_at_index(4, 'D')
            ll.insert_at_index(-1, 'E')

    def test_append(self):
        ll = DoublyLinkedList()
        ll.append('A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'A'
        assert ll.size == 1
        ll.append('B')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'B'
        assert ll.size == 2
        ll.append('C')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'
        assert ll.size == 3

    def test_prepend(self):
        ll = DoublyLinkedList()
        ll.prepend('C')
        assert ll.head.data == 'C'
        assert ll.tail.data == 'C'
        assert ll.size == 1
        ll.prepend('B')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        assert ll.size == 2
        ll.prepend('A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'
        assert ll.size == 3

    def DISABLE_test_delete(self):
        ll = DoublyLinkedList()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        ll.delete('A')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        assert ll.size == 2
        ll.delete('C')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'B'
        assert ll.size == 1
        ll.delete('B')
        assert ll.head is None
        assert ll.tail is None
        assert ll.size == 0
        with self.assertRaises(ValueError):
            ll.delete('D')

    def test_find(self):
        ll = DoublyLinkedList()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        assert ll.find(lambda item: item == 'B') == 'B'
        assert ll.find(lambda item: item < 'B') == 'A'
        assert ll.find(lambda item: item > 'B') == 'C'
        assert ll.find(lambda item: item == 'D') is None


if __name__ == '__main__':
    unittest.main()
