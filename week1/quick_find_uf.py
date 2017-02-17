# coding=utf8
import sys


class QuickFindUF(object):
    """
    The QuickFindUF class represents a union–find data type (also known as
    the disjoint-sets data type). It supports the union and find operations,
    along with a connected operation for determining whether two sites are in
    the same component and a count operation that returns the total number of
    components. The union–find data type models connectivity among a set of n
    sites, named 0 through n–1. The is-connected-to relation must be an
    equivalence relation (reflexive, symmetric and transitive).

    This implementation uses quick find. Initializing a data structure with n
    sites takes linear time. Afterwards, the find, connected, and count
    operations take constant time but the union operation takes linear time.

    All credits goes to Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n):
        """ Initializes an empty union–find data structure with n sites 0
            through n-1.
        """
        self._ids = list(range(n))
        self._count = n

    def _validate_index(self, idx):
        """ Validate that p is a valid index """
        n = len(self._ids)
        if idx < 0 or idx >= n:
            raise IndexError("Index %d is not between 0 and %d" % (idx, n - 1))

    def connected(self, p, q):
        """ Returns True if the sites p and q are in the same component. """
        self._validate_index(p)
        self._validate_index(q)
        return self._ids[p] == self._ids[q]

    def count(self):
        """ Returns the number of components """
        return self._count

    def find(self, p):
        """ Returns the component identifier for the component containing
            site p.
        """
        self._validate_index(p)
        return self._ids[p]

    def union(self, p, q):
        """ Merges the component containing site p with the the component
            containing site q.
        """
        self._validate_index(p)
        self._validate_index(q)
        p_id, q_id = self._ids[p], self._ids[q]

        # p and q are already in the same component
        if p_id == q_id:
            return

        for i in range(len(self._ids)):
            if self._ids[i] == p_id:
                self._ids[i] = q_id
        self._count -= 1


if __name__ == "__main__":
    # Reads in a sequence of pairs of integers (between 0 and n-1) from
    # standard input, where each integer represents some site; if the sites
    # are in different components, merge the two components and print
    # the pair to standard output.
    n = int(sys.stdin.readline())
    uf = QuickFindUF(n)
    for pair in sys.stdin:
        p, q = map(int, pair.split())
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print(p, q)

    print("%d components" % uf.count())
