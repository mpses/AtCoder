#!/usr/bin/env python3.4.3
# CODE FESTIVAL 2017 Final B - Palindrome-phobia

*c, = map(input().count, "abc")
print(["YES","NO"][max(c)-min(c) > 1])