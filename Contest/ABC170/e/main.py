#!/usr/bin/env python3
import sys
input = sys.stdin.readline

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)
        
    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.left.value - 1 if nd_.left else -1,
                    nd_.right.value - 1 if nd_.right else -1)
        
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])
        
    def append(self, v):
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p) // 2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p) // 2)
                        break
    
    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd
    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd
    
    def find_l(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.value < v: prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1
    
    def find_r(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.value > v: prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1
    
    def find_max(self):
        return self.find_l((1 << self.N)-1)
    def find_min(self):
        return self.find_r(-1)
    
    def delete(self, v, nd = None, prev = None):
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return 0
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return 0
        if (not nd.left) and (not nd.right):
            if nd.value < prev.value:
                prev.left = None
            else:
                prev.right = None
        elif not nd.left:
            if nd.value < prev.value:
                prev.left = nd.right
            else:
                prev.right = nd.right
        elif not nd.right:
            if nd.value < prev.value:
                prev.left = nd.left
            else:
                prev.right = nd.left
        else:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)
    
    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

n, q = map(int, input().split())
m = 200200
BT = [BalancingTree(48) for _ in [None] * m]
BT_all = BalancingTree(48)
# [30 : レート, 18 : ID]

A = [0] * N
X = [0] * N
for i in range(n):
    a, b = map(int, input().split())
    b -= 1
    A[i] = (a << 18) + i
    X[i] = b
    BT[b].append(A[i])

for i in range(M):
    BT_all.append(BT[i].find_max())

for _ in [None] * q:
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    b = X[c]
    a = A[c]
    X[c] = d
    BT_all.delete(BT[d].find_max())
    BT_all.delete(BT[b].find_max())
    
    BT[d].append(a)
    BT[b].delete(a)
    
    BT_all.append(BT[d].find_max())
    BT_all.append(BT[b].find_max())
    
    print(BT_all.find_min() >> 18)
