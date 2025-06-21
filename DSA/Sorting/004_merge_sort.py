

def merge(array, low, mid, high):
    temp_arr = []
    left = low
    right = mid + 1

    while (left <= mid and right <= high):
        if array[left] <= array[right]:
            temp_arr.append(array[left])
            left += 1
        else:
            temp_arr.append(array[right])
            right += 1
    
    while left <= mid:
        temp_arr.append(array[left])
        left += 1
    
    while right <= high:
        temp_arr.append(array[right])
        right += 1

    for i in range(low, high + 1):
        array[i] = temp_arr[i - low]
    return array


def merge_sort(array, low, high):
    if low == high:
        return
    mid = int((low + high)/2)
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)
    merge(array, low, mid, high)
    return array


if __name__=="__main__":
    input_array = input("Enter the array of numbers seperated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    input_array = merge_sort(input_array, 0, len(input_array) - 1)
    print(input_array)