from .GeneralTrees import Tree
class BinaryTree(Tree):
    """an abstract base class representing a binary tree structure"""

    # -----additional abstract methods-------
    def left(self, p):
        """Return the Position representing p's left child
        return None if p does not have a left child"""
        raise NotImplementedError('must be implemented by a subclass')

    def right(self, p):
        """Return the Position representing p's right child
        return None if p does not have a right child"""
        raise NotImplementedError('must be implemented by a subclass')

    # -----concrete methods implemented in this class----
    def sibling(self, p):
        """Return a Position representing p's sibling
        (or none if no sibling)"""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):  # if p is the left child of the parent
                return self.right(parent)  # return the right child of the parent (possibly None)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing P's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

