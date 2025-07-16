class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        currentNode = self
        while True:
            if value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left       
        return self


def findClosestValueInBst(tree, target):
    # Write your code here.

    if not tree:
        return None
    if tree.value == target:
        return tree.value
    

    closest = float('inf')

    while tree:
        if abs(closest - target) > abs(tree.value - target):
                    closest = tree.value

        if tree.value < target:
            tree = tree.right
        else:
            tree = tree.left
    return closest



if __name__ == '__main__':
    # Example usage
    root = BST(10)
    root.insert(5)
    root.insert(15)
    root.insert(2)
    root.insert(7)
    root.insert(12)
    root.insert(20)

    target = 13
    print(findClosestValueInBst(root, target))  # Expected output: 12