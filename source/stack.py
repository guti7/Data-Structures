#!python

from linkedlist import LinkedList


# implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack"""
        # Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # Push given item, the top is the end of list
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # Return top item, if any
        # return self.list.get_at_index(self.length())
        # return self.list.tail
        try:
            return self.list.get_at_index(self.length() - 1)
        except ValueError as error:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # Remove and return top item, if any
        pop = self.peek()
        self.list.delete(pop)
        return pop


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):
    # LIFO
    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # Check if empty, the length zero
        return self.length() == 0

    def length(self):
        """Return the number of items in this stack"""
        # Count number of items, the size of list
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # Insert given item at top, the top is the end of list
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # Return top item, if any
        return self.list[-1] if not self.is_empty() else None
        # if self.is_empty():
        #     return None
        # return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # Remove and return top item, if any
        # return self.list.pop() if not self.is_empty else raise ValueError
        if self.is_empty():
            raise ValueError("Can't pop empty stack: {}".format(self.list))
        return self.list.pop()


# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
