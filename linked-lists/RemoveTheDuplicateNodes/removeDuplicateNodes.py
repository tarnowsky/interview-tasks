from __future__ import annotations
from lib.LinkedList import LinkedList as LL

class ReverseExtension(LL):
    def __init__(self, data=0):
        super().__init__(data)

    def reverse(self) -> ReverseExtension:
        prev = None
        curr = self
        while curr:
            next_node = curr._next
            curr._next = prev
            prev = curr
            curr = next_node
        return curr
    

head = ReverseExtension()
print(head)
head = head.reverse()
print(head)
