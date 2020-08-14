#!/usr/bin/env python3
s = sorted
i = input
print(["No", "Yes"][s(i()) < s(i(), reverse=True)])