from .DoublyPositionList import PositionalList

class FavoritesList:
    """List of elements ordered from most frequently accessed to least"""

    # --------------NESTED ITEM CLASS----------

    class _item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    # --------------NON PUBLIC UTILITIES--------

    def _find_position(self, e):
        """search for element e and return its Position (or none if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """move an item at position p earlier in the list based on access count"""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count()):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    #---------PUBLIC METHODS------------
    def __init__(self):
        """Create an empty list of favorites"""
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        """access element e therby increasing its access counts"""
        p = self._find_position(e)
        if p is None:
            self._data.delete(p)

    def top(self, k):
        """Generate a sequence of top k elements in terms of access count"""
        if not  1 <= k <=len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item  = walk.element()
            yield item._value
            walk = self._data.after(walk)
