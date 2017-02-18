# coding=utf8


class DequeNode(object):
    item = None
    next_node = None
    prev_node = None

    def __repr__(self):
        return "<DequeNode '%s'>" % self.item


class Deque(object):
    """
    A double-ended queue or deque (pronounced "deck") is a generalization of
    a stack and a queue that supports adding and removing items from either
    the front or the back of the data structure.

    This implementation support each deque operation in constant worst-case
    time.
    A deque containing n items use space proportional to the number of items
    currently in the deque.
    Additionally, iterator implementation support each operation (including
    construction) in constant worst-case time.
    """

    _first = None
    _last = None
    _count = 0

    def is_empty(self):
        """ Return True if the deque is empty """
        return self._count == 0

    def __len__(self):
        """ Return the number of items on the deque """
        return self._count

    def add_first(self, item):
        """ Add the item to the front """
        node = DequeNode()
        node.item = item

        if self._first:
            node.next_node = self._first
            self._first.prev_node = node
        else:
            self._last = node
        self._first = node

        self._count += 1

    def add_last(self, item):
        """ Add the item to the end """
        node = DequeNode()
        node.item = item

        if self._last:
            node.prev_node = self._last
            self._last.next_node = node
        else:
            self._first = node
        self._last = node

        self._count += 1

    def remove_first(self):
        """ Remove and return the item from the front """
        if not self._first:
            raise KeyError("Remove from empty deque")

        node = self._first
        if self._first.next_node:
            self._first = self._first.next_node
            self._first.prev_node = None
        else:
            self._first, self._last = None, None

        self._count -= 1

        return node.item

    def remove_last(self):
        """ Remove and return the item from the end """
        if not self._last:
            raise KeyError("Remove from empty deque")

        node = self._last
        if self._last.prev_node:
            self._last = self._last.prev_node
            self._last.next_node = None
        else:
            self._first, self._last = None, None

        self._count -= 1

        return node.item

    def __iter__(self):
        it = self._first
        while it:
            yield it.item
            it = it.next_node


if __name__ == "__main__":
    # simple tests
    d = Deque()
    assert d.is_empty()
    assert len(d) == 0
    assert tuple(d) == tuple()
    d.add_first(1)
    assert not d.is_empty()
    d.add_first(0)
    assert len(d) == 2
    d.add_last(2)
    assert tuple(d) == (0, 1, 2)
    d.remove_first()
    assert len(d) == 2
    d.add_last("%")
    assert tuple(d) == (1, 2, "%")
    d.remove_last()
    assert len(d) == 2
    d.remove_last()
    assert not d.is_empty()
    d.remove_last()
    assert d.is_empty()
    d.add_first(-1)
    assert tuple(d) == (-1,)
    d.remove_first()
    assert len(d) == 0
    d.add_last("")
    assert not d.is_empty()
