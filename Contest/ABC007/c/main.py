#!/usr/bin/env python3
from collections import deque

def 周辺埋め(grid, H):
    U = "#" * (H + 2)
    return [list(U)] + [["#"] + list(g) + ["#"] for g in grid] + [list(U)]

H, W, sy, sx, gy, gx, *grid = open(0).read().split()
H, W, sy, sx, gy, gx = map(int, (H, W, sy, sx, gy, gx))

grid = 周辺埋め(grid, W)

grid[sy][sx] = "!"
grid[gy][gx] = "G"

D = [(0,1), (1,0), (0,-1), (-1, 0)]

def bfs():
    que = deque()
    que.append((sy, sx, 0))

    while que:
        cy, cx, c = que.popleft()

        for my, mx in D:
            nx = cx + mx
            ny = cy + my

            if grid[ny][nx] == ".":
                # 未探索
                que.append((ny, nx, c + 1))
                grid[ny][nx] = "!"  # 探索済み
            
            elif grid[ny][nx] == "G": # ゴール
                return c + 1

    return -1

print(bfs())