#!/usr/bin/python3

n = int(input())
X = map(int, input().split())

a = [0, 0, 0, 0, 0]

for i in X:
    a[i-1] += 1

index = 0
m = a[index]

for i, j in enumerate(a[1:], 1):
    if m < j:
        m = j
        index = i

print(index + 1)
