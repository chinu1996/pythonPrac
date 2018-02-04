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
            p = self._data.add_last(self._item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e foem the list of favorites"""
        p = self._find_position(e)              #find the position of the element
        if p is not None:
            self._data.delete(p)                #delete if found


    def top(self, k):
        """Generate a sequence of top k elements in terms of access count"""
        if not  1 <= k <=len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item  = walk.element()
            yield item._value
            walk = self._data.after(walk)


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heurisitc"""

    #----override _move_up to provide move to front semantics
    def _move_up(self, p):
        """Move accessed item to the front of the list"""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # we override top as the list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access counts"""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value of k")

        # we begin by making a copy of the list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # we repeatedly find report and remove element with largest count
        for j in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            #we have found the element with the highest count
            yield highPos.element()._value
            temp.delete(highPos)
            