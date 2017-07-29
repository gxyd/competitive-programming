#!/usr/bin/python3

if __name__ == '__main__':
    s = input()

    n = 0
    for i in s:
        if not i.islower():
            n += 1
    print(n + 1)

