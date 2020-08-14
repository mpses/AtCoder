#!/usr/bin/env python3
from collections import deque
d = deque(range(1, 10))
Dequeue = lambda: d.popleft()
Enqueue = lambda x: d.append(x)

for _ in range(int(input())):
    x = Dequeue()
    m = x%10
    if m != 0: Enqueue(10*x + m-1)
    if True  : Enqueue(10*x +  m )
    if m != 9: Enqueue(10*x + m+1)
print(x)