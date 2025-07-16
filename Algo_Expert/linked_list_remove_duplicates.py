

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here. 
    current_node = linkedList
    while current_node is not None:
        next_node = current_node.next
        while next_node is not None and next_node.value == current_node.value:
            next_node = next_node.next   
        current_node.next = next_node
        current_node = next_node
        
    return linkedList


if __name__ == '__main__':
    linked_list = {
    "head": "1",
    "nodes": [
      {"id": "1", "next": "1-2", "value": 1},
      {"id": "1-2", "next": "1-3", "value": 1},
      {"id": "1-3", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 3},
      {"id": "3", "next": "3-2", "value": 4},
      {"id": "3-2", "next": "3-3", "value": 4},
      {"id": "3-3", "next": "4", "value": 4},
      {"id": "4", "next": "5", "value": 5},
      {"id": "5", "next": "5-2", "value": 6},
      {"id": "5-2", "next": None, "value": 6}
    ]
  }