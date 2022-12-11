import math
import re

class Monkey:
    mod_fact = 1
    def __init__(self, mid, items, oper, tst, t, f):
        self.mid = mid
        self.oper = oper
        self.test = tst
        self.true_target = t
        self.false_target = f
        self.icount = 0

        self.items = [0 for _ in range(36)]
        self.items[:len(items)] = items
        self.ptr = len(items)

    @classmethod 
    def make_monkey(cls, group):
        mid = int(re.findall(r'\d+', group[0])[0])
        items = [int(i) for i in re.findall(r'\d+', group[1])]
        oper = re.findall(r'old\s+(.)\s+(\d+)', group[2])
        tst = int(re.findall(r'\d+', group[3])[0])
        tm = int(re.findall(r'\d+', group[4])[0])
        fm = int(re.findall(r'\d+', group[5])[0])
        Monkey.mod_fact *= tst

        if oper == []:
            o = lambda x: x*x
        elif oper[0][0] == '*':
            o = lambda x: x*int(oper[0][1])
        else:
            o = lambda x: x+int(oper[0][1])

        return Monkey(mid, items, o, lambda x: 0==x%tst, tm, fm)

    def add_item(self, worry_level):
        self.items[self.ptr] = worry_level
        self.ptr += 1

    def do(self, f=1):
        if self.ptr == 0:
            return []
        worry_levels = [
            (self.oper(worry_level)//f) % Monkey.mod_fact
            for worry_level in self.items[:self.ptr]
        ]
        self.icount += len(worry_levels)
        throw_to = [
            [self.false_target, self.true_target][self.test(new_level)] 
            for new_level in worry_levels[:self.ptr]
        ]

        self.ptr = 0

        return zip(throw_to, worry_levels)

def init_monkeys(data):
    group = []
    monkeys = []
    for line in data:
        if line == '':
            monkeys.append(Monkey.make_monkey(group))
            group = []
        else:
            group.append(line)
    monkeys.append(Monkey.make_monkey(group))
    return monkeys

def simulate(monkeys, cutoff, f=1):
    round = 1
    while True:
        for m in monkeys:
            things = m.do(f)
            for mid, wl in things:
                monkeys[mid].add_item(wl)
        round += 1
        if round > cutoff:
            break

    return math.prod(sorted(m.icount for m in monkeys)[-2:])

if __name__ == '__main__':
    with open('/Users/stefan/work/AoC22/d/11') as f:
        data = f.read().splitlines()

    print(simulate(init_monkeys(data), 20, 3))
    print(simulate(init_monkeys(data), 10_000, 1))
