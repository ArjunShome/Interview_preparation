class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, is_balanced: bool, height: int):
        self.is_balanced = is_balanced
        self.height = height

def heightBalancedBinaryTree(tree):
    # Write your code here.
    tree_info = check(tree)
    return tree_info.is_balanced

def check(tree):
    if not tree:
        return TreeInfo(True, -1)
    
    left = check(tree.left)
    right = check(tree.right)

    is_balanced = left.is_balanced and right.is_balanced and (abs(left.height - right.height) <= 1)
    height = max(left.height, right.height) + 1

    return TreeInfo(is_balanced, height)


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.right.left = BinaryTree(7)
    root.left.right.left.left = BinaryTree(12)
    root.left.right.left.right = BinaryTree(13)
    root.left.right.right = BinaryTree(8)
    root.right = BinaryTree(3)
    root.right.right = BinaryTree(6)
    root.right.right.left = BinaryTree(9)
    root.right.right.right = BinaryTree(10)

    print(heightBalancedBinaryTree(root))

