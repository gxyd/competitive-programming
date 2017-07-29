#!/usr/bin/python3

def isPalindrome(s):
    l = len(s)
    if l % 2 == 0:
        return s[: l//2] == s[-1: -l//2 - 1:-1]
    else:
        return s[:l//2] == s[-1: -(l//2 + 1):-1]

n = input()
print(isPalindrome(n))
