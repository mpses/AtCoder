#!/usr/bin/env python3
from time import perf_counter
from math import exp
from random import random, getrandbits
from copy import deepcopy
start = perf_counter()
INF = float("inf")

obj = open(0)
(n,), *data = [[*map(int, o.split())] for o in obj]

ans = []

def ind_score(x, y, r, a, b, c, d):
    if not point_in(a, b, c, d, x, y):
        return 0
    area = (c - a) * (d - b)
    return 1 - (1 - min(r, area) / max(r, area)) ** 2

def main():
    for _ in ans:
        print(*_)
    return

def debug(ind = True, write = False, k = n):
    from sys import argv
    filewrite = argv[-1] != "ONLINE_JUDGE"
    amount = score()
    J = judge()
    print(f"{J}, score : {amount} pt")
    if J != "AC":
        raise RuntimeError
    if not ind:
        return
    for point, i in sorted(nowkey())[:k]:
        print(i, point)
    s = int(start)
    if write and filewrite and amount < 730000000:
        indata, outdata = ['\n'.join(" ".join(map(str, i)) for i in p) for p in [data, ans]]
        with open(f"debug/{s}.txt", mode = "x") as f:
            f.write(f"in: \n{n}\n{indata}\nout: \n{outdata}")
    return

def judge():
    from itertools import combinations
    for i, j in combinations(ans, 2):
        if has_intersect(*i, *j):
            return f"WA: {i} {j}"
    else:
        return "AC"

def CHECK_ERROR(message = 0):
    J = judge()
    if J != "AC":
        raise RuntimeError(f"{J} : {message}")
    return

def score(key = None):
    if key:
        return round((10 ** 9) * sum(point for point, _ in key) / n)
    return round((10 ** 9) * sum(ind_score(x, y, r, a, b, c, d) for (x, y, r), (a, b, c, d) in zip(data, ans)) / n)

def has_intersect(a, b, c, d, s, t, u, v):
    return max(a, s) < min(c, u) and max(b, t) < min(d, v)

def point_in(a, b, c, d, x, y):
    return a <= x < c and b <= y < d

def find(a, b, c, d, A = -1, B = -1, C = -1, D = -1):
    return any(has_intersect(a, b, c, d, s, t, u, v) for s, t, u, v in ans if (A, B, C, D) != (s, t, u, v))

def findx(a, b, c, d, A = -1, B = -1, C = -1, D = -1):
    res = []
    for e, (s, t, u, v) in enumerate(ans):
        if (A, B, C, D) == (s, t, u, v):
            continue
        if has_intersect(a, b, c, d, s, t, u, v):
            res += (s, t, u, v, e),
    return res

def point(a, b, c, d, x, y):
    return any(point_in(a, b, c, d, x1, y1) for x1, y1, _ in data if (x, y) != (x1, y1))

def ng(a, b, c, d, x, y, A = -1, B = -1, C = -1, D = -1):
    return find(a, b, c, d, A, B, C, D) or point(a, b, c, d, x, y)

def ok(*args, **kwargs):
    return not ng(*args, *kwargs)

def nowkey():
    return [(ind_score(x, y, r, a, b, c, d), e) for e, ((x, y, r), (a, b, c, d)) in enumerate(zip(data, ans))]

def init(x, y, r, i = None):
    k = round(r ** .5)
    a, b, c, d = A, B, C, D = x, y, min(x + k, 10000), min(y + round(r / k), 10000)
    if i:
        A, B, C, D = ans[i]
    flag = True
    z = 0
    while ng(a, b, c, d, x, y, A, B, C, D):
        c, d = max(a + 1, c - 25), max(b + 1, d - 25)
        z += 1
        if z > 800:
            flag = False
            c, d = a + 1, b + 1
            break
    while flag and ok(max(0, a - 25), max(0, b - 25), c, d, x, y, A, B, C, D) and z:
        a, b = max(0, a - 25), max(0, b - 25)
        z -= 1
    return [a, b, c, d]
"""
def init(x, y, r, i = None):
    a, b, c, d = x, y, x + 1, y + 1
    A = B = C = D = -1
    if i:
        A, B, C, D = ans[i]
    z = 0
    while (c - a) * (d - b) < r and z < 500:
        if ok(max(0, a - 25), b, c, d, x, y, A, B, C, D):
            a = max(0, a - 25)
        if ok(a, max(0, b - 25), c, d, x, y, A, B, C, D):
            b = max(0, b - 25)
        if ok(a, b, min(c + 25, 10000), d, x, y, A, B, C, D):
            c = min(c + 25, 10000)
        if ok(a, b, c, min(d + 25, 10000), x, y, A, B, C, D):
            d = min(d + 25, 10000)
        z += 1

    return [a, b, c, d]
"""
def Greedy(limit = INF, cand = None):
    key = nowkey()
    key.sort()
    for point, i in key:
        if cand and i not in cand:
            continue
        if perf_counter() - start > limit:
            return
        if point > 0.995:
            return
        a, b, c, d = ans[i]
        x, y, r = data[i]
        p_score = 0
        for _ in range(500):
            new_score = ind_score(x, y, r, a, b, c, d)
            if p_score > new_score:
                break
            if new_score > 0.995:
                break
            A, B, C, D = a, b, c, d
            h, w = getrandbits(1), getrandbits(1)
            if h and a and not(find(max(0, a - 5), b, c, d, A, B, C, D)):
                a = max(a - 5, 0)
            if w and b and not(find(a, max(0, b - 5), c, d, A, B, C, D)):
                b = max(b - 5, 0)
            if h and c < 10000 and not(find(a, b, min(c + 5, 10000), d, A, B, C, D)):
                c = min(c + 5, 10000)
            if w and d < 10000 and not(find(a, b, c, min(d + 5, 10000), A, B, C, D)):
                d = min(d + 5, 10000)
            ans[i] = [a, b, c, d]
            p_score = new_score
    return

def Annealing(limit):
    global ans, archive
    start_ = perf_counter()
    timelimit = limit - (start_ - start)
    t0, t1 = 14e6 / n, 5e6 / n

    def temperature():
        return t0 + (t1 - t0) * (start_ - perf_counter()) / timelimit

    def prob(subscore): 
        subscore *= 10 ** 9 / n
        return exp(subscore / temperature())

    key = nowkey()
    for point, i in sorted(key):
        if perf_counter() - start > limit:
            return
        if point > 0.8:
            return
        for _ in range(15):
            a, b, c, d = A, B, C, D = ans[i]
            x, y, r = data[i]
            co_score = ind_score(x, y, r, a, b, c, d)
            k = findx(a - 10, b, c, d, A, B, C, D) if a >= 10 else None
            if k:
                if all(data[e][0] < u - 10 for s, t, u, v, e in k):
                    subscorep = 0
                    archive = deepcopy(ans)
                    for s, t, u, v, e in k:
                        S, T, U, V = s, t, u, v
                        if s and not find(max(0, s - 10), t, u, v, S, T, U, V):
                            s = max(0, s - 10)
                        u -= 10
                        p, z = data[e][2] // (u - s), 15;
                        while p > (v - t) and z:
                            if t and not find(s, max(0, t - 5), u, v):
                                t = max(0, t - 5)
                            if v < 10000 and not find(s, t, u, min(v + 5, 10000)):
                                v = min(v + 5, 10000)
                            z -= 1
                        ans[e] = s, t, u, v
                        subscorep += ind_score(*data[e], s, t, u, v) - key[e][0]
                    af_score = ind_score(x, y, r, a - 10, b, c, d)
                    subscoreq = af_score - co_score
                    co_score = af_score
                    if random() <= prob(subscorep + subscoreq):
                        a -= 10
                    else:
                        ans = deepcopy(archive)
                            
            #CHECK_ERROR()
            k = findx(a, b - 10, c, d, A, B, C, D) if b >= 10 else None
            if k:
                if all(data[e][1] < v - 10 for s, t, u, v, e in k):
                    subscorep = 0
                    archive = deepcopy(ans)
                    for s, t, u, v, e in k:
                        S, T, U, V, area = s, t, u, v, (v - t) * (u - s)
                        if t and not find(s, max(0, t - 10), u, v, S, T, U, V):
                            t = max(0, t - 10)
                        v -= 10
                        p = data[e][2] // (v - t)
                        z = 15
                        while p > (u - s) and z:
                            if s and not find(max(0, s - 5), t, u, v):
                                s = max(0, s - 5)
                            if u < 10000 and not find(s, t, min(u + 5, 10000), v):
                                u = min(u + 5, 10000)
                            z -= 1
                        ans[e] = s, t, u, v
                        subscorep += ind_score(*data[e], s, t, u, v) - key[e][0]
                    af_score = ind_score(x, y, r, a, b - 10, c, d)
                    subscoreq = af_score - co_score
                    co_score = af_score
                    if random() <= prob(subscorep + subscoreq):
                        b -= 10
                    else:
                        ans = deepcopy(archive)
                        
            #CHECK_ERROR()
            k = findx(a, b, c + 10, d, A, B, C, D) if c + 10 <= 10000 else None
            if k:
                if all(s + 10 <= data[e][0] for s, t, u, v, e in k):
                    subscorep = 0
                    archive = deepcopy(ans)
                    for s, t, u, v, e in k:
                        S, T, U, V, area = s, t, u, v, (v - t) * (u - s)
                        if u < 10000 and not find(s, t, min(u + 10, 10000), v):
                            u = min(u + 10, 10000)
                        s += 10
                        p = data[e][2] // (u - s)
                        z = 15
                        while p > (v - t) and z:
                            if t and not find(s, max(0, t - 5), u, v, S, T, U, V):
                                t = max(0, t - 5)
                            if v < 10000 and not find(s, t, u, min(v + 5, 10000), S, T, U, V):
                                v = min(v + 5, 10000)
                            z -= 1
                        ans[e] = s, t, u, v
                        subscorep += ind_score(*data[e], s, t, u, v) - key[e][0]
                    af_score = ind_score(x, y, r, a, b, c + 10, d)
                    subscoreq = af_score - co_score
                    co_score = af_score
                    if random() <= prob(subscorep + subscoreq):
                        c += 10
                    else:
                        ans = deepcopy(archive)
                        
            ##CHECK_ERROR()
            k = findx(a, b, c, d + 10, A, B, C, D) if d + 10 <= 10000 else None
            if k:
                if all(t + 10 <= data[e][1] for s, t, u, v, e in k):
                    subscorep = 0
                    archive = deepcopy(ans)
                    for s, t, u, v, e in k:
                        S, T, U, V, area = s, t, u, v, (v - t) * (u - s)
                        if v < 10000 and not find(s, t, u, min(v + 10, 10000), S, T, U, V):
                            v = min(v + 10, 10000)
                        t += 10
                        p = data[e][2] // (v - t)
                        z = 15
                        while p > (u - s) and z:
                            if s and not find(max(0, s - 5), t, u, v, S, T, U, V):
                                s = max(0, s - 5)
                            if u < 10000 and not find(s, t, min(u + 5, 10000), v, S, T, U, V):
                                u = min(u + 5, 10000)
                            z -= 1
                        ans[e] = s, t, u, v
                        subscorep += ind_score(*data[e], s, t, u, v) - key[e][0]
                    af_score = ind_score(x, y, r, a, b, c, d + 10)
                    subscoreq = af_score - co_score
                    co_score = af_score
                    if random() <= prob(subscorep + subscoreq):
                        d += 10
                    else:
                        ans = deepcopy(archive)
            #CHECK_ERROR()
            ans[i] = a, b, c, d
    return

def reset():
    global ans
    pre_score = score()
    archive = deepcopy(ans)
    key = nowkey()
    key.sort()
    for point, i in key:
        if point > 0.4:
            return
        a, b, c, d = ans[i]
        res = []
        for *_, e in findx(a - 10, b, c, d, a, b, c, d) + findx(a, b - 10, c, d, a, b, c, d) + \
                     findx(a, b, c + 10, d, a, b, c, d) + findx(a, b, c, d + 10, a, b, c, d):
            x, y, r = data[e]
            res += e,
            ans[e] = init(x, y, r, e)
        Greedy(cand = res)
    if score() + random() * 10 ** 6 <= pre_score:
        ans = deepcopy(archive)
    return


for x, y, r in data:
    ans += init(x, y, r),
#CHECK_ERROR()
Greedy(2)
for i in range(1, 8):
    Greedy(2 + i / 3)
    Annealing(2.13 + i / 3)
    if i < 7:
        reset()
    #debug(k = 5)
    #print("\n")

#main()
debug(ind = 0)
#judge()