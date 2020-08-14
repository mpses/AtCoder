#!/usr/bin/env python3
H, W = map(int,input().split())
s = [input() for _ in range(H)]
for h in range(H):
    l = ""
    for w in range(W):
        l += "#" if s[h][w] == "#" else str(
                    sum(
                        [t[max(0, w - 1) : min(W, w + 2)]
                            .count("#") for t in 
                         s[max(0, h - 1) : min(H, h + 2)]
                        ]
                        ))
    print(l)