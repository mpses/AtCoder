#!/usr/bin/env python3
n, m, *q = map(int, open(0).read().split())

##### bisect 自己実装 #####
def getitem(l: "list or func", i: int):
    return l[i] if type(l) is list else l(i)

def bisect(ng, ok, func):
    while abs(ng - ok) > 1:
        mid = (ok + ng) >> 1  ## // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def bisect_left(func: "list or func", x, ng = -1, ok = None):
    if ok is None: ok = len(func)
    return bisect(ng, ok, lambda i: getitem(func, i) >= x)

def bisect_right(func: "list or func", x, ng = -1, ok = None):
    if ok is None: ok = len(func)
    return bisect(ng, ok, lambda i: getitem(func, i) > x)

# PartiallyPersistentUnionFind
class PPUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.time = [10 ** 5 + 1] * n
        r = [None] * n
        self.number_time = [[0] for _ in r]
        self.number_dots = [[1] for _ in r]

    def find(self, x, t):
        while self.time[x] <= t:
            x = self.parents[x]
        return x
        ########### or ###########
        # if self.time[x] > t:
        #    return x
        # return self.find(self.parents[x], t)

    def union(self, x, y, t):
        x = self.find(x, t)
        y = self.find(y, t)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.number_time[x] += [t]
        self.number_dots[x] += [-self.parents[x]]
        self.time[y] = t

    def size(self, x, t):
        x = self.find(x, t)
        return self.number_dots[x][bisect_right(self.number_time[x], t) - 1]
        
    def same(self, x, y, t):
        return self.find(x, t) == self.find(y, t)

UF = PPUnionFind(n + 1)
for t, (a, b) in enumerate(zip(*[iter(q[:m*2])]*2)):
    UF.union(a, b, t + 1)

def check(x, y, t):
    return UF.size(x, t) + UF.size(y, t) * (not UF.same(x, y, t))

for x, y, z in zip(*[iter(q[m*2 + 1:])]*3):
    judge = lambda t: check(x, y, t)
    print(bisect_left(judge, z, 0, m))