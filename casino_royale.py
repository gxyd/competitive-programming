#!/usr/bin/python3

n, x, m = map(int, input().split())

lost = 0

for i in range(n):
    wi, pi = map(int, input().split())
    lost += wi*pi/100

print(x*m - lost*m)
