#!/usr/bin/python3

n = int(input())
X = []

for i in range(n):
    px, py, qx, qy = map(int, input().split())
    rx, ry = 2*qx - px, 2*qy - py
    X.append((rx, ry))

for rx, ry in X:
    print("%s %s" % (rx, ry))
