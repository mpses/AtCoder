#!/usr/bin/env python3
sx, sy, tx, ty = map(int, input().split())
x, y = tx - sx, ty - sy
print("R"*x + "U"*-~y + "L"*-~x + "D"*-~y + "R" + "U"*y + "R"*-~x + "D"*-~y + "L"*-~x + "U")