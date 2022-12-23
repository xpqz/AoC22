from sympy import sympify, Symbol
from sympy.solvers import solve
import re
import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '==': operator.eq,
}

REV = {
    operator.add: '+',
    operator.sub: '-',
    operator.mul: '*',
    operator.truediv: '/',
    operator.eq: '==',
}

class Constant:
    def __init__(self, value):
        self.value = value

class Node:
    def __init__(self, left, op, right):
        self.value = None
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        o = REV[self.op]
        if o in '+-':
            return f'({self.left}{REV[self.op]}{self.right})'
        return f'{self.left}{REV[self.op]}{self.right}'

    def visit(self):
        if self.left == 'humn' or self.right == 'humn':
            return self
        return self.op(self.left, self.right)

    def execute(self, val):
        if self.left == 'humn' or isinstance(self.left, (int, float)):
            left = val
        else:
            left = self.left.execute(val)
        if self.right == 'humn' or isinstance(self.right, (int, float)):
            right = val
        else:
            right = self.right.execute(val)

        return self.op(left, right)

def parse(symtab, top):
    root = symtab[top]

    def _parse(node):
        if isinstance(node, Constant):
            return node.value
        else:
            node.left = _parse(symtab[node.left])
            node.right = _parse(symtab[node.right])
            if (not isinstance(node.left, Node)) and (not isinstance(node.right, Node)):
                return node.visit()
            return node
    return _parse(root)

def tokenise(data, part2=False):
    symtab = {}
    for i, row in enumerate(data):
        if part2 and row.startswith('humn'):
            symtab['humn'] = Constant('humn')
        elif m := re.match(r'^(.*): (-?\d+)$', row):
            symtab[m.group(1)] = Constant(int(m.group(2)))
        elif m := re.match(r'^(.*): (.+) (.) (.+)$', row):
            name, f1, op, f2 = [m.group(i) for i in range(1, 5)]
            if part2 and name == 'root':
                op = '=='
            symtab[name] = Node(f1, OPS[op], f2)
    return symtab

if __name__=="__main__":
    with open('/Users/stefan/work/AoC22/d/21') as f:
        data = f.read().splitlines()

    symtab = tokenise(data, part2=False)
    print('Part1:', sympify(str(parse(symtab, 'root'))))
    
    symtab = tokenise(data, part2=True)    
    ast = str(parse(symtab, 'root'))
    left, right = ast.split('==')
    expr = sympify(f'{left}-{right}')
    humn = Symbol('humn')
    print('Part2:', int(solve(expr, humn)[0]))
