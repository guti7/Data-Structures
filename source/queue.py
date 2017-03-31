#!python

from linkedlist import LinkedList


# implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):
    # FIFO
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue"""
        # Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        # Return front item, if any
        return self.list.get_at_index(0) if not self.is_empty() else None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        # TODO: Remove and return front item, if any
        front = self.front()
        self.list.delete(front)
        return front
        

# implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):
    # FIFO
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue"""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # Insert given item, at the end of list
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        # Return front item, if any. The front is the start of the list
        return self.list[0] if not self.is_empty() else None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        # Remove and return front item, if any
        if not self.is_empty():
            deq = self.front()
            self.list.remove(deq)
            return deq
        raise ValueError("Can't dequeue empty queue: {}".format(self.list))


# implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
