#!/usr/bin/python3

s = input()
count = dict()

for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


def isValid1(dictionary):
    l = len(set(dictionary.values()))
    if l == 1:
        return True
    else:
        return False


def isValid2(dictionary):
    for i in dictionary:
        dictionary[i] -= 1
        if dictionary[i] == 0:
            dictionary.pop(i)
            if isValid1(dictionary):
                return True
            dictionary[i] = 1
        else:
            if isValid1(dictionary):
                return True
            dictionary[i] += 1
    return False


if isValid1(count) or isValid2(count):
    print("YES")
else:
    print("NO")
