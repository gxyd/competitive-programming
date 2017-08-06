#!/usr/bin/python3

s = input()

alphabets = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z')


def func():
    if len(s) != 18 or s[5:] != "@hogwarts.com":
        return False
    r = s[:5]
    for i in r:
        if i not in alphabets:
            return False
    return True


if func():
    print("Yes")
else:
    print("No")
