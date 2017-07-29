#!/usr/bin/python3

if __name__ == '__main__':
    r = int(input())
    str_arr = input().split()
    mod = 10**9 + 7
    answer = 1
    for i in str_arr:
        answer = (answer * int(i)) % mod
    print(answer)

