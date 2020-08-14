#!/usr/bin/env python3
s = "".join
*i, l = input()
for t in map(lambda x: format(x, "03b").translate(str.maketrans("01","-+")), range(8)):
    h = s(map(s, zip(i, t))) + l
    if eval(h) == 7:
        print(h+"=7")
        break