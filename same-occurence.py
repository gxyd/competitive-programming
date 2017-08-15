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
    last_last_x = last_last_y = last_x = last_y = -1


    while k < n:
        if an[k] == x:
            countx += 1
            last_last_x = last_x
            last_x = k
        elif an[k] == y:
            county += 1
            last_last_y = last_y
            last_y = k

        if countx > county:
            number_of_sub += k - last_x
        elif countx < county:
            number_of_sub += k - last_y
        else:
            if an[k] == y:
                number_of_sub += last_x - last_last_y
            elif an[k] == x:
                number_of_sub += last_y - last_last_x
            else:
                number_of_sub += k - countx

        k += 1
    return number_of_sub


for i in range(k):
    X.append(func())

for i in range(k):
    print(X[i])
