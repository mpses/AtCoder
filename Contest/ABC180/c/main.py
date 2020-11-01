#!/usr/bin/env python3
def div(n) -> list:
    if n == 0:
        return [0]
    i = 1
    table = set()
    while i * i <= n:
        if n % i == 0:
            table |= {i, n // i}
        i += 1
    return sorted(table)
for i in div(int(input())):
    print(i)