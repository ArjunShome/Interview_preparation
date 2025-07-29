
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class RootInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


def reconstructBst(preOrderTraversalValues):
    root_info = RootInfo(0)
    root = reconstruct(preOrderTraversalValues, root_info, left_bound = float('-inf'), right_bound = float('inf'))
    return root

def reconstruct(traversal_value, root_info, left_bound, right_bound):
    if root_info.root_idx == len(traversal_value):
        return None

    root_value = traversal_value[root_info.root_idx]
    if root_value < left_bound or root_value >= right_bound:
        return None
     
    root_info.root_idx += 1
    
    left_sub_tree = reconstruct(traversal_value, root_info, left_bound, root_value)
    right_sub_tree = reconstruct(traversal_value, root_info, root_value, right_bound)

    return BST(root_value, left_sub_tree, right_sub_tree)


if __name__ == '__main__':
    array = [10,4,2,1,5,17,19,18]
    print(reconstructBst(array).value)
