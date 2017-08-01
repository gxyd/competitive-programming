#!/usr/bin/python3

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())

Apples = list(map(int, input().split()))
Oranges = list(map(int, input().split()))

house = set(range(s, t+1))

ap = 0
for i in Apples:
    if i + a in house:
        ap += 1

ora = 0
for i in Oranges:
    if i + b in house:
        ora += 1

print(ap)
print(ora)
