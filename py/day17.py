from collections import defaultdict

def psum(pos, points):
    return [
        [p[0]+pos[0], p[1]+pos[1]]
        for p in points
    ]

class Hline:
    def __init__(self, pos):
        self.shape = psum(pos, [[0, 0], [0, 1], [0, 2], [0, 3]])

class Cross:
    def __init__(self, pos):
        self.shape = psum(pos, [[2, 1], [1, 0], [1, 1], [1, 2], [0, 1]])

class Ell:
    def __init__(self, pos):
        self.shape = psum(pos, [[2, 2], [1, 2], [0, 0], [0, 1], [0, 2]])

class Vline:
    def __init__(self, pos):
        self.shape = psum(pos, [[3, 0], [2, 0], [1, 0], [0, 0]])

class Square:
    def __init__(self, pos):
        self.shape = psum(pos, [[1, 0], [1, 1], [0, 0], [0, 1]])

class Chamber:
    BLOCKS = [Hline, Cross, Ell, Vline, Square]
    SEEN = defaultdict(list)

    def __init__(self, moves):
        self.moves = moves
        self.rows = defaultdict(list)
        self.first = -1
        self.last_key = None
        self.block_count = 0
        self.move_idx = 0
        self.profile = [0, 0, 0, 0, 0, 0, 0] # Max height per column
        
    def first_rock(self):
        if self.first == -1:
            return [-1, 0]
        return [self.first, min(self.rows[self.first])]

    def register_state(self):
        """
        Part 2: record the 'profile' -- that is the relative height of all
        seven columns, together with the current move index. If this ever
        recurs, we can stop, as every subsequent state can now be derived.
        """
        p = min(self.profile)
        prf = [a-p for a in self.profile]
        key = (tuple(prf), self.move_idx)
        found = key in Chamber.SEEN
        Chamber.SEEN[key].append((self.block_count, self.first))
        self.last_key = key
        return found

    def freeze(self, block):
        for y, x in block.shape:
            if y > self.first:
                self.first = y
            if y > self.profile[x]:
                self.profile[x] = y
            self.rows[y].append(x)

    def can_move(self, block, delta):
        for y, x in block.shape:
            ypos = y + delta[0]
            if ypos < 0:
                return False
            xpos = x + delta[1]
            if xpos < 0 or xpos > 6:
                return False
            for r in self.rows.get(ypos, []):
                if r==xpos:
                    return False
        return True

    def get_jet(self):
        delta_x = self.moves[self.move_idx]
        self.move_idx += 1
        self.move_idx %= len(self.moves)
        return delta_x

    def add_block(self):
        ypos, _ = self.first_rock()
        ypos += 4
        xpos = 2

        block = Chamber.BLOCKS[self.block_count%5]([ypos, xpos])        
        while True:
            delta_x = self.get_jet()
            if self.can_move(block, [0, delta_x]):
                block.shape = psum([0, delta_x], block.shape)
            if self.can_move(block, [-1, 0]):
                block.shape = psum([-1, 0], block.shape)
            else:
                self.freeze(block)
                self.block_count += 1
                break
        return self.register_state()
    
if __name__ == '__main__':
    with open('/Users/stefan/work/AoC22/d/17') as f:
        data = f.read()

    moves = []
    for c in data:
        if c == '<':
            moves.append(-1)
        elif c == '>':
            moves.append(1)

    chamber = Chamber(moves)
    # Keep going until we find a recurring state
    while True:
        if chamber.add_block():
            break

    # We have a recurring state. Work out the periodicity
    spec = Chamber.SEEN[chamber.last_key]
    blocks_period = spec[1][0] - spec[0][0]
    height_period = spec[1][1] - spec[0][1]

    # We can skip most of the mega range
    full = (1_000_000_000_000 - chamber.block_count) // blocks_period
    remainder = 1_000_000_000_000 - chamber.block_count - blocks_period * full

    # Run out the remainder
    for i in range(remainder):
        if chamber.block_count == 2022:
            print(chamber.first) # Part 1
        chamber.add_block()

    print(chamber.first + full*height_period + 1) # Part 2