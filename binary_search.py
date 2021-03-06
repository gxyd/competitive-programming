#!/usr/bin/python3

def binary_search(ar, l, r, element):
    """
    l: low index
    r: high index
    element: element to be searched
    ar: array in which searching is to be done
    """
    middle = l + (r - l)//2
    if ar[middle] == element:
        return middle
    if l >= r:
        return -1
    if ar[middle] > element:
        return binary_search(ar, l, middle-1, element)
    else:
        return binary_search(ar, middle+1, r, element)


a = [-1, 1, 3, 4, 6, 7, 10, 21]
print(binary_search(a, 0, len(a)-1, 3))
