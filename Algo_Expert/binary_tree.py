
class BtNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = BtNode(root_value)
        self.traversal_str = ""

    def pre_order_traversed_values(self, start_node: BtNode):
        if start_node:
            self.traversal_str += f"{start_node.value} - "
            self.pre_order_traversed_values(start_node.left)
            self.pre_order_traversed_values(start_node.right)
        return self.traversal_str
    
    def in_order_traversed_values(self, start_node: BtNode):
        if start_node:
            self.in_order_traversed_values(start_node.left)
            self.traversal_str += f"{start_node.value} - "
            self.in_order_traversed_values(start_node.right)
        return self.traversal_str
    
    def post_order_traversed_values(self, start_node: BtNode):
        if start_node:
            self.post_order_traversed_values(start_node.left)
            self.post_order_traversed_values(start_node.right)
            self.traversal_str += f"{start_node.value} - "
        return self.traversal_str

    def print_tree_values(self, traversal_rule):
        if self.traversal_str:
            self.traversal_str = ""
        if traversal_rule == "preorder":
            return self.pre_order_traversed_values(self.root)
        elif traversal_rule == "inorder":
            return self.in_order_traversed_values(self.root)
        elif traversal_rule == "postorder":
            return self.post_order_traversed_values(self.root)
        else:
            return f"Invalid Traversal Rule provided: {traversal_rule}"

if __name__ == '__main__':
    bt = BinaryTree(1)
    bt.root.left = BtNode(2)
    bt.root.right = BtNode(3)
    bt.root.left.left = BtNode(4)
    bt.root.left.right = BtNode(5)
    bt.root.right.left = BtNode(6)
    bt.root.right.right = BtNode(7)

    print("Printing tree values in preorder traversal rule")
    print(bt.print_tree_values("preorder"))

    print("Printing tree values in inorder traversal rule")
    print(bt.print_tree_values("inorder"))

    print("Printing tree values in postorder traversal rule")
    print(bt.print_tree_values("postorder"))

          