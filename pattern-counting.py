#!/usr/bin/python3

q = int(input())

C = []

def func():
    # for each query
    s = input()
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == '1' and s[i+1] == '0':
            j = i + 1
            while j < len(s) and s[j] == '0':
                j += 1
            if j < len(s) and s[j] == '1':
                count += 1
            i = j
        else:
            i += 1
    return count


for i in range(q):
    C.append(func())

for i in C:
    print(i)
