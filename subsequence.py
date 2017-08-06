#!/usr/bin/python3

s = input()
k = int(input())

t = []

def replace(s):
    for i in s:
        if s.count(i) < k:
            s = s.replace(i, "")

    return s

# wrong sorted ('r', 5) and ('r', 6) will both be present
s = replace(s)
sorted_s = sorted([(i, s.index(i)) for i in set(s)], reverse=True, key=lambda x: x[0])


def func0(string, char):
    count = 0
    for j in string:
        if j == char:
            count += 1

    t.extend([char]*count)

    string = string[string.rfind(char)+1:]
    return string


for i, j in sorted(sorted_s):
    s = func0(s[j:], i)
    s = replace(s)


print(t)
