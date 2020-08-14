#!/usr/bin/env python3
from datetime import datetime as dt
a = dt.strptime(input(), "%m %d")
print(sum(d <= a for d in [dt(1900,i,i) for i in range(1, 13)]))