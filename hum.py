#!/usr/bin/python3

q = int(input())
R = []


def func():
    n = int(input())
    a = list(map(int, input().split()))

    for i, j in enumerate(a):
        if i % 2 == 0:
            if j % 2 == 0:
                spare += j - 2
            else:
                if j == 1:
                    nec_spare -= 1
                    transfer -= 1
        else:
            if j % 2 == 1:
                spare += 
