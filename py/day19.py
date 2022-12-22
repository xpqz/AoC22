from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass, field
from math import prod
import re

@dataclass
class Recipe:
    ore: int
    clay: int
    obsidian: tuple[int, int]
    geode: tuple[int, int]
    max_ore: int = field(init=False)

    def __post_init__(self):
        self.max_ore = max(self.obsidian[0], self.geode[0], self.clay)

@dataclass
class State:
    ore: int
    geode: int
    clay: int
    obsidian: int

    ore_r: int
    geode_r: int
    clay_r: int
    obsidian_r: int

    def _produce(self):
        self.ore += self.ore_r
        self.geode += self.geode_r
        self.clay += self.clay_r
        self.obsidian += self.obsidian_r

    def produce(self):
        s = deepcopy(self)
        s._produce()
        return s

    def build(self, recipe, robot):
        s = deepcopy(self)
        s._produce()
        if robot == 'ore': 
            s.ore -= recipe.ore
            s.ore_r += 1
        elif robot == 'geode':
            s.ore -= recipe.geode[0]
            s.obsidian -= recipe.geode[1]
            s.geode_r += 1
        elif robot == 'clay':
            s.ore -= recipe.clay
            s.clay_r += 1
        elif robot == 'obsidian':
            s.ore -= recipe.obsidian[0]
            s.clay -= recipe.obsidian[1]
            s.obsidian_r += 1
        return s

    def buildable(self, recipe):
        """
        Return a set of buildable robots, given the current state. Three aspects to this:

        1. Do we have sufficient mineral resources "in the bank"?
        2. Do we NEED to build a given robot? That is, if we already have enough 
           robots of a type to satisfy the needs for other robot builds, we skip.
        3. [Heuristic] If we can build a Geode, don't explore any other options.

        """
        if self.ore >= recipe.geode[0] and self.obsidian >= recipe.geode[1]: # Geode takes ore and obsidian
            return {'geode'}

        r = {'none'}
        if self.ore >= recipe.ore and self.ore_r < recipe.max_ore:
            r.add('ore')
        
        if self.ore >= recipe.clay and self.clay_r < recipe.obsidian[1]: # A clay robot requires ore
            r.add('clay')

        if self.ore >= recipe.obsidian[0] and self.clay >= recipe.obsidian[1] and self.obsidian_r < recipe.geode[1]:
            r.add('obsidian')

        return r

def search(recipe, minutes):
    """
    Key observation:

    If at time t we built no robot when we could have, don't build any of those
    we skipped at time t at time t+1. This single prune decimates the search space.
    """
    queue = deque()
    queue.append((State(0, 0, 0, 0, 1, 0, 0, 0), 0, set()))
    geodes = defaultdict(int)

    while queue:
        current, t, skipped = queue.popleft()
        prior_best = geodes[t]

        if current.geode >= prior_best:
            geodes[t] = current.geode
            if t == minutes:
                continue
            
            can_build = current.buildable(recipe)
            for robot in can_build:
                if robot == 'none': # Stick no-builds at the end of the queue
                    queue.append((current.build(recipe, robot), t + 1, can_build))
                elif robot in skipped:
                    continue
                else:
                    queue.appendleft((current.build(recipe, robot), t + 1, set()))

    return geodes[minutes]

if __name__=="__main__":
    with open('../d/19') as f:
        data = f.read().splitlines()

    numbers = [
        [int(n) for n in re.findall(r'(-?\d+)', row)]
        for row in data
    ]

    recipes = [
        Recipe(
            ore=r[1],
            clay=r[2],
            obsidian=(r[3], r[4]),
            geode=(r[5], r[6])
        )
        for r in numbers
    ]

    total = 0
    for i, r in enumerate(recipes):
        total+=(i+1)*search(recipes[i], 24)

    print(total)
    print(prod(search(r, 32) for r in recipes[:3]))