
def arrayOfProducts(array):
    # Write your code here.
    output_array = [0] * len(array)
    for i in range(len(array)):
        left = i
        right = i
        left_prod = 1
        right_prod = 1
        
        while left >= 0:
            gone_left = False
            if left - 1 >= 0:
                left -= 1
                gone_left = True
            if not gone_left:
                break
            else:
                left_prod = left_prod * array[left]
            
        while right <= len(array) - 1:
            gone_right = False
            if right + 1 <= len(array) - 1:
                right += 1
                gone_right = True
            if not gone_right:
                break
            else:
                right_prod = right_prod * array[right]          
        output_array[i] = left_prod * right_prod
    return output_array


if __name__ == '__main__':
    array = [5,1,4,2]
    print(arrayOfProducts(array))
