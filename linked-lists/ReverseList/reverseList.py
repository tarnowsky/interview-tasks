from __future__ import annotations
from ..lib.LinkedList import LinkedList as LL
class Node(LL):
    def __init__(self, data=0):
        super().__init__(data)
        
    def reverse(self) -> Node:
        pass

head = Node().insert(1).insert(2).insert(5)
print(head)
head = head.reverse()
print(head)
