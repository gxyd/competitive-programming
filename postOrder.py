#!/usr/bin/python2


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print root.data,