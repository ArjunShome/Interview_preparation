class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def removeAtPos(self, position):
    node = self.head
    previous_node = None
    i = 1
    while node:
        if i == position:
            break
        previous_node = node
        node = node.next
    if node == self.head:
        if node.next:
            self.head = node.next
            node.next = None
        else:
            self.head.value = None
            self.head.next = None
    else:
        previous_node.next = node.next
        node.next = None

def removeKthNodeFromEnd(head, k):
    # Write your code here.
    node = head
    lst_node_pos = []
    pos = 1
    while node:
        lst_node_pos.append(pos)
        pos += 1
    pos = lst_node_pos[-k]
    removeAtPos(pos)
