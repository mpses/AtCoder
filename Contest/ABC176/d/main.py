#!/usr/bin/env python3
INF = 10**7
import sys
input = sys.stdin.readline
from collections import*

def bfs(sx, sy, gx, gy, c):
    q = deque([(sx, sy)])
    dist = [[INF] * W for _ in range(H)]
    dist[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        if (x, y) == (gx, gy): return dist[gx][gy]
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0<=nx<H and 0<=ny<W and dist[nx][ny] > dist[x][y]:
                if c[nx][ny] == ".":
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
        for nx in range(x-2, x+3):
            for ny in range(y-2, y+3):
                if 0<=nx<H and 0<=ny<W and dist[nx][ny] > dist[x][y]:
                    if c[nx][ny] == ".":
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny)) 
    return -1
H, W = map(int, input().split())

cx, cy = map(int, input().split())
dx, dy = map(int, input().split())
ans = bfs(cx - 1, cy - 1, dx - 1, dy - 1, [input()[:-1] for _ in range(H)])
print(ans if ans != INF else -1)
