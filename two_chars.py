#!/usr/bin/python3

if __name__ == '__main__':
    n = int(input())
    s = input()

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            s = s.replace(s[i], ' ')
    s = s.replace(" ", "")
    print(s)
