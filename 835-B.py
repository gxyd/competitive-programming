#!/usr/bin/python3

k = int(input())
n = int(input())


def sum_of_digits(n, k):
    l = len(str(n))
    r = 10**(l-1)
    s = 0
    for i in range(l-1, -1, -1):
        t = n//10**i
        s += t
        if s >= k:
            return True
        n -= t*10**i
    return False


def digits(n):
    l = len(str(n))
    r = 10**(l-1)
    a = []
    for i in range(l-1, -1, -1):
        t = n//10**i
        a.append(t)
        n -= t*10**i
    return a


if sum_of_digits(n, k):
    print(0)
else:
    r = sorted(digits(n))
    s = sum(r)
    i = 0
    change = 0
    while s < k and i < n:
        if r[i] != 9:
            s = s + 9 - r[i]
            change += 1
        i += 1
    print(change)
