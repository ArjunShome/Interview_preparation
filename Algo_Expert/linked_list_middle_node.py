# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    lst_calc = []
    current_node = linkedList["nodes"][0]
    lst_calc.append(current_node)
    
    while current_node.next is not None:
        next_node = current_node.next
        lst_calc.append(next_node.value)
        current_node = next_node

    mid = len(lst_calc) // 2
    if len(lst_calc) % 2 != 0:
        return lst_calc[mid]
    else:
        return lst_calc[mid + 1]


if __name__ == '__main__':
    linkedList = {
        "head": "1",
        "nodes": [
            {"id": "1", "next": "2", "value": 1},
            {"id": "2", "next": "3", "value": 2},
            {"id": "3", "next": null, "value": 3}
            ]
        }