import tables, macros, math, sets, strutils, strformat, sugar
template `max=`(x,y) = x = max(x,y)
template `min=`(x,y) = x = min(x,y)
template makeArray(x, init):auto =
    var v:array[x, init.type]
    when init isnot typedesc:
        for a in v.mitems: a = init
    v
macro Array(lens: varargs[typed], init):untyped =
    var a = fmt"{init.repr}"
    for i in countdown(lens.len - 1, 0):
        a = fmt"makeArray({lens[i].repr}, {a})"
    parseStmt(fmt"""
block:
  {a}""")

let read = iterator: string {.closure.} =
    while true:
        for s in stdin.readLine.split:
            yield s

var item = initTable[(int, int), int]()
let R, C, K = read().parseInt

for _ in 1..K:
    let r, c, v = read().parseInt
    item[(r, c)] = v

var dp = Array(1..3000, 1..3000, 4, -1)
dp[1][1][0] = 0

for r in 1..R:
    for c in 1..C:
        var v = item.getOrDefault((r, c), 0)
        for i in 0..3:
            if dp[r][c][i] < 0: continue
            if r < R:
                dp[r + 1][c][0].max = dp[r][c][i]
            if c < C:
                dp[r][c + 1][i].max = dp[r][c][i]
            if i < 3 and v > 0:
                if r < R:
                    dp[r + 1][c][0].max = dp[r][c][i] + v
                if c < C:
                    dp[r][c + 1][i + 1].max = dp[r][c][i] + v

var v = item.getOrDefault((R, C), 0)
for n in 0..2:dp[R][C][n] += v
echo max dp[R][C]
