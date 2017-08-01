#!/usr/bin/python3

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = max(A)
M = min(B)
x = 0

for i in range(m, M+1):
    if all([i % a == 0 for a in A]) and all([b % i == 0 for b in B]):
        x += 1

print(x)
