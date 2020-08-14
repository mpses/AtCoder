#!/usr/bin/env python3
print(["YES", "NO"][set(map(int, input().split())) & set(map(int, input().split())) == set()])