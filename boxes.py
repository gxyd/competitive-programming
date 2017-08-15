#!/usr/bin/python3

#q = int(input())
#
## for one query
#n = int(input())
a = list(map(int, input().split()))


def func():
    spare = 0
    for i, j in enumerate(a):
        if i % 2 == 0:
            if j % 2 == 0:
                spare += j - 2
            else:
                if j == 1:
                    spare -= 1
                else:
                    spare += j - 3
        else:
            if j % 2 == 1:
                if j != 1:
                    spare += j - 1
            else:
                spare += j - 1

    if spare < 0:
        return -1
    print(spare)

    spare = 0
    nec_spare = 0
    transfer = 0
    for i, j in enumerate(a):
        if i % 2 == 0:
            if j % 2 == 0:
                spare += j - 2
            else:
                nec_spare += 1
                if j != 1:
                    spare += j - 3
        else:
            if j % 2 == 1:
                spare += j - 1
            else:
                nec_spare += 1
                spare += j - 2

    if nec_spare % 2 == 0:
        return nec_spare//2
    else:
        return -1

print(func())
