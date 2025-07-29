class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# def findKthLargestValueInBst(tree, k):
#     # Write your code here.
#     parent_node = tree
#     node = tree
#     kth_highest = 0
#     i = 0
#     while i <= k:
#         if not node.right and not node.left:
#             kth_highest = node.value
#             node = parent_node.left
#         else:
#             kth_highest = node.value
#             parent_node = node
#             node = node.right
            
#         i += 1
#     return kth_highest
     
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    lst_node_val = []
    lst_node_val = find(tree, k, lst_node_val)
    return lst_node_val[-1]

def find(tree, k, lst_node_values):
    if not tree:
        return
    if len(lst_node_values) == k:
        return lst_node_values
    
    find(tree.right, k, lst_node_values)
    if len(lst_node_values) < k:
        lst_node_values.append(tree.value)
    find(tree.left, k, lst_node_values)    
    return lst_node_values

if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)

    k = 3

    print(findKthLargestValueInBst(root, k))
