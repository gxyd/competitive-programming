#!/usr/bin/python3

if __name__ == '__main__':
    N = int(input())
    strings = [input() for i in range(N)]

    Q = int(input())
    queries = [input() for i in range(Q)]

    for query in queries:
        print(strings.count(query))
