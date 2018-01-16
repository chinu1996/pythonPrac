# Error trying to access the empty container
class Empty(Exception):
    pass


class LinkedList:
    # --------------Nested node class----------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ------------------- stack methods-------------
    def __init__(self):
        """Create new empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the size of the array"""
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but do not remove the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the top element of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer=self._head._element
        self._head=self._head._next         # Bypass the former top node
        self._size -= 1
        return answer

