#!/usr/bin/python3

if __name__ == '__main__':
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = 0
    sol1 = set()
    for ak in a:
        x += ak
        sol1.add(b[0] - x)
    print(sol1)

    for bk in b[1:]:
        x = 0
        sol = set()
        for ak in a:
            x += ak
            sol.add(bk - ak)
        sol1 = sol1.intersection(sol)
    print(len(sol1))
