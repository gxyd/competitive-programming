#!/usr/bin/python3

q = int(input())

# for each query
hck = "hackerrank"

def func(string, hack):
    if string == hack:
        return True
    if len(string) == 0:
        return False
    if string[0] == hack[0]:
        return func(string[1:], hack[1:])
    else:
        return func(string[1:], hack)


X = []

for i in range(q):
    s = input()
    X.append(s)

for i in X:
    if func(i, hck):
        print("YES")
    else:
        print("NO")
