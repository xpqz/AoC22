def visible(d):
    viz = [[0 for c in range(len(d[0]))] for r in range(len(d))]

    # Look left → right along rows
    for y, row in enumerate(d):
        highest = row[0]
        for x in range(1, len(row)):
            if row[x] > highest:
                highest = row[x]
                viz[y][x] = 1

    # Look right → left along rows
    for y, row in enumerate(d):
        highest = row[-1]
        for x in range(len(row) - 2, -1, -1):
            if row[x] > highest:
                highest = row[x]
                viz[y][x] = 1

    # Look top → bottom along cols
    for x in range(len(d[0])):
        highest = d[0][x]
        for y in range(1, len(d)):
            if d[y][x] > highest:
                highest = d[y][x]
                viz[y][x] = 1

    # Look bottom → top along cols
    for x in range(len(d[0])):
        highest = d[-1][x]
        for y in range(len(d) - 2, -1, -1):
            if d[y][x] > highest:
                highest = d[y][x]
                viz[y][x] = 1

    # Set all edges
    viz[0]  = [1 for _ in range(len(viz[0]))]
    viz[-1] = [1 for _ in range(len(viz[-1]))]
    for r in viz:  # Set all edges
        r[0] = r[-1] = 1

    return viz


def scenic(data):
    best = 0    
    for i, row in enumerate(data):
        for j, elem in enumerate(row):
            t = r = b = l = 0

            # Top
            for y in reversed(range(0, i)):
                t += 1
                if data[y][j] >= elem:
                    break

            # Right
            for x in range(j + 1, len(row)):
                r += 1
                if data[i][x] >= elem:
                    break

            # Bottom
            for y in range(i + 1, len(data)):
                b += 1
                if data[y][j] >= elem:
                    break

            # Left
            for x in reversed(range(0, j)):
                l += 1
                if data[i][x] >= elem:
                    break

            score = t * r * b * l

            if score > best:
                best = score 

    return best

if __name__ == '__main__':
    with open('/Users/stefan/work/AoC22/d/8') as f:
        data = [
            list(map(int, l)) for l in (list(r) for r in f.read().splitlines())
        ]

    a = visible(data)
    print(sum(sum(a, [])))

    print(scenic(data))
