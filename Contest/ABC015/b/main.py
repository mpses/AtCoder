#!/usr/bin/env python3
s = [int(i) for i in open(0).read().split()[1:] if int(i)]
print(0--sum(s)//len(s))