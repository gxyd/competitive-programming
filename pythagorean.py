#!/usr/bin/python3

a = int(input())

def func(a):
    """For any odd number."""
    a0 = a**2
    k = (a0 - 1)//2
    b, c = k + 1, k
    return b, c


if a % 2 == 1:
    b, c = func(a)
    print(a, b, c)
else:
    i = 1
    while a % 2**(i+1) == 0:
        i += 1
    f = func(a//2**i)
    b, c = 2**i*f[0], 2**i*f[1]
    print(a, b, c)
