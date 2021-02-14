#!/usr/bin/env python3
import datetime
d = datetime.datetime.strptime(input(), "%Y/%m/%d")
while True:
  if d.year % (d.month * d.day) == 0:
    print(d.strftime("%Y/%m/%d"));exit()
  d += datetime.timedelta(days=1)