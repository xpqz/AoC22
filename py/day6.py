import itertools
import sys


def windowed(l, stride):
    return zip(*[itertools.islice(l, i, sys.maxsize) for i in range(stride)])


def marker(d, size):
    for i, e in enumerate(windowed(data, size)):
        if len(set(e)) == size:
            return i + size


with open('/Users/stefan/work/AoC22/d/6') as f:
    data = f.read()

print(marker(data, 4))
print(marker(data, 14))
