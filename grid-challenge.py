#!/usr/bin/python3

t = int(input())


def isSorted(arr):
    l = len(arr)
    for i in range(l-1):
        if arr[i] > arr[i+1]:
            return False
    return True


R = ["YES"]*t

for i in range(t):
    # for each test case
    n = int(input())
    X = [None]*n
    for j in range(n):
        r = list(input())
        X[j] = sorted(r)

    for w1 in range(n):
        l = [X[w2][w1] for w2 in range(n)]
        if not isSorted(l):
            R[i] = "NO"
            break


for i in range(t):
    print(R[i])
