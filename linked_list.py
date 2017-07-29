#!/usr/bin/python

class Node:
    """
    Represents the node class
    """
    __slots__ = ('data', 'next')

    def __init__(self, data):
        self.data = data # assign data
        self.next = None # initialise 'next' as NULL


class LinkedList:
    """
    Create a new linked list.
    """
    __slots__ = ('head',)

    def __init__(self):
        """
        Initialize the LinkedList with head as "NULL".
        """
        self.head = None

    def __repr__(self):
        s = ""
        temp = self.head
        while temp.next:
            s += str(temp.data) + " -> "
            temp = temp.next
        s += str(temp.data)
        return s

    __str__ = __repr__

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def insert_at_end(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next

        old_endNode = temp
        old_endNode.next = node

    def __contains__(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def __getitem__(self, i):
        temp = self.head
        for index in range(i):
            if temp is None:
                raise IndexError("index out of range")
            temp = temp.next

        return temp.data


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    print(llist)
    zero = Node(0)
    fourth = Node(4)

    llist.insert_at_beginning(zero)
    print(llist)

    llist.insert_at_end(fourth)
    print(llist)

    print(3 in llist)
    print(llist[1])
    print(llist[5])
