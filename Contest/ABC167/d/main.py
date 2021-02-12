#!/usr/bin/env python3
class CycleGetter():
    def __init__(self, max_time, lift: "list or func", start = 0, decrement = True):
        """
        :param max_time: 移動回数
        :param start: 初期条件
        :param lift: 遷移の関数（リストの場合はlift[i]）
        :return res: max_time 回進んだあとの場所
                front: cycleまでの要素のリスト
                cycle: cycle内の要素のリスト
                end: cycle後の余った部分の要素のリスト
                cnt: cycle回数
        """
        self.max_time = max_time
        if hasattr(lift, "__getitem__"):
            LIFT = lift
            if decrement:
                LIFT = [None] + LIFT
                max_time += 1
            lift = lambda x: LIFT[x]
        p = start
        front, cycle, end = [], [], []
        cnt = 0
        visit = {p:0}
        L, R = max_time, -1
        P = [p]
        for i in range(1, max_time):
            p = lift(p)
            if p in visit:
                # (L, R) = (サイクルに入るまでに移動した回数, サイクルの終端に着くまでに移動した回数)
                L, R = visit[p], i
                period = R - L
                break
            visit[p] = i
            P.append(p)
        front = P[:L]
        if L != max_time:
            cycle, end = P[L : R], P[L : L + (max_time - L) % period]
            cnt = (max_time - L) // period
        self.front, self.cycle, self.end, self.cnt = front, cycle, end, cnt

    def __call__(self):
        return self.front, self.cycle, self.end, self.cnt
    
    def apply(self, time = None):
        """
        :param time: 進む回数
        :return: 進み終わったときの場所
        """
        if time is None:
            time = self.max_time
        if time < len(self.front):
            return self.front[time]
        else:
            time -= len(self.front)
            if self.cycle:
                time %= len(self.cycle)
                return self.cycle[time]
            else:
                return self.end()
    
    def sum(self):
        return sum(self.front) + sum(self.cycle) * self.cnt + sum(self.end)

n, k, *a = map(int, open(0).read().split())
print(CycleGetter(k, a, 1).apply())