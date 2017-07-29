#!/usr/bin/python3

if __name__ == '__main__':
    n, d = map(int, input().strip().split())

    a = input().strip().split()
    print(" ".join(a[d: ] + a[0: d]))
