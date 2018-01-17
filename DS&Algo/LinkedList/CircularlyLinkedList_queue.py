# Error trying to access the empty container
class Empty(Exception):
    pass

class circularQueue:
    """Circularly linked list queue implementation"""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return but do not remove the front element of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')

        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None

        else:
            self._tail._next = oldhead._next        #bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)                #Node will be a tail node

        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail=self._tail._next


