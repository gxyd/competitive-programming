#!/usr/bin/python

n = int(input())
X = set(map(int, input().split()))
Y = set(map(int, input().split()))

if X.union(Y) == set(range(1, n+1)):
    print("We win :-)")
else:
    print(":-( Lost!!")
