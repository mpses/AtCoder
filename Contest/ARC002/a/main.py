#!/usr/bin/env python3
def is_leap_year(y):  # 閏年判定
    if y % 400 == 0: return True
    elif y % 100 == 0: return False
    elif y % 4 == 0: return True
    else: return False
print(["NO", "YES"][is_leap_year(int(input()))])