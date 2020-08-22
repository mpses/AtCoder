#!/usr/bin/env python3
def v(n):
    d = set()
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            d |= {i, n//i}
    return sum(d - {n})

n = int(input())
s = v(n)
print("Deficient" if s<n else "Abundant" if s>n else "Perfect")