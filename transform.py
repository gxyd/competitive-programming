#!/usr/bin/python3

#n, k, m = map(int, input().split())

def func():
    R = []
    k = 7

    for i in range(k):
        a, b = map(int, input().split())
        R.append((a, b))

    X = []
    elements = set()

    for a, b in R:
        flag = False

        if a in elements or b in elements:
            flag = True

        if flag:
            A = []
            B = []
            for s in X:
                if a in s:
                    A.append(s)
                if b in s:
                    B.append(s)
                s.update([a, b])
        else:
            X.append(set([a, b]))

        elements.update([a, b])

    return X


if __name__ == '__main__':
    print(func())
