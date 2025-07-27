# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head:
                if self.head != node:
                    if self.containsNode(node.value):
                        if node == self.tail:
                            self.tail = node.prev
                            self.tail.next = None
                            node.prev = None
                            node.next = self.head
                            self.head.prev = node
                            self.head = node
                        else:
                            node.prev.next = node.next
                            node.next.prev = node.prev
                            self.head.prev = node
                            node.next = self.head
                            node.prev = None
                            self.head = node
                    else:
                        self.head.prev = node
                        node.next = self.head
                        self.head = node
        else:
            self.head = node
            self.tail = node

    def setTail(self, node):
        # Write your code here.
        if self.head:
            if self.head == self.tail and self.head != node:
                self.head.next = node
                node.prev = self.head
                self.tail = node
            else:
                if not self.containsNode(node):
                    node.prev = self.tail
                    self.tail.next = node
                    self.tail = node 
                else:
                    if self.head == node:
                        node.next.prev = None
                        self.head = node.next
                        node.prev = self.tail
                        self.tail.next = node
                        self.tail = node
                        node.next = None
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        node.prev = self.tail
                        node.next = None
                        self.tail.next = node
                        self.tail = node
        else:
            self.head = node
            self.tail = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if self.containsNode(nodeToInsert.value):
            if node == self.head:
                node.prev = nodeToInsert
                nodeToInsert.prev.next = nodeToInsert.next
                nodeToInsert.next.prev = nodeToInsert.prev
                nodeToInsert.next = node
                nodeToInsert.prev = None
                self.head = nodeToInsert
            elif nodeToInsert == self.tail:
                self.tail = nodeToInsert.prev
                self.tail.next = None
                nodeToInsert.prev = node.prev
                nodeToInsert.next = node
                if nodeToInsert.prev:
                    nodeToInsert.prev.next = nodeToInsert
                node.prev = nodeToInsert
            else:
                nodeToInsert.prev.next = nodeToInsert.next
                nodeToInsert.next.prev = nodeToInsert.prev
                nodeToInsert.prev = node.prev
                nodeToInsert.next = node
                nodeToInsert.prev.next = nodeToInsert
                nodeToInsert.next.prev = nodeToInsert
        else:
            if node == self.head:
                node.prev = nodeToInsert
                nodeToInsert.next = node
                self.head = nodeToInsert
            else:    
                nodeToInsert.next = self.node
                nodeToInsert.prev = node.prev
                node.prev.next = nodeToInsert
                node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if self.containsNode(nodeToInsert):
            if node == self.tail:
                nodeToInsert.prev.next = nodeToInsert.next
                nodeToInsert.next.prev = nodeToInsert.prev
                self.tail.next = nodeToInsert
                nodeToInsert.prev = self.tail
                nodeToInsert.next = None
                self.tail = nodeToInsert
                self.tail.next = None
            elif node == self.head:
                nodeToInsert.prev.next = nodeToInsert.next
                nodeToInsert.next.prev = nodeToInsert.prev
                nodeToInsert.next = node.next
                nodeToInsert.next.prev = nodeToInsert
                nodeToInsert.prev = node
                node.next = nodeToInsert
            else:
                if nodeToInsert == self.head:
                    nodeToInsert.next.prev = None
                    self.head = nodeToInsert.next
                    node.next.prev = nodeToInsert
                    nodeToInsert.prev = node
                    nodeToInsert.next = node.next
                    node.next = nodeToInsert
                else:
                    nodeToInsert.prev.next = nodeToInsert.next
                    nodeToInsert.next.prev = nodeToInsert.prev
                    node.next.prev = nodeToInsert
                    nodeToInsert.prev = node
                    nodeToInsert.next = node.next
                    node.next = nodeToInsert
        else:
            if node == self.tail:
                self.tail.next = nodeToInsert
                nodeToInsert.prev = self.tail
                self.tail = nodeToInsert
                self.tail.next = None
            else:
                node.next.prev = nodeToInsert
                nodeToInsert.prev = node
                nodeToInsert.next = node.next
                node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        node = self.head
        if node:
            i = 1
            while node:
                if i == position:
                    break
                node = node.next
                i += 1
            if node == self.head:
                node.prev = nodeToInsert
                nodeToInsert.next = node
                self.head = nodeToInsert
            else:
                nodeToInsert.next = node
                node.prev.next = nodeToInsert
                nodeToInsert.prev = node.prev
                node.prev = nodeToInsert
        else:
            self.head = nodeToInsert
            self.tail = nodeToInsert


    def removeNodesWithValue(self, value):
        # Write your code here.
        delete_nodes = self.find_all_nodes_with_value(value)
        for delete_node in delete_nodes:
            if delete_node == self.head:
                delete_node.next.prev = None
                self.head = delete_node.next
                delete_node.next = None
            elif delete_node == self.tail:
                delete_node.prev.next = None
                self.tail = delete_node.prev
            else:
                delete_node.next.prev = delete_node.prev
                delete_node.prev.next = delete_node.next

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head.next.prev = None
            node.next = None
            self.head = self.head.next
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
    
    def containsNode(self, node):
        # Write your code here.
        node = self.head
        while node:
            if node == node:
                return True
            node = node.next

    def display_values(self):
        node = self.head
        node_lst = []
        while node:
            node_lst.append(f"{node.value}")
            node = node.next
        print(" <--> ".join(node_lst))

    def find_node_with_value(self, value):
        node = self.head
        if not self.containsNodeWithValue(value):
            return
        while node:
            if node.value == value:
                return node
            node = node.next
        return None

    def find_all_nodes_with_value(self, value):
        lst = []
        node = self.head
        while node:
            if node.value == value:
                lst.append(node)
            node = node.next
        return lst    
            




if __name__ == '__main__':
    # node1 = Node(5)
    node2 = Node(4)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(1)
    # node6 = Node(4)
    # node7 = Node(6)
    # node8 = Node(3)
    # node9 = Node(3)

    ll = DoublyLinkedList()
    # ll.setHead(node1)
    # ll.display_values()
    # ll.setHead(node2)
    # ll.display_values()
    # ll.setHead(node3)
    # ll.display_values()
    # ll.setHead(node4)
    # ll.display_values()
    # ll.setHead(node5)
    # ll.display_values()
    # ll.setHead(node2)
    # ll.display_values()
    ll.setHead(node5)
    # ll.setTail(node5)
    ll.insertAfter(node5, node4)
    ll.insertAfter(node4, node3)
    ll.insertAfter(node3, node2)
    ll.insertAfter(node4, node5)
    ll.insertBefore(node3, node2)
    # ll.display_values()
    # ll.insertBefore(node7, node3)
    # ll.display_values()
    # ll.insertBefore(node5, node4)
    # ll.insertBefore(node4, node3)
    # ll.insertBefore(node3, node2)
    # ll.display_values()
    # ll.setHead(node5)
    # ll.display_values()
    # ll.insertAtPosition(1, node9)
    # ll.display_values()
    # ll.removeNodesWithValue(3)
    # ll.display_values()
    # ll.remove(node4)
    # ll.display_values()
    # print(ll.containsNodeWithValue(5))
    ll.display_values()