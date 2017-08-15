#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))

a1 = [a[i] for i in range(0, n, 2) if a[i] % 2 != 0]
a2 = [a[i] for i in range(1, n, 2) if a[i] % 2 == 0]

spare = 0

for i in range(n):
    if i % 2 == 0 and a[i] % 2 == 0:
        spare += a[i] - 2
    elif i % 2 == 1 and a[i] % 2 == 1:
        spare += a[i] - 1

if len(a1) == len(a2):
    print(len(a1))
else:
    count = 0
    m = min(len(a1), len(a2))
    if len(a1) > len(a2):
        count += len(a2)
        r = a1[len(a2):]
        for l in range(len(r)):
            if r[l] == 1:
                spare -= 1
                count += 1
            else:
                pass
    else:
        count += len(a1)
        r = a2[len(a1):]

    for i in range(m):
        spare += a1[i] + a[2] - 3

    for i in range(len(r)):
        pass
