#!/usr/bin/env python3.4.3
# 三井住友信託銀行プログラミングコンテスト2019 C

x = int(input())
c = x//100
print(int(100*c <= x <= 105*c))