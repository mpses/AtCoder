#!/usr/bin/env python3
from collections import deque

def 周辺埋め(grid, W):
    U = "#" * (W + 2)
    return [list(U)] + [["#"] + list(g) + ["#"] for g in grid] + [list(U)]

H, W, *grid = open(0).read().split()
H, W = map(int, (H, W))

C = sum(g.count(".") for g in grid)

grid = 周辺埋め(grid, W)

grid[1][1] = "!"
grid[H][W] = "G"

D = [(0,1), (1,0), (0,-1), (-1, 0)]

def bfs():
    que = deque()
    que.append((1, 1, 0))

    while que:
        cy, cx, c = que.popleft()

        for my, mx in D:
            nx = cx + mx
            ny = cy + my

            if grid[ny][nx] == ".":
                # 未探索
                que.append((ny, nx, c + 1))
                grid[ny][nx] = "!"  # 探索済み
            
            elif grid[ny][nx] == "G":  # ゴール
                return C - (c + 2)

    return -1

print(bfs())