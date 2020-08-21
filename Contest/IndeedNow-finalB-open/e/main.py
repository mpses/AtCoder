#!/usr/bin/env python3
class Bit:
    # Binary Indexed Tree
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i + 1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # Σ [0, i)
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key + 1) - self.sum(key)

    def __setitem__(self, key, value):
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

def compress(a: list) -> list:
    d = {v : i for i, v in enumerate(sorted(set(a)))}
    return [d[i] for i in a]

# mergecount 改造
def mergecount_(A: list):
    bit = Bit(n + 1)
    cnt = 0
    for i, (h, d) in enumerate(zip(A, compress(A))):
        cnt += h * (i - bit.sum(d + 1))
        bit.add(d, 1)
    return cnt

n, *h = map(int, open(0).read().split())
print(-1 if len(set(h)) != n else mergecount_(h))