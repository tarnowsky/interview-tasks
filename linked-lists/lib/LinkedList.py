from __future__ import annotations

class LinkedList:
    def __init__(self, data=0):
        self._next: LinkedList = None
        self._data = data

    def insert(self, data, *args) -> LinkedList:
        new_node = LinkedList(data)
        head = self
        while head._next: head = head._next
        head._next = new_node
        for next_data in args:
            head = head._next
            head._next = LinkedList(next_data)
        return self

    def __str__(self):
        result = ''
        head = self
        while head:
            result += f'{head._data} -> '
            head = head._next
        return result[:-4]

