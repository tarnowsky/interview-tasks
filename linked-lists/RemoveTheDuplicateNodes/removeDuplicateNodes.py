from __future__ import annotations
from collections import defaultdict
from lib.LinkedList import LinkedList as LL

class LinkedListDuplicatesExtension(LL):
    def __init__(self, data=0):
        super().__init__(data)

    def removeDuplicateNodes(self) -> LinkedListDuplicatesExtension:
        head = self
        nodes = defaultdict(bool)
        nodes[head._data] = True
        while head._next:
            if nodes[head._next._data]:
                head._next = head._next._next
            else:
                nodes[head._next._data] = True
                head = head._next
        return self
    

head = LinkedListDuplicatesExtension().insert(0, 1, 1, 2, 3, 4, 5, 6, 6)
print(head)
head = head.removeDuplicateNodes()
print(head)
