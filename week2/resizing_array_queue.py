# coding=utf8
import sys


class ResizingArrayQueue(object):
    """
    The ResizingArrayQueue class represents a first-in-first-out (FIFO) queue
    of items. It supports the usual enqueue and dequeue operations, along with
    methods for peeking at the first item, testing if the queue is empty, and
    iterating through the items in FIFO order.

    This implementation uses resizing array, which double the underlying array
    when it is full and halves underlying array when it is one-quarter full.
    The enqueue and dequeue operations take constant amortized time. The len(),
    peek, and is_empty operations takes constant time in the worst case.

    All credits goes to Robert Sedgewick and Kevin Wayne.

    Disclaimer: Python has it's own resize mechanism for lists, so '_resize'
    method and pre-init of lists are implemented just for educational purposes.
    """

    def __init__(self):
        """ Initializes an empty queue """
        self._q = [None] * 2
        self._n, self._first, self._last = 0, 0, 0

    def is_empty(self):
        """ Return True if queue is empty """
        return self._n == 0

    def __len__(self):
        """ Returns the number of items in this queue """
        return self._n

    def _resize(self, capacity):
        """ Resize the underlying array """
        temp = [None] * capacity
        for i in range(self._n):
            temp[i] = self._q[(self._first + i) % len(self._q)]
        self._q = temp

        self._first, self._last = 0, self._n

    def enqueue(self, item):
        """ Adds the item to this queue """

        # double size of array if necessary and recopy to front of array
        if self._n == len(self._q):
            self._resize(2 * len(self._q))

        self._q[self._last] = item
        self._n += 1
        self._last += 1

        if self._last == len(self._q):
            self._last = 0  # wrap-around

    def dequeue(self):
        """ Removes and returns least recently added item from queue """
        if self.is_empty():
            raise KeyError("Dequeue from empty queue")

        item = self._q[self._first]
        self._q[self._first] = None
        self._n -= 1
        self._first += 1

        if self._first == len(self._q):
            self._first = 0  # wrap-around

        # shrink size of array if necessary
        if self._n > 0 and self._n == len(self._q) // 4:
            self._resize(len(self._q) // 2)

        return item

    def peek(self):
        """ Returns the item least recently added to this queue """
        if self.is_empty():
            raise KeyError("Peek from empty queue")

        return self._q[self._first]

    def __iter__(self):
        """ Returns an iterator that iterates over the items
            in this queue in FIFO order.
        """
        for i in range(self._n):
            yield self._q[i + self._first % len(self._q)]


if __name__ == "__main__":
    queue = ResizingArrayQueue()

    for item in sys.stdin:
        if item != "-":
            queue.enqueue(item)
        elif not queue.is_empty():
            print(queue.dequeue())

    print("(%d left on queue)" % len(queue))
