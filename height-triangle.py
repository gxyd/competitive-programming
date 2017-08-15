#!/usr/bin/python3

b, a = map(int, input().split())

if (2*a) % b == 0:
    h = (2*a)//b
else:
    h = (2*a)//b + 1

print(h)
