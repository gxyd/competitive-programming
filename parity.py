#!/usr/bin/python3

n = int(input())
a = list(map(int, input().split()))

s = sum(a)
def func():
    if s % 2 == 0:
        return 0
    else:
        if len(a) == 1:
            return -1

        i = 0
        while i < len(a):
            if a[i] % 2 != 0:
                return 1
            i += 1

        return -1


print(func())
