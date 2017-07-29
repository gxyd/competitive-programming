#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))

i = 1
length = len(a)
while i < length:
    j = i
    while j > 0 and a[j] < a[j-1]:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1
    i += 1
    print(" ".join(map(str, a)))

