#!/usr/bin/python3

def search(ar, n):
    if len(ar) == 0:
        return -1
    middle = len(ar)//2
    if ar[middle] == n:
        return middle
    elif ar[middle] < n:
        return middle - 1 + search(ar[middle:], n)
    else:
        return search(ar[:middle], n)


print(search([1, 1, 3, 5, 6, 7], 3))
