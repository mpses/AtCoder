#!/usr/bin/env python3
_, w, *s = open(0).read().split()
t, k = "#"*-~int(w), "#\n#"
print(t, *s, sep=k, end=k+t)