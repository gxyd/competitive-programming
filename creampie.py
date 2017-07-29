#!/usr/bin/python3

t = int(input())

def func(m, n, cost):
    for i, ci in enumerate(cost):
        for j, cj in enumerate(cost):
            if i !=j and ci + cj == m:
                return "%s %s" % (i+1, j+1)


for i in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))
    print(func(m, n, cost))
