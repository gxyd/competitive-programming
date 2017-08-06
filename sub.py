#!/usr/bin/python3

s = input()
k = int(input())

t = []

def func(string):
    for i in string:
        if string.count(i) < k:
            string = string.replace(i, '')

    if string == '':
        return

    # look for max, index
    maxi = string[0]
    for i in string[1:]:
        if i > maxi:
            maxi = i

    last_index = string.rfind(maxi)
    count = string.count(maxi)
    t.extend([maxi]*count)
    string = string[count+1:]
    return func(string)


func(s)
print("".join(t))