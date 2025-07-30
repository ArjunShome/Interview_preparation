# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None and tree2 is None:
        return None
    
    if not tree1 and tree2:
        return clone_tree(tree2)
    
    if not tree2 and tree1:
        return tree1
    
    tree1.value = tree1.value + tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1

def clone_tree(tree):
    if tree is None:
        return None
    node = BinaryTree(tree.value)
    node.left = clone_tree(tree.left)
    node.right = clone_tree(tree.right)
    return node

if __name__ == '__main__':
    tree1 = BinaryTree(1)
    tree1.left = BinaryTree(3)
    tree1.right = BinaryTree(2)
    tree1.left.left = BinaryTree(5)

    tree2 = BinaryTree(2)
    tree2.left = BinaryTree(3)
    tree2.left.right = BinaryTree(4)
    tree2.right = BinaryTree(6)

    # print(mergeBinaryTrees(tree1, tree2))
    m = mergeBinaryTrees(tree2, tree1)
    print(m)