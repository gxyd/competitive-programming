#!/usr/bin/python3

n = int(input())
s = input()
k = int(input())

d = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z']

ld = len(d)
S = ''

for i in s:
    try:
        r = d.index(i)
        l = (r + k) % ld
        _i = d[l]
        S += _i
    except ValueError:
        S += i

print(S)
