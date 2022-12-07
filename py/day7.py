import re


def cd(f, path):
    cwd = f
    for p in path:
        cwd = cwd[p]
    return cwd


def buildfs(data):
    fs = {'/': {}}
    path = ['/']
    cwd = fs
    for row in data:
        if n := re.findall(r'^\$\s+cd\s+(.+)$', row):
            if n[0] == '..':
                path.pop()
                cwd = cd(fs, path)
                continue
            if n[0] == '/':
                path = ['/']
                cwd = fs['/']
                continue
            path.append(n[0])
            cwd = cd(fs, path)
        elif dir := re.findall(r'^dir\s+(.+)$', row):
            cwd[dir[0]] = {}
        elif m := re.match(r'^(\d+)\s+(.+)', row):
            cwd[m.group(2)] = int(m.group(1))  # type: ignore

    return fs


def dirsize(fs, acc, path=['/']):
    cwd = cd(fs, path)
    ls = cwd.keys()
    size = 0
    for name in ls:
        if type(cwd[name]) == dict:
            size += dirsize(fs, acc, path + [name])
        else:
            size += cwd[name]
    acc.append(size)
    return size


if __name__ == '__main__':
    with open('/Users/stefan/work/AoC22/d/test') as f:
        data = f.read().splitlines()

    fs = buildfs(data)
    sizes = []
    dirsize(fs, sizes)
    print(sizes)
    print(sum(s for s in sizes if s < 100_000))
    print(min(a for a in sizes if a >= 30_000_000 - (70_000_000 - sizes[-1])))
