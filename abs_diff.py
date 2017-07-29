#!/usr/bin/python3

n = int(input())
A = sorted(map(int, input().split()))

m = float('inf')
for i in range(n-1):
    a = abs(A[i] - A[i+1])
    if m > a:
        m = a


print(m)
