#!/usr/bin/python3

q = int(input())


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack += list(graph[vertex] - visited)
    return visited


def func():
    # for each query
    n, m, clib, croad = map(int, input().split())
    X = []
    for i in range(m):
        a, b = map(int, input().split())
        X.append((a, b))

    if m == 0:
        return n*clib

    if clib <= croad:
        return clib*n

    graph = dict([(i, set()) for i in range(1, n+1)])
    for i, j in X:
        graph[i].add(j)
        graph[j].add(i)

    components = []
    k = set(graph.keys())
    while k:
        node = k.pop()
        visited = dfs(graph, node)
        components.append(visited)
        k -= visited

    cost = 0
    for i in components:
        cost += clib + croad*(len(i) - 1)
    return cost


Y = []

for i in range(q):
    Y.append(func())

for i in Y:
    print(i)
