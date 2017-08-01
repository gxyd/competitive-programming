#!/usr/bin/python3

n = int(input())
r = 10**9 + 7

X = [None]*n

for i in range(n):
    t = int(input())
    X[i] = (t**2) % r

for i in X:
    print(i)
