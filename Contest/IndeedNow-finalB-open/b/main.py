from itertools import*
(n,), *d = [[*map(int, o.split())] for o in open(0)]
S, T = zip(*d)
a = [0] * -~max(T)
for s in S:
    a[s] += 1
*a, = accumulate(a)
for s, t in d:
    print(a[t] - a[s])