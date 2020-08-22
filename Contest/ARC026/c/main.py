#!/usr/bin/env python3
class SegmentTree(object):
    __slots__ = ["elem_size", "tree", "default", "op", "real_size"]

    def __init__(self, a, default = float("inf"), op: "func" = min):
        self.default = default
        self.op = op
        if hasattr(a, "__iter__"):
            self.real_size = len(a)
            self.elem_size = elem_size = 1 << (self.real_size-1).bit_length()
            self.tree = tree = [default] * (elem_size * 2)
            tree[elem_size:elem_size + self.real_size] = a
            for i in range(elem_size - 1, 0, -1):
                tree[i] = op(tree[i << 1], tree[(i << 1) + 1])
        elif isinstance(a, int):
            self.real_size = a
            self.elem_size = elem_size = 1 << (self.real_size-1).bit_length()
            self.tree = [default] * (elem_size * 2)
        else:
            raise TypeError

    def get_value(self, x: int, y: int) -> int:   # [x, y)
        l, r = x + self.elem_size, y + self.elem_size
        tree, result, op = self.tree, self.default, self.op
        while l < r:
            if l & 1:
                result = op(tree[l], result)
                l += 1
            if r & 1:
                r -= 1
                result = op(tree[r], result)
            l, r = l >> 1, r >> 1
        return result

    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        op, tree = self.op, self.tree
        tree[k] = value
        while k > 1:
            k >>= 1
            tree[k] = op(tree[k << 1], tree[(k << 1) + 1])

    def get_one_value(self, i):
        return self.tree[i + self.elem_size]

    def debug(self):
        print(self.tree[self.elem_size : self.elem_size + self.real_size])

(N, L), *d = [[*map(int, o.split())] for o in open(0)]
d.sort()
dp = SegmentTree(L + 1) # dp[i] := 距離 i まで照らすのに使う最小コスト
for i, (l, r, c) in d:
    dp[r] = min(dp[r], )