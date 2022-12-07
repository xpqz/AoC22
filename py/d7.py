import re

P1 = 0
P2 = 7e7


def size(input, idx=0):
    res = 0
    global P1
    global P2
    while idx < len(input):
        line = input[idx]
        if m := re.match(r'^(\d+)\s+(.+)', line):
            res += int(m.group(1))
        elif line.endswith('..'):
            return (res, idx)
        elif line.startswith('$ cd'):
            (dir_size, idx) = size(input, idx + 1)
            if dir_size < 1e5:
                P1 += dir_size
            if dir_size < P2 and dir_size > needed:
                P2 = dir_size
            res += dir_size
        idx += 1
    return (res, idx)


if __name__ == "__main__":
    with open('/Users/stefan/work/AoC22/d/7') as f:
        data = f.read().splitlines()

    total_size = 0
    for i in data:
        if m := re.findall(r'(\d+)', i):
            total_size += sum(int(n) for n in m)
    needed = 3e7 - (7e7 - total_size)

    size(data)

    print(P1, P2)