class BST:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    lst = []
    lst = find(tree, lst)

    for i in range(len(lst)):
        if lst[i] == node:
            return lst[i + 1]
    return None
    

def find(tree, lst):
    # Write your code here.
    if not tree:
        return lst

    find(tree.left, lst)        
    lst.append(tree.value)
    find(tree.right, lst)

    return lst

if __name__ == '__main__':
    bst = BST(1)
    bst.left = BST(2)
    bst.right = BST(3)
    bst.left.left = BST(4)
    bst.left.left.left = BST(6)
    bst.left.right = BST(5)

    node = BST(5)
    print(findSuccessor(bst, node))
