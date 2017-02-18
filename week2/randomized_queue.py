# coding=utf8
import sys
import random


class RandomizedQueue(object):
    """
    A randomized queue is similar to a stack or queue, except that the item
    removed is chosen uniformly at random from items in the data structure.

    This implementation support each randomized queue operation (besides
    creating an iterator) in constant amortized time. Additionally, iterator
    implementation support operation next() in constant worst-case time and
    construction in linear time.

    Disclaimer: Python has it's own resize mechanism for lists, so '_resize'
    method and pre-init of lists are implemented just for educational purpose.
    """

    def __init__(self):
        """ Construct an empty randomized queue """
        self._q = [None] * 2
        self._n = 0

    def is_empty(self):
        """ Return True if queue is empty """
        return self._n == 0

    def __len__(self):
        """ Return the number of items on the queue """
        return self._n

    def _resize(self, capacity):
        """ Resize the underlying array """
        temp = [None] * capacity
        for i in range(self._n):
            temp[i] = self._q[i]
        self._q = temp

    def enqueue(self, item):
        """ Add the item to this queue """

        # double size of array if necessary
        if self._n == len(self._q):
            self._resize(2 * len(self._q))

        self._q[self._n] = item
        self._n += 1

    def dequeue(self):
        """ Remove and return random item from queue """
        if self.is_empty():
            raise KeyError("Dequeue from empty queue")

        # choose random element, pop it and replace
        # with last element from array
        idx = random.randint(0, self._n - 1)
        item = self._q[idx]
        self._q[idx] = self._q[self._n - 1]
        self._q[self._n - 1] = None
        self._n -= 1

        # shrink size of array if necessary
        if self._n > 0 and self._n == len(self._q) // 4:
            self._resize(len(self._q) // 2)

        return item

    def sample(self):
        """ Return (but not remove) a random item from queue """
        if self.is_empty():
            raise KeyError("Sample from empty queue")

        return self._q[random.randint(0, self._n - 1)]

    def __iter__(self):
        """ Return an independent iterator over items in random order """
        items = self._q[:self._n]
        random.shuffle(items)
        yield from items


if __name__ == "__main__":
    queue = RandomizedQueue()

    for item in sys.stdin:
        if item != "-":
            queue.enqueue(item)
        elif not queue.is_empty():
            print(queue.dequeue())

    print("(%d left on queue)" % len(queue))
