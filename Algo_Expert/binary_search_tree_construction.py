

class BinaryTree:
    def __init__(self, root):
        self.value = root
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        currentNode = self
        while True:
            if value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BinaryTree(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BinaryTree(value)
                    break
                else:
                    currentNode = currentNode.left       
        return self

    def contains(self, value):
        # Write your code here.
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False
            
    def remove(self, value):
        if not self:
            return self

        if self.value > value and self.left:
            self.left = self.left.remove(value)
        elif self.value < value and self.right:
            self.right = self.right.remove(value)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            cur_val = self.right
            while cur_val.left:
                cur_val = cur_val.left

            self.value = cur_val.value
            self.right = self.right.remove(cur_val.value)
        
        return self
    

if __name__ == '__main__':
    # Example usage
    root = BinaryTree(10)
    root.insert(5)
    root.insert(15)
    root.insert(2)
    root.insert(7)
    root.insert(12)
    root.insert(20)

    print(root.contains(7))  # True
    print(root.contains(8))  # False

    root.remove(5)
    print(root.contains(5))  # False
    print(root.contains(2))  # True