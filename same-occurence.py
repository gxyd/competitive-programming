#!/usr/bin/python3

n, k = map(int, input().split())
an = list(map(int, input().split()))
X = []


def func():
    x, y = map(int, input().split())

    countx = 0
    county = 0
    k = 0
    number_of_sub = 0
    last_x = last_y = -1

    while k < n:
        if an[k] == x:
            countx += 1
            last_x = k
        elif an[k] == y:
            county += 1
            last_y = k

        if countx > county:
            number_of_sub += k - last_x + 1
        elif countx < county:
            number_of_sub += k - last_y + 1
        else:
            number_of_sub += k - max(last_x, last_y)

        k += 1
    return number_of_sub


for i in range(k):
    X.append(func())

for i in range(k):
    print(X[i])
