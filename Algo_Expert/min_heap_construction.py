# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.  
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array) -> list:
        # Write your code here.
        first_parent_idx = (len(array)) - 1 // 2
        for cur_idx in reversed(range(first_parent_idx)):
            self.siftDown(cur_idx, len(array) - 1, array)
        return array

    def siftDown(self, cur_idx, end_idx, heap):
        # Write your code here.
        child_one_idx = (cur_idx * 2) + 1
        while child_one_idx <= end_idx:
            child_two_idx = (cur_idx * 2) + 2 if (cur_idx *2) + 1 < end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            
            if heap[idx_to_swap]  < heap[cur_idx]:
                self.swap(cur_idx, idx_to_swap, self.heap)
                cur_idx = idx_to_swap
                child_one_idx = cur_idx * 2 + 1
            else:
                break 
        

    def siftUp(self, cur_idx, heap):
        # Write your code here.
        parent_idx = (cur_idx - 1) // 2
        parent_val = self.heap[parent_idx]
        while cur_idx > 0 and self.heap[cur_idx] < parent_val:
            self.swap(cur_idx, parent_idx, self.heap)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2
            parent_val = self.heap[parent_idx]
        
    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
       

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]



if __name__ == '__main__':
    array = [48,12,24,7,8,-5,24,391,24,56,2,6,8,41]
    heap = MinHeap(array)