#!/usr/bin/env python3
INF = float("inf")
import sys
input = sys.stdin.readline
from collections import*

def bfs():
    q = deque([(sx, sy)])
    dist = [[INF] * W for _ in range(H)]
    dist[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        b = dist[x][y]
        if (x, y) == (gx, gy):
            return b
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] > b and c[nx][ny] == ".":
                dist[nx][ny] = b
                q.appendleft((nx, ny))
        b += 1
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] > b and c[nx][ny] == ".":
                    dist[nx][ny] = b
                    q.append((nx, ny)) 
    return -1

H, W = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())
sx, sy, gx, gy = cx - 1, cy - 1, dx - 1, dy - 1
c = [input()[:-1] for _ in range(H)]
ans = bfs()
print(ans if ans != INF else -1)