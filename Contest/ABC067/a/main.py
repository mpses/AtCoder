#!/usr/bin/env python3
l = list(map(int, input().split()))
print(["P","Imp"][all(map(lambda x: min(x%3, 1), [sum(l)]+l))]+"ossible")