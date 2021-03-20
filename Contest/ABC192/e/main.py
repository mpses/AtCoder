#!/usr/bin/env python3
(n, m, x, y), *z = [[*map(int, o.split())] for o in open(0)]
from heapq import heappush, heappop

INF = float("inf")
graph = [[] for _ in range(n)]
for a, b, c, d in z:
    a -= 1
    b -= 1
    graph[a].append((c, d, b))
    graph[b].append((c, d, a))
 
import heapq
 
INF = float("inf")
 
def dijkstra(graph, start):
    global n
    queue = [(0, start)]
    dist = [INF] * n
    dist[start] = 0
 
    while queue:
        cost, current = heapq.heappop(queue)
        if cost > dist[current]:
            continue
 
        for n_cost, n_train_mul, n in graph[current]:
            new_cost = dist[current]
            # 現在の駅で列車が発車するのを待つ
            if dist[current] % n_train_mul != 0:
                new_cost += (n_train_mul - (dist[current] % n_train_mul))
 
            # 移動する
            new_cost += n_cost
 
            if dist[n] > new_cost:
                dist[n] = new_cost
                heapq.heappush(queue, (dist[n], n))
    return dist
 
dist = dijkstra(graph, x - 1)[y - 1]
print(dist if dist != INF else -1)