#!/usr/bin/env python3
class V:
    def __init__(self, f, v = None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def __call__(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n) 

def rotate():
    global n, m, c
    n, m = m, n
    c = [[*s][::-1] for s in zip(*c)]


def trycut(size, y, x):
    res = 0
    for i in range(size):
        row = c[y+i][x:x+i+1]
        if "X" in row: return 0
        res += sum(int(c) for c in row)
    return res

def evaluate():
    res = V(max)
    for size in range(1, min(n, m) + 1):
        for y in range(n - size + 1):
            for x in range(m - size + 1):
                res(trycut(size, y, x))
    return res.v

n, m = map(int, input().split())
c = [[*input()] for _ in [None] * n]
ans = V(max)

for i in range(4):
    ans(evaluate())
    rotate()
print(ans.v)