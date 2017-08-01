#!/usr/bin/python3


A = []

def inOrder(root):
    if root:
        inOrder(root.left)
        A.append(root.data)
        inOrder(root.right)


def isSorted(A):
    l = len(A)
    for i in range(l-l):
        if A[i] >= A[i+1]:
            return False
    return True


def check_binary_search_tree_(root):
    inOrder(root)
    return isSorted(A)