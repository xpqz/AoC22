from functools import reduce
import re

def manhattan(s, b):
    return abs(s[0]-b[0])+abs(s[1]-b[1])

def merge_ranges(acc, item):
    if item[1] > acc[1]:
        return [acc[0], item[1]]
    return acc

def merge_ranges_piecewise(acc, item):
    if acc == []:
        return [list(item)]
    last = acc[-1]
    if item[0] > last[1]: # Disjoint
        return acc+[list(item)]
    elif item[1] > last[0]:
        return acc[:-1]+[[last[0], max(last[1], item[1])]]
    return acc
 
def find_ranges(sensors, target):
    excluded = []
    for sensor, mhd in sensors.items():
        ydist = abs(sensor[1]-target)
        max_xdist = mhd-ydist
        if max_xdist > 0:
            excluded.append((sensor[0]-max_xdist, sensor[0]+max_xdist))

    return sorted(excluded)

def part1(sensors, beacons, target):
    srange = find_ranges(sensors, target)
    redux = reduce(merge_ranges, srange)
    redux[1] += 1
    remove = 0

    # Remove any beacons
    for beacon in beacons:
        if beacon[1] == target and beacon[0] in range(*redux):
            remove += 1

    return (len(list(range(*redux)))-remove)

def part2(sensors, target):
    for y in range(target+1):
        srange = find_ranges(sensors, y)
        redux = reduce(merge_ranges_piecewise, srange, [])
        x = 0
        for left, right in redux:
            if x < left:
                return x * 4000000 + y
            x = max(x, right + 1)
            if x > target:
                break
    return -1

if __name__ == '__main__':
    with open('/Users/stefan/work/AoC22/d/test') as f:
        data = f.read().splitlines()
    spec = [list(map(int, re.findall(r'(-?\d+)', row))) for row in data]

    sensors = {}
    beacons = set()
    for row in spec:
        sensor, beacon = (row[0], row[1]), (row[2], row[3])
        sensors[sensor] = manhattan(sensor, beacon)
        beacons.add(beacon)

    # print(part1(sensors, beacons, target=2000000))
    print(part1(sensors, beacons, target=10))

    # Part 2
    print(part2(sensors, target=4000000))
    
    


