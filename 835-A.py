#!/usr/bin/python3

s, v1, v2, t1, t2 = map(int, input().split())

re1 = s*v1 + 2*t1
re2 = s*v2 + 2*t2
if re1 < re2:
    print("First")
elif re1 > re2:
    print("Second")
else:
    print("Friendship")
