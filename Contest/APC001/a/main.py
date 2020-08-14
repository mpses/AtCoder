#!/usr/bin/env python3
x, y = map(int,input().split())
print([x, -1][x%y==0])acc