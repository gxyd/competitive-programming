#!/usr/bin/python3

n, m, k = map(int, input().split())

X = []

for i in range(m):
    x, y = map(int, input().split())
    X.append((x, y))


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


dist = []

for i range(m):
    r = X[i]
