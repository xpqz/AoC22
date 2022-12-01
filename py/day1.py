def data(n):
    with open(n) as f:
        return f.read().splitlines()
        
groups = []
elf = []
for s in data('/Users/stefan/work/AoC22/d/1'):
    if s=='':
        groups.append(sum(elf))
        elf = []
    else:
        elf.append(int(s))
        
top3 = sorted(groups)[-3:]

print(f'Part1: {top3[-1]}')
print(f'Part2: {sum(top3)}')