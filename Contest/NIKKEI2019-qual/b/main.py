#!/usr/bin/env python3
_, *a = open(0)
print(sum(len(set(i))-1 for i in zip(*a)))
