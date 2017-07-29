#!/usr/bin/python3

n, k = map(int, input().split())
s = input()

def richieRich(n, k, s):
    non_palin = []
    palin = []

    if n == 1 and k > 0:
        return 9

    for i in range(0, n//2):
        if s[i] == s[n-1-i]:
            palin.append(i)
        else:
            non_palin.append(i)

    n_p = len(non_palin)

    if k < n_p:
        return -1
    else:

        s = list(s)

        for xj in non_palin:
            k -= 1
            r = str(max(int(s[xj]), int(s[n-1-xj])))
            s[xj] = s[n-1-xj] = r

        i = 0

        while k >= 1 and i < n//2:
            if i in palin:
                r = s[i]
                if s[i] != '9':
                    s[i] = '9'
                    k -= 1

                if s[n-1-i] != '9' and k > 0:
                    s[n-1-i] = '9'
                    k -= 1
                else:
                    s[i] = r
                    k += 1
            else:
                k -= 1
                s[i] = '9'
                s[n-1-i] = '9'

            i += 1

        if n % 2 != 0 and k > 0:
            s[n//2] = '9'

        return "".join(s)

print(richieRich(n, k, s))
