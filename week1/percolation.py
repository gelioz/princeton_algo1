# coding=utf8
# from quick_find_uf import QuickFindUF
from weighted_quick_union_uf import WeightedQuickUnionUF


class Percolation(object):
    """ Model of percolation system with n-by-n grid of sites.

        Each site is either open or blocked.

        A full site is an open site that can be connected to an open site in
        top row via chain of neighboring (left, right, up, down) open sites.

        We say system percolates if there is a full site in bottom row.
        In other words, a system percolates if we fill all open sites connected
        to top row and that process fills some open site on bottom row.
    """

    def __init__(self, n):
        """ Create percolation model with n-by-n grid and all sites blocked """
        self._n = n
        self._grid = [[False] * n for _ in range(n)]
        # create sites for n-by-n grid and 2 "virtual" sites for top and bottom
        # self._uf = QuickFindUF(n * n + 2)
        self._uf = WeightedQuickUnionUF(n * n + 2)  # QuickFindUF(n * n + 2)
        # connect top and bottom virtual sites with respecting sides of grid
        self._top_idx = n * n
        self._bottom_idx = n * n + 1
        for i in range(n):
            self._uf.union(self._top_idx, i)
            self._uf.union(self._bottom_idx, (n - 1) * n + i)

    def _validate_indexes(self, row, col):
        """ Validate that row and col is a valid grid index """
        if min(row, col) < 0 or max(row, col) >= self._n:
            raise IndexError(
                "Incorrect position (%d, %d) in grid of size %d" % (
                    row, col, self._n
                )
            )

    def open(self, row, col):
        """ Open site on position (row, col) if it is not open already """
        self._validate_indexes(row, col)
        self._grid[row][col] = True
        site_idx = row * self._n + col
        # connect to left site
        if col > 0 and self.is_open(row, col - 1):
            self._uf.union(site_idx, site_idx - 1)
        # connect to right site
        if col < self._n - 1 and self.is_open(row, col + 1):
            self._uf.union(site_idx, site_idx + 1)
        # connect to upper site
        if row > 0 and self.is_open(row - 1, col):
            self._uf.union(site_idx, (row - 1) * self._n + col)
        # connect to lower site
        if row < self._n - 1 and self.is_open(row + 1, col):
            self._uf.union(site_idx, (row + 1) * self._n + col)

    def is_open(self, row, col):
        """ Return True if site on position (row, col) is open """
        self._validate_indexes(row, col)
        return self._grid[row][col]

    def is_full(self, row, col):
        """ Return True if site on position (row, col) is full """
        self._validate_indexes(row, col)
        return self._uf.connected(self._top_idx, row * self._n + col)

    def number_of_open_sites(self):
        """ Return number of open sites in n-by-n grid """
        return sum(sum(line) for line in self._grid)

    def is_percolates(self):
        """ Return True if system percolates """
        return self._uf.connected(self._top_idx, self._bottom_idx)


if __name__ == "__main__":
    p = Percolation(3)
    assert p.number_of_open_sites() == 0
    assert not p.is_open(0, 0)
    p.open(0, 0)
    assert p.is_open(0, 0)
    p.open(1, 2)
    assert not p.is_full(1, 2)
    p.open(1, 0)
    assert p.number_of_open_sites() == 3
    p.open(1, 1)
    assert p.is_full(1, 1)
    assert not p.is_percolates()
    p.open(2, 2)
    assert p.number_of_open_sites() == 5
    assert p.is_full(2, 2)
    assert p.is_percolates()
