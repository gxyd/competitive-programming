#!/usr/bin/python3

if __name__ == '__main__':
    integer = int(input())
    a = [input() for i in range(integer)]
    for i in range(integer):
        print(a[i][-1::-1])
