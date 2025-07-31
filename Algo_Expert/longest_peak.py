def longestPeak(array):
    # Write your code here.
    i = 1
    peak = (0, 0)
    
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            _, num = peak
            if num < array[i]:
                peak = i, array[i] 
        i += 1

    left = peak[0]
    right = peak[0]
    peak_len = 1

    if peak[1] != 0:
        while left >= 0  and right <= len(array) - 1:
            gone_left = False
            gone_right = False
            if left > 0 and array[left] > array[left - 1]:
                peak_len += 1
                left -= 1
                gone_left = True
            if right < len(array) - 1 and array[right] > array[right + 1]:
                peak_len += 1
                right += 1
                gone_right = True
            
            if not gone_left and not gone_right:
                break

    return peak_len if peak[1] != 0 else 0




    # while i <= len(array) - 1:
    #     if array[i] > prev:
    #        if increasing:
    #            count += 1
    #        else:
    #            longest = count
    #            count = 1
    #            increasing = True
    #     elif count > 0 and array[i] < prev:
    #         if increasing:
    #             increasing = False
    #         count += 1
    #     elif array[i] == prev:
    #         count = 1
    #     if i == len(array) - 1 and not increasing:
    #         longest = count

    #     prev = array[i]    
    #     i += 1
    # return longest + 1 if longest > 0 else 0

if __name__ == '__main__':
    array = [1,2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    array = [1, 2, 3, 4, 5, 1]
    array = [5, 4, 3, 2, 1, 2, 10, 12]
    print(longestPeak(array))
