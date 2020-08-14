#!/usr/bin/env python3
w, h = map(int, input().split())
print(["16:9","4:3"][h/w == 0.75])