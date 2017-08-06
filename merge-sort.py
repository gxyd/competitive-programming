#!/usr/bin/python3


def merge(a, b):
    """Function to merge two arrays"""
    c = []
    inv_count = 0
    diff = len(a)
    i = [0]
    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            c.append(a[0])
            a.remove(a[0])
            i[0] += 1
        else:
            c.append(b[0])
            b.remove(b[0])
            inv_count += diff - i[0] + 1
    if len(a) == 0:
        c += b
    else:
        c += a
    return inv_count, c


def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return 0
    else:
        inversion_count = 0
        middle = len(x)//2

        inversion_count += mergesort(x[:middle])
        print(inversion_count)
        inversion_count += mergesort(x[middle:])
        print(inversion_count)
        inversion_count += merge(x[:middle], x[middle:])
        return inversion_count


print(mergesort([1, 3, 2]))
