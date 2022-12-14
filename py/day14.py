from copy import deepcopy
import re

def pour(cave, last):
    ypath = 0
    xpath = 500
    while ypath < last:
        if cave.get((xpath, ypath+1), 0) != 0:         # rock, or sand
            if cave.get((xpath-1, ypath+1), 0) == 0:   # try left
                xpath -= 1            
            elif cave.get((xpath+1, ypath+1), 0) == 0: # try right
                xpath += 1
            else:
                cave[(xpath, ypath)] = 2               # settle
                return True
        ypath += 1
    return False

if __name__ == '__main__':
    with open('/Users/stefan/work/AoC22/d/14') as f:
        data = f.read().splitlines()
    spec = [re.findall(r'(\d+),(\d+)', row) for row in data]

    cave = {}
    lasty = 0
    lastx = 0
    for pairs in spec:
        d = []
        for start, end in pairs:
            d.append([int(start), int(end)])
        for b in range(1, len(d)):
            pair = d[b-1], d[b]
            xs, ys = list(map(sorted, list(zip(*pair))))
            expanded = [(x, y) for x in range(xs[0], xs[1]+1) for y in range(ys[0], ys[1]+1)]
            for p in expanded:
                cave[p] = 1
                if p[1]>lasty:
                    lasty=p[1]
                if p[0]>lastx:
                    lastx=p[0]

    # Part 1
    p1cave = deepcopy(cave)
    while True:
        if not pour(p1cave, lasty):
            break

    print(len(list(filter(lambda x:x==2, p1cave.values()))))
    for x in range(lastx+500):
        cave[(x, lasty+2)] = 1
    
    while True:
        pour(cave, lasty+3)
        if cave.get((500, 0), 0) == 2:
            break
    print(len(list(filter(lambda x:x==2, cave.values()))))

