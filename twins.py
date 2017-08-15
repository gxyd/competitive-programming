#!/usr/bin/python3

n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

min_x = float('inf')
ind_x = None

def find_min(a):
    m = float('inf')
    ind = None
    for i in range(len(a)):
        if m > a[i]:
            m = a[i]
            ind = i

    return m, ind


min_x, ind_x = find_min(X)
min_y, ind_y = find_min(Y)

if ind_y != ind_x:
    print(min_x + min_y)
else:
    min_s_x, ind_s_x = find_min(X[:ind_x] + X[ind_x+1:])
    min_s_y, ind_s_y = find_min(Y[:ind_y] + Y[ind_y+1:])

    s1 = min_s_x + min_y
    s2 = min_x + min_s_y
    if s1 < s2:
        print(s1)
    else:
        print(s2)
