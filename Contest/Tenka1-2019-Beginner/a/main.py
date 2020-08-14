#!/usr/bin/env python3
a, b, c = map(int, input().split())
print(["No","Yes"][a<c<b or b<c<a])