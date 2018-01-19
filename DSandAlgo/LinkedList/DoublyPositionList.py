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

class PositionalList(_DoublyLinkedBase):
    """Class allowing positional access"""
    #--------------nested Postion class--------

    class Position:
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user"""

            self._container = container
            self._node = node

        def element(self):
            """Return the element stored in that position"""
            return self._node._element

        def __eq__(self, other):
            """return true if a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """return true if other does not represent the same location"""
            return not (self == other)



    #------------UTILITY METHODS-----------------

    def _validate(self, p):
        """Return position's node or raise appropriate erroe if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError(' p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')

        return p._node
    def _make_Position(self, node):
        """Return position instance for given node(or None if sentinel)"""
        if node is self._header or self._trailer:       #boundary violation
            return None
        else:
            return self.Position(self, node)            #legitimate position


    #---------------ACCESSORS------


    def first(self):
        """Return the first Position in the list"""
        return self._make_Position(self._header._next)

    def last(self):
        """return the last position in the list"""
        return self._make_Position(self._trailer._prev)

    def before(self, p):
        """Return the position just before the position P"""
        node = self._validate(p)
        return self._make_Position(node._prev)

    def after(self, p):
        """Return the position just after position p"""
        node = self._validate(p)
        return self._make_Position(node._next)
    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)


    #------------MUTATORS---------
    #override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return the new position"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_Position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element at the last of the list and return the new postion"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Add element e into the list before the postion p"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Add element e into the list after the position p"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at position P"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """"replace the element at position p eith e

        return the element formely at position p"""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


#---------------SORTING A POSITIONAL LIST------------
def insertionSort(L):
    """"Sort positional list of comparable elements"""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():  # if the pivot is already sorted
                marker = pivot  # marker becomes pivot

            else:
                walk = marker
                while walk != L.first() and L.before(walk).element > value:
                    walk = L.before(walk)

                L.delete(pivot)
                L.add_before(walk, value)

