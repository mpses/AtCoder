#!/usr/bin/env python3
# Atcoder ABC 157
# Problem B

a = []
for i in range(3):
  a.append(list(map(int, input().split())))

n = int(input())

for _ in range(n):  #b_n roop
   b = int(input())
   for i in range(3):
    for j in range(3):
      if b == a[i][j]:
        a[i][j] = 0  #make a 0
        
for i in range(3):
    bingo = False
    if sum(a[i]) == 0: #横チェック
     print("Yes")
     exit()
    if sum([a[0][i], a[1][i], a[2][i]]) == 0: #縦チェック
     print("Yes")
     exit()

if sum([a[0][0], a[1][1], a[2][2]]) == 0: #斜めチェック
    print("Yes")
    exit()

if sum([a[2][0], a[1][1], a[0][2]]) == 0: #逆斜めチェック
    print("Yes")
    exit()

#n(Yes)=0のとき
print("No")