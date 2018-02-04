class Tree:
    """An abstract base class representing a tree structure"""

    # --------nested Position class-----
    class Position:
        """An abstraction representing a location of a single element"""

        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError('must be implemented by a subclass')

        def __eq__(self, other):
            """return true if the position represents the same location"""
            raise NotImplementedError('must be implemented by a subclass')

        def __ne__(self, other):
            """Return true if the other does not represent the same location"""
            return not (self == other)

    # -------abstract methods that concrete subclass must support-----
    def root(self):
        """Return Position representing the trees root"""
        raise NotImplementedError('must be implemented by a subclass')

    def parent(self, p):
        """Return the postion representing P's parent"""
        raise NotImplementedError('must be implemented by a subclass')

    def num_children(self, p):
        """Return the number of the children that position p has"""
        raise NotImplementedError('must be implemented by a subclass')

    def children(self, p):
        """Generate an iteration og Postions representing p's children"""
        raise NotImplementedError('must be implemented by a subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('must be implemented by a subclass')

    # ---------concrete methods implemented in this class-----
    def is_root(self, p):
        """Return True if the element p is the root"""
        return self.root() == p

    def is_leaf(self, p):
        """Return true if the element p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return true if the tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height2(self, p):
        """Return the height of the tree at posititon p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """return the height of the tree at position p

        If there is no p then return the height of the entire tree"""
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """Generate an iteration of the trees elements """
        for p in self.positions():
            yield p.element()


