#!/usr/bin/python3

def remove_duplicate(a, n):
    r = []
    for i in a:
        if i not in a:
            r.append(i)
        else:
            pass
    return r
