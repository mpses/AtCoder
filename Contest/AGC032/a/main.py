n, *b = map(int, open(0).read().split())
l = []
while 1:
    for i in reversed(range(len(b))):
        if i + 1 == b[i]:
            del b[i]
            l += i + 1,
            break
    else:
        break
if b:
    print(-1)
    exit()
for i in l[::-1]:
    print(i)