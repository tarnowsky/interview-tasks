from lib.bst import BST

def invertTree(node: BST):
    if not node:
        return None
    node.less, node.more = invertTree(node.more), invertTree(node.less)
    return node

bst = BST(0)
bst.insert(-10,10,-5,5,-15,15,2,7,-2,-7,12,-12,17,-17)

print("Original:")
print(bst)
print("Inverted:")
invertTree(bst)
print(bst)