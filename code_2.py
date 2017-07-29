#!/usr/bin/python3

if __name__ == '__main__':
    n, k = map(int, input().split())

    if (n // k) % 2 == 0:
        print("NO")
    else:
        print("YES")
