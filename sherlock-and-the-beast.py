#!/usr/bin/python3

T = int(input())

# number of digits
N = []
for i in range(T):
    N.append(int(input()))


def func(n):
    n5 = n
    n3 = 0
    while n5 >= 0:
        if n5 % 3 == 0 and n3 % 5 == 0:
            return n5, n3
        else:
            n5 -= 1
            n3 += 1
    return -1


for n in N:
    f = func(n)
    if f == -1:
        print(f)
    else:
        n5, n3 = f
        r = '5'*n5 + '3'*n3
        print(r)
