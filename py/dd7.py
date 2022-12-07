from functools import reduce
import re

with open('/Users/stefan/work/AoC22/d/7') as f:
    data = f.read().splitlines()

sizes = []


def fun(acc, elem):
    if elem.startswith('$ cd ..'):
        sizes.append(acc.pop(0))
        return acc

    if elem.startswith('$ cd'):
        return [0] + acc

    if m := re.match(r'(\d+)', elem):
        v = int(m.group(1))
        for i in range(len(acc)):
            acc[i] += v

    return acc


sizes.extend(reduce(fun, data, []))
print(sum(s for s in sizes if s < 100_000))
print(min(a for a in sizes if a >= 30_000_000 - (70_000_000 - sizes[-1])))
