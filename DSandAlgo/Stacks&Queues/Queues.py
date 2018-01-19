#array based implementation of queue
class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Three instance variables"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the size of the queue"""
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return BUT DO NOT REMOVE the first element of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # shriking an underlying array
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """Add and element to the back of the list"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list with capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)

        self._front = 0


class Empty(Exception):
    pass
