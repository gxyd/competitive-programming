#!/usr/bin/python3

s = input()

if s == '':
    print(0)
else:
    count = 0
    for i in s:
        if i == '_':
            count += 1

    print(count+1)
