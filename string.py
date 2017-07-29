#!/usr/bin/python3

s = input()
n = int(input())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z']


def weight(s):
    w = 0
    for i in s:
        w += letters[i]
    return w

i = 0
l = len(s)
weights = []
for i in range(1, l):
    xi_weight = letters[s[i]]
    weights.append()
    if s[i] == s[i - 1]:
        weights[i-1] += xi_weight

for i in range(n):
    p = int(input())
    if p in weights:
        print("YES")
    else:
        print("NO")
