#!/usr/bin/python3

n, m, k = map(int, input().split())
X = []

for i in range(m):
    x, y = map(int, input().split())
    X.append((x, y))


# O(n*log(n))
r1 = sorted([a for a in X if a[1] == 0], key=lambda i: i[0])
r2 = sorted([a for a in X if a[0] == n], key=lambda i: i[1])
r3 = sorted([a for a in X if a[1] == n], key=lambda i: i[0], reverse=True)
r4 = sorted([a for a in X if a[0] == 0], key=lambda i: i[1], reverse=True)

s1 = sum([a[0] for a in r1])
s2 = sum([a[1] for a in r2])
s3 = sum([a[0] for a in r3])
s4 = sum([a[1] for a in r4])

# for each point go clockwise and anti-clockwise
# O(n)
t1 = s1
for i, point0 in enumerate(r1):
    pass
