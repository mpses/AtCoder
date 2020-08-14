#!/usr/bin/env python3
# 深さ優先検索
def walk(f, x, y):
    # 10*10 のマップ範囲外に出るな！！！！！！禁じられた森に入ってはならん！！！
    if not (0 <= x < 10 > y >= 0):
        return

    i = y * 10 + x

    # 海歩くな！！！！！！！！！
    if f[i] == "x":
        return

    # 歩いた所を海に書き換えておこ
    f[i] = "x"

    # x, y の上下左右を歩いてみよ
    # 陸続きなら進むけどそうじゃないんだったらそこで止まるで
    walk(f, x, y + 1)
    walk(f, x, y - 1)
    walk(f, x + 1, y)
    walk(f, x - 1, y)

*j, = open(0)
field = "".join(map(str.strip, j))
for i, f in enumerate(field):
    # 陸なら無視
    if f == "o":
        continue
    
    ### リセット
    walking = list(field)
    y, x = divmod(i, 10)

    # 海ならそこだけ一旦埋め立ててみるで
    walking[i] = "o"
    walk(walking, x, y)

    # 陸が全て無くなったら陸続きやで。お疲れ様
    if "o" not in walking:
        print("YES")
        exit()
print("NO")