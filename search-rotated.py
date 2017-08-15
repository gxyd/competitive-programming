#!/usr/bin/python3

t = int(input())

# for one test case
n = int(input())
X = list(map(int, input().split()))
k = int(input())

def search_start(ar):
    middle = len(ar)//2
    if ar[0] > ar[middle-1]:
        return search_start(ar[:middle])
    elif ar[middle] < ar[]
    else:
        search_start(ar[middle:])
