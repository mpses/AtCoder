#!/usr/bin/env python3.4.3
# AGC 020 A
_, a, b = map(int, input().split())
print(["Alice", "Borys"][(b-a) % 2])