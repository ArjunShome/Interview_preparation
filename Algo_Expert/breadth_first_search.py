class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self, array):
        # Write your code here.
        if not self:
            return []
        
        queue = []

        # Add root element to the queue
        queue.append(self)
        self._search_and_store(array, queue)
        return array
    
    def _search_and_store(self, array, queue):
        if len(queue) <= 0:
            return
        # pop from queue
        current = queue[0]
        queue.remove(current)

        # Add elements in to the array
        array.append(current.name)

        # Add Children to the queue
        for child in current.children:
            queue.append(child)
        self._search_and_store(array, queue)

        return array


if __name__ == '__main__':
    root = Node('A')
    root.children = [Node('B'), Node('C'), Node('D')]
    root.children[0].children = [Node('E'), Node('F')]
    root.children[2].children = [Node('G'), Node('H')]
    root.children[0].children[1].children = [Node('I'), Node('J')]
    root.children[2].children[0].children = [Node('K')]

    node_list = []
    print(root.breadthFirstSearch(node_list))
