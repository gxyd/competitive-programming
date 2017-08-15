#!/usr/bin/python3

T = int(input())

# for each test case
n, m, pos = map(int, input().split())

ar = list(range(n))


def binary_search(l, r, element):
    """
    l: low index
    r: high index
    element: element to be searched
    ar: array in which searching is to be done
    """
    middle = l + (r - l)//2
    if ar[middle] == element:
        return middle
    if ar[middle] > element:
        return binary_search(l, middle-1, element)
    else:
        return binary_search(middle+1, r, element)


