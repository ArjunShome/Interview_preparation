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
        if self.findNode(node):
            # Remove from the existing position
            node = self.findNode(node)
            if node != self.head:
                if node == self.tail:
                    node.prev.next = None
                    self.tail = node.prev
                    node.prev = None
                else:
                    # Release from existing position
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node.next = None
                    node.prev = None
            else:
                return
        # Insert into Head
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
            
    def setTail(self, node):
        # Write your code here.
        if node == self.head:
            # Remove from the existing position
            node.next.prev = None
            self.head = node.next
            node.next = None
            node.prev = None
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
           self.tail = node 
           self.head = node
        

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if node == self.head:
            self.setHead(nodeToInsert)
            return
        if self.findNode(nodeToInsert):
            if self.head == self.tail and self.head == nodeToInsert and self.tail == nodeToInsert:
                self.setHead(nodeToInsert)
            if nodeToInsert == self.tail:
                # Remove from tail
                nodeToInsert.prev.next = None
                self.tail = nodeToInsert.prev
                nodeToInsert.prev = None
            elif nodeToInsert == self.head:
                #Remove rom head
                nodeToInsert.next.prev = None
                self.head = nodeToInsert.next
                nodeToInsert.next = None
            else:
                # Remove from the existing position
                nodeToInsert.prev.next = nodeToInsert.next
                nodeToInsert.next.prev = nodeToInsert.prev
                nodeToInsert.next = None
                nodeToInsert.prev = None
            # Insert at the new position
            if node == self.head:
                # After Head
                node.next.prev = nodeToInsert
                nodeToInsert.next = node.next
                nodeToInsert.prev = node
                node.next = nodeToInsert
            else:
                node.prev.next = nodeToInsert
                nodeToInsert.prev = node.prev
                nodeToInsert.next = node
                node.prev = nodeToInsert
        else:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node
            node.prev = nodeToInsert
        

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if node == self.tail:
            self.setTail(nodeToInsert)
            return
        if self.findNode(nodeToInsert):
            if self.head == self.tail and self.head == nodeToInsert and self.tail == nodeToInsert:
                self.setTail(nodeToInsert)
            if nodeToInsert == self.head:
                # Remove from head
                nodeToInsert.next.prev = None
                self.head = nodeToInsert.next
                nodeToInsert.next = None
            elif nodeToInsert == self.tail:
                # Remove from tail
                nodeToInsert.prev.next = None
                self.tail = nodeToInsert.prev
                nodeToInsert.prev = None
            else:
                # Remove from the existing position
                nodeToInsert.prev.next = nodeToInsert.next
                nodeToInsert.next.prev = nodeToInsert.prev
                nodeToInsert.next = None
                nodeToInsert.prev = None
            # Insert at the new position
            if node == self.tail:
                # After tail
                node.next = nodeToInsert
                nodeToInsert.prev = node
                self.tail = nodeToInsert
            else:
                node.next.prev = nodeToInsert
                nodeToInsert.next = node.next
                nodeToInsert.prev = node
                node.next = nodeToInsert
        else:
            if node.next:
                node.next.prev = nodeToInsert
                nodeToInsert.next = node.next
                nodeToInsert.prev = node
                node.next = nodeToInsert
            else:
                self.setTail(nodeToInsert)
        

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if self.head:
            node = self.head
            pos = 1
            while node:
                if pos != position:
                    node = node.next
                    pos += 1
                else:
                    if pos in (1, 2):
                        self.setHead(nodeToInsert)
                        return
                    elif node == self.tail:
                        self.insertBefore(node, nodeToInsert)
                        return
                    break
        else:
            self.setHead(nodeToInsert)
            return
        if node.prev == nodeToInsert:
            self.insertAfter(node, nodeToInsert)
        else:
            self.insertBefore(node, nodeToInsert)


    def removeNodesWithValue(self, value):
        # Write your code here.
        nodesToRemove = self.findAllNodeWithValue(value)
        while len(nodesToRemove) > 0:
            cur_node = nodesToRemove.pop()
            cur_node = self.findNode(cur_node)
            self.remove(cur_node)
            

    def remove(self, node):
        # Write your code here.
        if node == self.head and node == self.tail:
            node.prev = None
            node.next = None
            self.head = None
            self.tail = None
        elif node == self.tail and node != self.head:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        elif node == self.head and node != self.tail:
            node.next.prev = None
            self.head = node.next
            node.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
        

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node:
            if node.value == value:
                return True
            else:
                node = node.next
        return False
        

    def findAllNodeWithValue(self, value):
        node = self.head
        nodes = []
        while node:
            if node.value == value:
                nodes.append(node)
            if node == self.tail:
                break
            node = node.next
        return nodes
        

    def findNode(self, node):
        cur_node = self.head 
        while cur_node:
            if node == cur_node:
                return cur_node
            else:
                cur_node = cur_node.next

    def display_ll(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.value))
            node = node.next
        
        return print(" -> ".join(nodes))
            
          
            




if __name__ == '__main__':
    node5 = Node(5)
    node4 = Node(4)
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)
    node4_2 = Node(4)
    node6 = Node(6)
    node7 = Node(7)
    node3_2 = Node(3)
    node3_3 = Node(3)

    ll = DoublyLinkedList()
    ll.setHead(node1)
    # ll.insertAfter(node1, node2)
    # ll.insertAfter(node2, node3)
    # ll.insertAfter(node3, node4)
    # ll.insertAfter(node4, node5)
    # ll.insertAfter(node5, node6)
    # ll.insertAfter(node6, node7)
    # ll.insertAtPosition(7, node1)
    # ll.insertAtPosition(1, node1)
    # ll.insertAtPosition(2, node1)
    # ll.insertAtPosition(3, node1)
    # ll.insertAtPosition(4, node1)
    # ll.insertAtPosition(5, node1)
    # ll.insertAtPosition(6, node1)
    ll.remove(node1)
    ll.display_ll()
    