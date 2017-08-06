#!/usr/bin/python3

n, m = map(int, input().split())
X = list(map(int, input().split()))


def func(a):
    s = 0
    for i in range(m-1):
        j = i+1
        while j < m:
            if a[i] > a[j]:
                s += 1
            j += 1
    return s


su = 0

for i in range(n-m+1):
    su += func(X[i: i+m])

print(su)
