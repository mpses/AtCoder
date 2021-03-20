#!/usr/bin/env python3
a, b, c = map(int, input().split())
a %= 10
if a in {0, 1, 5, 6}:
    print(a)
elif a == 4:
    # b^c ≡ b (mod 2)
    print([4, 6][b % 2 - 1])
elif a == 9:
    # b^c ≡ b (mod 2)
    print([9, 1][b % 2 - 1])
else:
    seq = {2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6]}[a]
    ## mod 4
    # b ≡ 0 -> b^c ≡ 0
    # b ≡ 1 -> b^c ≡ 1
    # b ≡ 2 -> b^c ≡ 0 (c > 1), 2 (c = 1)
    # b ≡ 3 ≡ -1 -> b^c ≡ -1 ≡ 3 (c : odd), 1 (c : even)
    b %= 4
    if b <= 1:
        print(seq[b - 1])
    if b == 2:
        print(seq[2 - 1 if c == 1 else 0 - 1])
    if b == 3:
        if c % 2:
            print(seq[3 - 1])
        else:
            print(seq[1 - 1])