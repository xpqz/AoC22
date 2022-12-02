with open('/Users/stefan/work/AoC22/d/2') as f:
    data = f.read().splitlines()

num = [(ord(l) - ord('A'), ord(r) - ord('X'))
       for l, r in (line.split() for line in data)]

p1 = p2 = 0
s1 = [4, 8, 3, 0, 1, 5, 9, 0, 7, 2, 6]
s2 = [3, 4, 8, 0, 1, 5, 9, 0, 2, 6, 7]

for x, y in num:
    j = x * 4 + y
    p1 += s1[j]
    p2 += s2[j]

print(p1, p2)
