from __future__ import annotations
from collections import defaultdict

class Node:
    def __init__(self, data=0):
        self._next: Node = None
        self._data = data

    def insert(self, data, *args) -> Node:
        new_node = Node(data)
        head = self
        while head._next: head = head._next
        head._next = new_node
        for next_data in args:
            head = head._next
            head._next = Node(next_data)
        return self

    def reverse(self) -> Node:
        head = self
        if not head._next:
            return self
        prev = None
        curr = head
        while curr:
            next_node = curr._next
            curr._next = prev
            prev = curr
            curr = next_node
        return prev

    def __str__(self):
        result = ''
        head = self
        while head:
            result += f'{head._data} -> '
            head = head._next
        return result[:-4]

head = Node().insert(1).insert(2).insert(5)
print(head)
head = head.reverse()
print(head)
