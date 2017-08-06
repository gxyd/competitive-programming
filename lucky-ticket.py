#!/usr/bin/python3

def isLucky(n):
    return sum(map(int, str(n)[:3])) == sum(map(int, str(n)[-3:]))


n = int(input())

while True:
    n += 1
    if isLucky(n):
        break


print(n)
