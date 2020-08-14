#!/usr/bin/env python3
def I(): return list(input().upper())
A, B, C = I(), I(), I()
t = "A"
while True:
    try:
        t = eval("%s.pop(0)" % t)
    except IndexError:
        print(t)
        exit()