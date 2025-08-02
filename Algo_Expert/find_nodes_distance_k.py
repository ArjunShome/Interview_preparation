
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findNodesDistanceK(tree, target, distance_from_target):
    # Write your code here.
    
    # Populate the parents of each nodes.
    node_parents_dict = {}
    get_node_parents(tree, node_parents_dict)

    # Find the target Node
    node = find_target_node(tree, node_parents_dict, target)
    if not node:
        return []

    # BFS to find the distance of the nodes and the nodes from distance_from_target.
    return breadthFirstSearchForDistanceK(node, node_parents_dict, distance_from_target)
    

def breadthFirstSearchForDistanceK(node, node_parents_dict, distance_from_target):
    queue = [(node, 0)]
    seen = {node.value}

    while len(queue) > 0:
        current_node, distance = queue.pop(0)

        if distance == distance_from_target:
            nodes_at_k_distance = [node.value for node, _ in queue]
            nodes_at_k_distance.append(current_node.value)
            return nodes_at_k_distance
        
        connectedNodex = [current_node.left, current_node.right, node_parents_dict[current_node.value]]
        
        for node in connectedNodex:
            if node is None:
                continue
            if node.value in seen:
                continue
            seen.add(node.value)
            queue.append((node, distance + 1))

    return []



def find_target_node(tree, node_parents_pair, target):
    if tree.value == target:
        return tree
    
    parent_node = node_parents_pair[target]
    if parent_node.left and parent_node.left.value == target:
        return parent_node.left
    
    return parent_node.right



def get_node_parents(root, node_parents_dict, parent=None):
    if root:
        node_parents_dict[root.value] = parent
        get_node_parents(root.left, node_parents_dict, root)
        get_node_parents(root.right, node_parents_dict, root)



if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.right.left = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.right.right.right = BinaryTree(7)
    root.right.right.right.right = BinaryTree(8)
    
    target = 8
    k = 6

    print(findNodesDistanceK(root, target, k))
