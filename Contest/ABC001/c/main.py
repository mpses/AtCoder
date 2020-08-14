#!/usr/bin/env python3
Deg, Dis = map(int, input().split())

Dirl = "N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW N".split()
Pow = [2,15,33,54,79,107,138,171,207,244,284,326]

Dir = Dirl[(Deg*10 + 1125) // 2250] if Dis>14 else "C"
W = sum(Dis/6 > p+0.4 for p in Pow)
print(Dir, W)