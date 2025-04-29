from __future__ import annotations

class Node:
    def __init__(self, data:int=0):
        self._data = data
        self._next = None
        self._prev = None
    
    def reverse(self) -> Node:
        curr = self
        prev = None
        while curr:
            next_node = curr._next
            curr._next = prev
            curr._prev = next_node
            prev = curr
            curr = next_node
        return prev
    
    def insert(self, *args: int) -> Node:
        head = self
        while head._next: head = head._next
        for data in args[:]:
            new_node = Node(data)
            new_node._prev = head
            head._next = new_node
            head = head._next
        return self
    
    def __str__(self) -> str:
        result = 'None <- '
        head = self
        while head:
            result += f'{head._data} <-> '
            head = head._next
        return result[:-4] + '-> None'

head = Node()
head = head.insert(1, 2, 3, 4, 5, 6)
print(head)
head = head.reverse()
print(head)

        