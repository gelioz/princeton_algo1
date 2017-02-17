# coding=utf8
import math
import random
import sys
import statistics

from percolation import Percolation


class PercolationStats(object):
    """ Estimation of percolation threshold using Monte Carlo simulation """

    def __init__(self, n, trials):
        """ Perform trials independent experiments on an n-by-n grid """
        self._thresholds = []
        for _ in range(trials):
            self._thresholds.append(self._simulate(n))

    def _simulate(self, n):
        """ Process independent percolation experiment """
        p = Percolation(n)
        while True:
            p.open(random.randint(0, n - 1), random.randint(0, n - 1))
            if p.is_percolates():
                return p.number_of_open_sites() / (n * n)

    def mean(self):
        """ Sample mean of percolation threshold """
        return statistics.mean(self._thresholds)

    def standart_deviation(self):
        """ Sample standard deviation of percolation threshold """
        return statistics.stdev(self._thresholds)

    def confidence_low(self):
        """ Return low endpoint of 95% confidence interval """
        mean, stddev = self.mean(), self.standart_deviation()
        return mean - (1.96 * stddev) / math.sqrt(len(self._thresholds))

    def confidence_high(self):
        """ Return high endpoint of 95% confidence interval """
        mean, stddev = self.mean(), self.standart_deviation()
        return mean + (1.96 * stddev) / math.sqrt(len(self._thresholds))


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        trials = int(sys.argv[2])
    except (IndexError, ValueError):
        print("Usage: python3 percolation_stats.py *n* *trials*")
        sys.exit()

    ps = PercolationStats(n, trials)
    print("mean:\t\t\t\t%f" % ps.mean())
    print("stddev:\t\t\t\t%f" % ps.standart_deviation())
    print("95%% confidence interval:\t[%f, %f]" % (
        ps.confidence_low(), ps.confidence_high()
    ))
