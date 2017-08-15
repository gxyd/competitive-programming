n, m = map(int, input().split())
already_built = []
not_build = []

for i in range(m):
    r = input().split()
    if len(r) == 4:
        a, b, u, cost = map(int, r)
        not_build.append((a, b, cost))
    else:
        a, b, c = map(int, r)
        already_built.append((a, b, c))


connected_points = set()
for i in already_built:
    connected_points.update([i[0], i[1]])

not_build = sorted(not_build, key=lambda i: i[2])

cost = 0

for i in not_build:
    point0 = i[0]
    point1 = i[1]
    price = i[2]

    if point0 not in connected_points and point1 in connected_points:
        cost += price
        connected_points.update([point0])
    elif point1 not in connected_points and point0 in connected_points:
        cost += price
        connected_points.update([point1])

print(cost)
