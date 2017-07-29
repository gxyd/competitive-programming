#!/usr/bin/python3

n = int(input())
A = list(map(int, input().split()))

A = sorted(A)[::-1]
l = len(A)

def func():
    for i in range(l-2):
        a, b, c = A[i:i+3]
        if a < b + c:
            return "%s %s %s" % (c, b, a)
    else:
        return "-1"

print(func())
