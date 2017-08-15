#!/usr/bin/python3

q = int(input())
R = []


def func0():
    n = int(input())
    a = list(map(int, input().split()))
    transfer = 0
    spare = 0
    nec_spare = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 == 0:
                spare += a[i] - 2
            else:
                if a[i] == 1:
                    transfer += 1
                    nec_spare -= 1
                    # spare -= 1
                else:
                    spare += a[i] - 2
        else:
            if a[i] % 2 == 1:
                if a[i] != 1:
                    spare += a[i] - 1
            else:
                spare += a[i] - 1

    if spare < 0:
        return -1
    return transfer


for i in range(q):
    R.append(func0())

for i in range(q):
    print(R[i])
