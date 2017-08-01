#!/usr/bin/python3

N = int(input())
X = []

for i in range(N):
    r = int(input())
    if r < 38 or r % 5 == 0:
        X.append(r)
    elif (5*(r//5 + 1) - r) < 3:
        X.append(5*(r//5 + 1))
    else:
        X.append(r)

for i in X:
    print(i)
