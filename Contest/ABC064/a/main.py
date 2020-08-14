#!/usr/bin/env python3
print("YNEOS"[min(int(input().replace(" ",""))%4,1)::2])