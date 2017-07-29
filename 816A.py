#!/usr/bin/python3

n = input()
hh, mm = n[:2], n[3:]
k = 0

def isPalindrome(a, b):
    return a == b[::-1]

while True:
    if isPalindrome(hh, mm):
        break
    else:
        k += 1
        if int(mm) < 59:
            mm = int(mm) + 1
            if mm < 10:
                mm = '0' + str(mm)
            else:
                mm = str(mm)
        else:
            hh = int(hh) + 1
            mm = "00"
            if hh < 10:
                hh = '0' + str(mm)
            else:
                hh = str(mm)

print(k)
