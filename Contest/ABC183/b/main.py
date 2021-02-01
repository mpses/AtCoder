#!/usr/bin/env python3
sx, sy, gx, gy = map(int, input().split())
print(sy * (gx - sx) / (gy + sy) + sx)