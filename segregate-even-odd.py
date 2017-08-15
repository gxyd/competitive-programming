#!/usr/bin/python3

q = int(input())
X = []

def func():
    n = int(input())
    a = list(map(int, input().split()))

    e = [i for i in a if i % 2 == 0]
    o = [i for i in a if i % 2 == 1]
    return sorted(e) + sorted(o)

for i in range(q):
    X.append(func())

for i in X:
    print(" ".join(map(str, i)))
