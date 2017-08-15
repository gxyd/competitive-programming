#!/usr/bin/python

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

graph0 = {1: set([2, 3]),
          2: set([1, 3, 4]),
          3: set([1, 4, 2]),
          4: set([3, 2]),
          5: set([6]),
          6: set([5])}

graph1 = {1: set([0, 2]),
          0: set([1, 2]),
          2: set([1, 0]),
          3: set([4]),
          4: set([3])}

graph2 = {1: set([2, 5]),
          2: set([1]),
          3: set([4, 8, 7]),
          4: set([3, 8]),
          5: set([1, 9, 10]),
          6: set([]),
          7: set([3, 11]),
          8: set([3, 4, 11, 12]),
          9: set([5, 10]),
          10: set([5, 9]),
          11: set([7, 8, 12]),
          12: set([11, 8])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack += list(graph[vertex] - visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in graph[vertex] - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))


components = []
vis = set()
for node in set(graph0.keys()) - vis:
    if node not in vis:
        visited = dfs(graph0, node)
        components.append(visited)
        vis = vis.union(visited)

print(components)
#print(dfs(graph2, 7))
#print(list(dfs_paths(graph0, 1, 5)))
