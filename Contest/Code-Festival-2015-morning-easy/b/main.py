#!/usr/bin/env python3
def main():
    n = int(input())
    s = input()
    if n % 2:
        return -1
    return sum(u != v for u, v in zip(s[:n // 2], s[n // 2:]))
print(main())