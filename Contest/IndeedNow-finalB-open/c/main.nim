import tables, macros, math, sets, strutils, sequtils, strformat, sugar
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

var 
    n = read().parseInt
    s = read()
    c = newSeqWith(n, read().parseInt)

var dp = Array(5001, 100000000000000)
var A = Array(5000, 5000, false)
for center in 0..<n:
    for i in 0..1:
        var L = center
        var R = center + i
        while 0 <= L and R < n and s[L] == s[R]:
            A[L][R] = true
            L -= 1
            R += 1
dp[0] = 0
for i in 0..<n:
    for j in 0..<n-i:
        if A[i][i+j]:
            dp[i+j+1].min = dp[i] + c[j]
echo dp[n]