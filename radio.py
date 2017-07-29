#!/usr/bin/python3

n, k = map(int, input().split())
X = list(map(int, input().split()))


def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

X = mergesort(X)

j = 0
while X:
    r = set(range(X[0], X[0] + 2*k + 1))
    X = list(set(X).difference(r))
    j += 1

print(j)