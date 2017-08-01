#!/usr/bin/python3

k = int(input())

Cost = []

for i in range(k):
    # for a single query
    n, m, c_lib, c_road = map(int, input().split())

    X = [None]*m

    for i in range(m):
        ui, vi = map(int, input().split())
        X[i] = ui, vi

    # for one component
    if c_lib <= c_road:
        cost = c_lib*n
    else:
        Y = [set(X[0])]
        for ui, vi in X[1:]:
            index = 0
            while index < len(Y):
                s = Y[index]
                if ui in s or vi in s:
                    s.update([ui, vi])
                    break
                index += 1

            if index == len(Y):
                Y.append(set([ui, vi]))

        cost = 0
        print(Y)
        for s in Y:
            r = len(s)
            cost += (r-1)*c_road + c_lib

    Cost.append(cost)

for i in Cost:
    print(i)
