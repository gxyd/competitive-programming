#!/usr/bin/python3

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = input()
s = s.lower()


def func():
    for i in a:
        if i not in s:
            return False
    return True


if func():
    print("pangram")
else:
    print("not pangram")
