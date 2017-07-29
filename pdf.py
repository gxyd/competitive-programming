#!/usr/bin/python3

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

size = list(map(int, input().split()))
r = dict(zip(letters, size))

s = input()
n = len(s)
print(r)
set_val = set([r[key] for key in s])
maximum = max(set_val)
print(set_val)
print(n*maximum)