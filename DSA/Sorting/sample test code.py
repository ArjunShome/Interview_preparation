

# class QuickSort:
#     def quick_sort(self, array, low, high):
#         if low < high:
#             pIndex = self._get_partition_index(array, low, high)
#             self.quick_sort(array, low, pIndex - 1)
#             self.quick_sort(array, pIndex + 1, high)
#         return array
    
#     def _get_partition_index(self, array, low, high):
#         pivot = array[low]
#         i = low
#         j = high
#         while(i < j):
#             while(array[i] <= pivot and i <= high-1):
#                 i+=1
                
#             while(array[j] > pivot and j >= low+1):
#                 j-=1
                
#             if(i < j ):
#                 self._swap(array, i, j)
#         self._swap(array, low, j)
#         return j
    
#     def _swap(self, array, low, high):
#         temp = array[low]
#         array[low]=array[high]
#         array[high] = temp

class MergeSort:
    def merge_sort(self, array, low, high):
        if low == high:
            return
        mid = int((low + high) / 2)
        self.merge_sort(array, low, mid)
        self.merge_sort(array, mid+1, high)
        self.merge(array, low, mid, high)
        return array

    def merge(self, array, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        while(left <= mid and right <= high):
            if array[left] <= array[right]:
                temp.append(array[left])
                left += 1
            else:
                temp.append(array[right])
                right += 1
        
        while(left <= mid):
            temp.append(array[left])
            left +=1

        while(right <= high):
            temp.append(array[right])
            right += 1

        for i in range(low,high+1):
            array[i] = temp[i - low]

if __name__ == "__main__":
    user_input = input("Enter the numbers seperated by comma to sort: ")
    list_array = [int(num) for num in user_input.split(",")]
    ms = MergeSort()
    sorted_array = ms.merge_sort(list_array, 0, len(list_array)-1)
    
    print(sorted_array)