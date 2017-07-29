#!/usr/bin/python3

N, K = map(int, input().split())
L = []
luck = 0

for i in range(N):
    l, t = map(int, input().split())
    if t == 0:
        luck += l
    else:
        L.append(l)

L = sorted(L)

while K > 0 and len(L) > 0:
    luck += L.pop()
    K -= 1

luck -= sum(L)

print(luck)
