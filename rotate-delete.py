#!/usr/bin/python3

t = int(input())
X = []

for i in range(t):
    k = int(input())
    a = list(map(int, input().split()))

    if k % 2 == 0:
        t = k//2
    else:
        t = k//2 + 1

    j = t
    l = 1
    while j > 0:
        a = [a[-1]] + a[:-1]
        del a[-l]
        l += 1
        j -= 1

    for r in range(k-t-1):
        a = [a[-1]] + a[:-1]
        del a[0]

    X.append(a[0])

for i in X:
    print(i)
