
from collections import deque
from dataclasses import dataclass
import re

def minmax(numbers):
    res = {
        'xmin': float('inf'),
        'xmax': float('-inf'),
        'ymin': float('inf'),
        'ymax': float('-inf'),
        'zmin': float('inf'),
        'zmax': float('-inf'),
    }

    for x, y, z in numbers:
        res['xmin'] = min(x, res['xmin'])
        res['ymin'] = min(y, res['ymin'])
        res['zmin'] = min(z, res['zmin'])

        res['xmax'] = max(x, res['xmax'])
        res['ymax'] = max(y, res['ymax'])
        res['zmax'] = max(z, res['zmax'])

    return res

def flood_fill(numbers):
    shape = minmax(numbers)
    cave = {}
    for n in numbers:
        cave[tuple(n)] = 1
    Q = deque()
    Q.append((shape['xmin']-1, shape['ymin']-1, shape['zmin']-1))
    hull = 0
    while Q:
        n = Q.popleft()
        elem = cave.get(n, 0)
        if elem == 0:
            cave[n] = 2
            if n[0]-1>=shape['xmin']-1:
                Q.append((n[0]-1, n[1], n[2]))
            if n[1]-1>=shape['ymin']-1:
                Q.append((n[0], n[1]-1, n[2]))
            if n[2]-1>=shape['zmin']-1:
                Q.append((n[0], n[1], n[2]-1))

            if n[0]+1<=shape['xmax']+1:
                Q.append((n[0]+1, n[1], n[2]))
            if n[1]+1<=shape['ymax']+1:
                Q.append((n[0], n[1]+1, n[2]))
            if n[2]+1<=shape['zmax']+1:
                Q.append((n[0], n[1], n[2]+1))
        elif elem == 1:
            hull += 1

    return hull

@dataclass(frozen=True)
class Cube:
    x: int
    y: int
    z: int

    def faces(self):
        return set([
            (   # ∆y = 0
                (self.x,   self.y, self.z), 
                (self.x+1, self.y, self.z), 
                (self.x,   self.y, self.z+1), 
                (self.x+1, self.y, self.z+1)
            ),
            (   # ∆y = 1
                (self.x,   self.y+1, self.z), 
                (self.x+1, self.y+1, self.z), 
                (self.x,   self.y+1, self.z+1), 
                (self.x+1, self.y+1, self.z+1)
            ),
            (   # ∆x = 0
                (self.x, self.y,   self.z), 
                (self.x, self.y+1, self.z), 
                (self.x, self.y,   self.z+1), 
                (self.x, self.y+1, self.z+1)
            ),
            (   # ∆x = 1
                (self.x+1, self.y,   self.z), 
                (self.x+1, self.y+1, self.z), 
                (self.x+1, self.y,   self.z+1), 
                (self.x+1, self.y+1, self.z+1)
            ),
            (   # ∆z = 0
                (self.x,   self.y,   self.z), 
                (self.x+1, self.y,   self.z), 
                (self.x,   self.y+1, self.z), 
                (self.x+1, self.y+1, self.z)
            ),
            (   # ∆z = 1
                (self.x,   self.y,   self.z+1), 
                (self.x+1, self.y,   self.z+1), 
                (self.x,   self.y+1, self.z+1), 
                (self.x+1, self.y+1, self.z+1)
            ),
        ])

if __name__=="__main__":
    with open('../d/18') as f:
        data = f.read().splitlines()

    numbers = [
        [int(n) for n in re.findall(r'(-?\d+)', row)]
        for row in data
    ]

    points = [
        Cube(*point) for point in numbers
    ]

    faces = set()
    for p in points:
        faces ^= p.faces()

    print(f'Part 1: {len(faces)}')
    print(f'Part 1: {flood_fill(numbers)}')


