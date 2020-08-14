#!/usr/bin/env python3
w, h, x, y = map(int, input().split())
print(w*h/2, int(x+x-w == y+y-h == 0))