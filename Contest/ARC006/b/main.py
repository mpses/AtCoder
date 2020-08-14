#!/usr/bin/env python3
p, *t, a = open(0)
j = a.index("o")
for i in range(int(p.split()[1])):
    s = " " + t[-i-1]
    j += [-2, 9, 2, 0][s[j:j+3].find("-")]
print(j // 2 + 1)