#!/usr/bin/python3

n = int(input())
vin = input()
cat = input()

score = 0
for i in range(n):
    if vin[i] != cat[i] and vin[i] != ".":
        score += 1


print(score)
