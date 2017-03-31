#!python

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string represeantation of this node."""
        return 'Node({})'.format(repr(self.data))


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list: append the given items, if any."""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'DoublyLinkedList({})'.format(repr(self.items()))

    def items(self, reverse=False):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        result = []
        current = self.head if not reverse else self.tail
        while current is not None:
            result.append(current.data)
            current = current.next if not reverse else current.previous
        return result

    def is_empty(self):
        """Return True if this linked list is empty, False otherwise."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size."""
        # Check if the given index is out of range and if so raise error
        if not(0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # Find the node and return the node's data
        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        return current.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size."""
        # check if the index is valid
        if not(0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # Traverse to the previous node before node and insert
        # Insert at the start is similar to prepend
        if index == 0:
            self.prepend(item)
        # Insert at the end is similar to append
        elif index == self.size:
            self.append(item)
        else:
            # Traverse to location given by index
            current = self.head
            while index > 0:
                # Update index
                index -= 1
                # Skp to next node
                current = current.next
            # Create new node
            new_node = BinaryNode(item)
            # Point the new node to current node
            new_node.next = current
            # New node's previous points to what current previous points to.
            new_node.previous = current.previous
            # The previous node points to the new node
            current.previous.next = new_node
            # Remove what current previous points to
            current.previous = new_node
            # Increase the size
            self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        # Create new node to hold given data
        new_node = BinaryNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Update new node's previous pointer to old tail
            new_node.previous = self.tail
            # Insert new node at tail
            self.tail.next = new_node
        # Update tial to new node
        self.tail = new_node
        # increase size
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        # Create new node with given item
        new_node = BinaryNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Previous node becomes the new node
            self.head.previous = new_node
            # Insert new node before head
            new_node.next = self.head
        # Update new head
        self.head = new_node
        # Increase size
        self.size += 1

    def delete(self, item):
        """Delete the given item from the linked list, or raise ValueError."""
        # Start at the head node
        current = self.head
        # Keep track of the node before the one containing the given tiem
        # previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the current node is None
        while not found and current is not None:
            # Check if the current node's data matches the given item
            if current.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                # previous = current
                current = current.next

        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if current is not self.head and current is not self.tail:
                # Unlink the found node from its next node
                current.next.previous = current.previous
                # Update the previous node to skip around the found node
                # previous.next = current.next
                current.previous.next = current.next
            # Check if we found a node at the head
            if current is self.head:
                # Update head to the next node
                self.head = current.next
                # Unlink the found node from the next node
                current.next = None
                # Unlink the previous node of the new head
                self.head.previous = None
            # Check if we found a node at the tail
            if current is self.tail:
                # Check if there is a node before the found node
                # if previous is not None:
                if current.previous is not None:
                    # Unlink the previous node from the found node
                    # previous.next = None
                    current.previous.next = None
                # Update tail to the previous node regardless
                self.tail = current.previous  # previous
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        current = self.head
        while current:
            if quality(current.data):
                return current.data
            current = current.next
        return None

def test_linked_list():
    ll = DoublyLinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)

    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('size: ' + str(ll.size))
    print('length: ' + str(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {}'.format(index, repr(item)))

    print(ll.items(reverse=True))

    print('Inserting items by index:')
    for index in range(ll.size):
        item = str(index)
        ll.insert_at_index(index * 2, item)
        print('insert_at_index({}, {})'.format(index * 2, item))
        print(ll)

    print(ll.items(reverse=True))

    print('Deleting items:')
    print(ll)
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    ll.delete('0')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('size: ' + str(ll.size))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
