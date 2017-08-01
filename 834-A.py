#!/usr/bin/python3

v1, v2 = input().split()
n = int(input())

o1 = ord(v1)
o2 = ord(v2)

if n % 4 == 0:
    print("undefined")
elif n % 4 == 1:
    if (o1 == 118 and o2 == 60) or (o1 == 60 and o2 == 94) or (o1 == 94 and o2 == 62) or (o1 == 62 and o2 == 118):
        print("cw")
    else:
        print("ccw")
elif n % 4 == 2:
    print("undefined")
else:
    if (o1 == 118 and o2 == 62) or (o1 == 60 and o2 == 118) or (o1 == 94 and o2 == 60) or (o1 == 62 and o2 == 94):
        print("cw")
    else:
        print("ccw")
