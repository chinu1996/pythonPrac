# Error trying to access the empty container
class Empty(Exception):
    pass

class _DoublyLinkedBase:
    """A basic class providing a doubly linked list representation"""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer              #trailer is after header
        self._trailer._prev = self._header              #header is before trailer
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _insert_between(self, e, predecessor, successor):
        """add an element between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    def _delete_node(self, node):
        """delete a from list and return the element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._next = node._prev = node._element = None  #deprecate the node
        return element

class LinkedDeque(_DoublyLinkedBase):                 # Note the use of inheritance
    """Double-ended queue implementation"""
    def first(self):
        """Return but do not remove the element at the front of the deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element
    def last(self):
        """Return but do not remove the last element of the deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element at the front of the deque"""
        #In the following line the first arg is the element itself, secong is the address of the the header and
        #third is the ADDRESS stored in header for the next element which will become the successor
        self._insert_between(e, self._header, self._header._next)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)    #Use of inherited method

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)   #Use of inherited method


