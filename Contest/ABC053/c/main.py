#!/usr/bin/env python3
p, q = divmod(int(input()), 11)
print(p*2 + (q and [1, 2][q > 6]))