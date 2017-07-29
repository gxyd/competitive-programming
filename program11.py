#!/usr/bin/python3

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0]*(N + 1)

    for i in range(M):
        a, b, k = map(int, input().split())
        A[a] += k
        if b + 1 <= N:
            A[b+1] -= k

    x = 0
    max = 0
    for i in range(1, N+1):
        x += A[i]
        if max < x:
            max = x

    print(max)
