
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def repairBst(tree):
    # Write your code here.
    prev = None
    node_1 = None
    node_2 = None

    def recurseFindOffNodes(tree):
        nonlocal prev, node_1, node_2

        if tree is None:
            return 
        
        recurseFindOffNodes(tree.left)

        if prev and tree.value < prev.value:
            if node_1 is None:
                node_1 = prev
            node_2 = tree
        
        prev = tree
        recurseFindOffNodes(tree.right)

    # Calling the find 
    recurseFindOffNodes(tree)

    # Swapped
    node_1.value, node_2.value = node_2.value, node_1.value
    return tree


if __name__ == '__main__':
    bst  = BinaryTree(10)
    bst.left = BinaryTree(7)
    bst.left.right = BinaryTree(12)
    bst.right = BinaryTree(20)
    bst.right.left = BinaryTree(8)
    bst.right.left.right = BinaryTree(14)
    bst.right.right = BinaryTree(22)
    bst.left.left = BinaryTree(3)
    bst.left.left.left = BinaryTree(2)

    print(repairBst(bst))

