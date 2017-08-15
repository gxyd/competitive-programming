#!/usr/bin/python3

n, m = map(int, input().split())

X = []

for i in range(m):
    a, b = map(int, input().split())
    X.append((a, b))

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    if (a, b) in X:
        print("YES")
    else:
        print("NO")
