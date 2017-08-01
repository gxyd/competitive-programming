#!/usr/bin/python3

n = int(input())
P = list(map(int, input().split()))
D = list(map(int, input().split()))

def func():
    for i in range(n-1):
        p_diff = P[i+1] - P[i]
        d_diff = D[i+1] - D[i]
        if p_diff*d_diff < 0:
            return "No"
        elif p_diff*d_diff == 0:
            if p_diff != 0 or d_diff != 0:
                return "No"
    return "Yes"

print(func())
