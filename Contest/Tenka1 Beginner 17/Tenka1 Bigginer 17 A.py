#!/usr/bin/env python3.4.3
# Tenka1 Programmer Beginner Contest (17) A
#ワンライナーの本気
print(sum(sorted([[int(i) for i in input().split()] for _ in range(int(input()))], key=lambda x: x[1])[0]))