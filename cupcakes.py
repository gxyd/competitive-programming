#!/usr/bin/python3

n = int(input())
K = reversed(sorted(map(int, input().split())))

s = 0
for i, ci in enumerate(K):
    s += 2**(i)*ci

print(s)
