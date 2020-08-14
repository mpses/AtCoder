#!/usr/bin/env python3
c = [[0] * 10 for _ in [0] * 10]
for i in range(1, int(input()) + 1):
    c[int(str(i)[0])][int(str(i)[-1])] += 1

print(sum(c[i][j] * c[j][i] for i in range(10) for j in range(10)))