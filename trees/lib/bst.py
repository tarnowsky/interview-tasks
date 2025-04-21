from __future__ import annotations
from collections import deque

class BST:
    def __init__(self, val: int=None, less: BST=None, more:BST=None):
        self.val = val
        self.less = less
        self.more = more

    def find(self, num):
        node = self
        while True:
            if not node: return False
            if num == node.val: return True
            if num > node.val: node = node.more
            else: node = node.less

    def delete(self, num) -> object | None:
        # if its root
        if self.val == num:
            if not self.less: return self.more
            if not self.more: return self.less
            else:
                tmp = self.less
                while tmp.more: tmp = tmp.more
                tmp.more = self.more
                return self.less
        elif num > self.val and self.more:
            self.more = self.more.delete(num)
        elif num < self.val and self.less:
            self.less = self.less.delete(num)
        return self

    def insert(self, *values: int) -> BST:
        if not self.val:
            self.val = values[0]
            values = values[1:]

        for value in values:
            current = self
            while True:
                if value < current.val:
                    if current.less is None:
                        current.less = BST(value)
                        break
                    current = current.less
                else:
                    if current.more is None:
                        current.more = BST(value)
                        break
                    current = current.more

        return self
    
    def __str__(self):
        def draw_tree(node, prefix="", is_left=True):
            if not node:
                return ""
            result = ""
            if node.more:
                result += draw_tree(node.more, prefix + ("│   " if is_left else "    "), False)
            result += prefix + ("└── " if is_left else "┌── ") + str(node.val) + "\n"
            if node.less:
                result += draw_tree(node.less, prefix + ("    " if is_left else "│   "), True)
            return result

        return draw_tree(self)

tree = BST(5).insert(3, 7, 2, 4)
print(tree)