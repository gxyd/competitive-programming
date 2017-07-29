#!/usr/bin/python3

n, k = map(int, input().split())

H = map(int, input().split())
maximum = max(H)

if maximum < k:
    print(0)
else:
    print(maximum - k)
