"""
Heavily inspired by a solution on Reddit megathread
"""
def zi(data):
    for i in range(len(data)):
        if data[i][1] == 0:
            return i

def mix(data, mix_count=1, multiplier=1):
    size = len(data)
    data = [(i, n * multiplier) for i, n in data]
    for _ in range(mix_count):
        for i in range(size):
            for j in range(size):
                if data[j][0] == i:
                    num = data.pop(j)
                    if num[1] == -j:
                        data.append(num)
                    else:
                        data.insert((j + num[1]) % (size-1), num)
                    break

    return sum(data[(zi(data) + i) % len(data)][1] for i in range(1000, 4000, 1000))

if __name__=="__main__":
    with open(r"../d/20") as f:
        data = list(enumerate(map(int, f.read().splitlines())))

    print("Part 1:", mix(data))
    print("Part 2:", mix(data, 10, 811589153))