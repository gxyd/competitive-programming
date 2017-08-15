#!/usr/bin/python3

n, p = map(int, input().split())

X = []
for i in range(p):
    a, b = map(int, input().split())
    X.append((a, b))

graph = dict([(i, set()) for i in range(n)])
for i, j in X:
    graph[i].add(j)
    graph[j].add(i)


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack += list(graph[node] - visited)

    return visited


components = []
k = set(graph.keys())

while k:
    node = k.pop()
    visited = dfs(graph, node)
    components.append(visited)
    k -= visited

t = [len(i) for i in components]
count = 0
l = 0
for j in range(len(t) - 1, 0, -1):
    l += t[j]
    count += t[j-1]*l

print(count)
