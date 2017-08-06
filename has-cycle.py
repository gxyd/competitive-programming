#!/usr/bin/python3

def has_cycle(head):
    A = []
    temp = head
    while temp:
        A.append(temp)
        temp = temp.next
        if temp in A:
            return True
    return True
