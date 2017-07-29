#!/usr/bin/python3


class Node(object):
    """
    Node class
    """
    __slots__ = ('data', 'left', 'right')

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def inOrder(self):
        """
        In-order traversal

        """
        r = ""
        data = str(self.data)
        if self.left:
            r += self.left.inOrder()
        r += " " + data + " "
        if self.right:
            r += self.right.inOrder()

        r = r.strip()
        return r

    def preOrder(self):
        """
        Pre-order traversel

        """
        r = ""
        data = str(self.data)
        r += data + " "
        if self.left:
            r += self.left.preOrder() + " "
        if self.right:
            r += self.right.preOrder()
        r = r.strip()
        return r

    def postOrder(self):
        """
        Post-order traversel

        """
        r = ""
        data = str(self.data)
        if self.left:
            r += " " + self.left.postOrder()
        if self.right:
            r += " " + self.right.postOrder()
        r += " " + data
        r = r.strip()
        return r


class Tree(object):
    def __init__(self, root):
        self.root = root

    def inOrder(self):
        return self.root.inOrder()

    def preOrder(self):
        return self.root.preOrder()

    def postOrder(self):
        return self.root.postOrder()


N4 = Node(4)
N6 = Node(6)
N3 = Node(3, right=N4)
N5 = Node(5, N3, N6)
N2 = Node(2, right=N5)
N1 = Node(1, right=N2)
T = Tree(N1)
print(N2.inOrder())
print(T.inOrder())
print(T.preOrder())
print(T.postOrder())
