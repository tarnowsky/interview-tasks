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
    
    def remove_duplicates(self) -> Node:
        visited = defaultdict(bool)
        head = self
        visited[head._data] = True
        
        while head._next:
            if visited[head._next._data]:
                head._next = head._next._next
            else:
                visited[head._next._data] = True
                head = head._next

        return self

    def __str__(self):
        result = ''
        head = self
        while head:
            result += f'{head._data} -> '
            head = head._next
        return result[:-4]

head = Node().insert(1, 2, 2, 4, 5, 6, 6 ,7 ,2, 8, 0)
print(head)
head = head.remove_duplicates()
print(head)
