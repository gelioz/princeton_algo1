# coding=utf8
import sys

from randomized_queue import RandomizedQueue


# 1. takes a command-line integer k
# 2. reads in a sequence of strings from standard input and prints exactly k of
# them, uniformly at random.
# 3. prints each item from the sequence at most once.

try:
    k = int(sys.argv[1])
except (IndexError, ValueError):
    print("Usage: python3 permutation.py *k*")
    sys.exit()

queue = RandomizedQueue()
for item in sys.stdin.read().split():
    queue.enqueue(item)

for _ in range(k):
    print(queue.dequeue())
