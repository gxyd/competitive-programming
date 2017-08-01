#!/usr/bin/python3

N = int(input())
W = set(map(int, input().split()))

i = 0
while len(W) > 0:
    i += 1
    m = min(W)
    W = W.difference(set(range(m, m + 5)))

print(i)
