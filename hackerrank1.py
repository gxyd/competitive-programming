#!/usr/bin/python3

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [0]*(N + 1)
    for i in range(K):
        a, b, k = map(int, input().split())
        A[a-1] += k
        if (b < N):
            A[b] -= k

    x = 0
    Max = 0
    for i in range(N):
        x += A[i]
        if Max < x:
            Max = x
