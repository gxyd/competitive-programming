#!/usr/bin/python3

from collections import Counter
T = int(input())
l = []

def func():
    n, x = map(int, input().split())
    X = list(map(int, input().split()))
    r = Counter(X)[x]
    if r == 0:
        return -1
    else:
        return r


for i in range(T):
    l.append(func())

for i in range(T):
    print(l[i])
