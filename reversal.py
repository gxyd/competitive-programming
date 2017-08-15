#!/usr/bin/python3

t = int(input())
L = []

# for each test case

def func():
    n = int(input())
    X = list(map(int, input().split()))
    d = int(input())
    L.append(X[d:] + X[:d])


for i in range(t):
    func()


for i in range(t):
    print(" ".join(map(str, L[i])))
