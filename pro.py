#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))

j = n - 1
r = a[j]

while j > 0 and r < a[j - 1]:
    a[j] = a[j - 1]
    j -= 1
    print(" ".join(map(str, a)))

a[j] = r
print(" ".join(map(str, a)))
