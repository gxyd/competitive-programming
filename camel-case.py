#!/usr/bin/python3

q = int(input())
X = []

def func():
    n = int(input())
    a = input().split()
    match = input()
    p = ""

    for string in a:
        j = 0
        i = 0
        while i < len(string) and j < len(match):
            if string[i].isupper():
                if string[i] != match[j]:
                    break
                else:
                    j += 1
            i += 1

        if j == len(match):
            p += " " + string

    if p:
        return p.strip()
    else:
        return "No match found"


for i in range(q):
    X.append(func())

for i in X:
    print(i)