#!/usr/bin/python3

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0]*N
    for i in range(M):
        a, b, k = map(int, input().split())
        A[a-1: b] = [A[j] + k for j in range(a-1, b)]
    print(max(A))
