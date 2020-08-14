#!/usr/bin/env python3
# Python shortest 134 byte (normally:194) 
a, b, c = map(int, input().split())
o = 0
if a == b == c:print(a%2-1);exit() 
while 1-any([a%2, b%2, c%2]):
    a, b, c = (b+c)//2, (c+a)//2, (a+b)//2
    o += 1
print(o) 