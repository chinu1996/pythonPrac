from .binaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    """Linked representation of a binary tree"""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right


    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user"""
            self._container = container
            self._node = node


        def element(self):
            # return the element stored at this position
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node


    def _validate(self, p):
        """Return the associated node if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be at valid position')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node


    def _make_position(self, node):
        """Return Position instance for given node"""
        return self.Position(self, node) if node is not None else None


    # --------------BINARY TREE CONSTRUCTOR ---------

    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    # --------PUBLIC ACCESSORS---------
    def __len__(self):
        return self._size

    def root(self):
        """Return the root position of the tree"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of the p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of the p's left child(or None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of the p's right child(or None if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count


    #----NON PUBLIC UPDATE METHODS-----
    def _add_root(self, e):
        """Place element at the root of an empty tree and return new Position
        raise ValueError if tree is non empty"""
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for a postion P storing element e.
        return the position of the new node
        raise a ValueError if the node already has a left child"""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for a postion P storing element e.
        return the position of the new node
        raise a ValueError if the node already has a right child"""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def replace(self, p, e):
        """Replace the element at position p with e and return old element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p and replace it with its child, if any
        Return the element that had been stored at Position p
        raise ValueError if position p is invalid or p has two children"""
        node = self._validate(p)
        if self.children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right           #might be none
        if child is not None:
            child._parent = node._parent        #child grandparent becomes the parent
        if node is self._root:
            self._root = child          #child becomes the root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach t1 and t2 as a subtree at external p"""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('p must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('trees must be of same type')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2.size = 0

