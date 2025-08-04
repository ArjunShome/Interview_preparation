

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    new_intervals = []
    idx = 1

    new_intervals.append(intervals[idx - 1])
    
    while idx < len(intervals):
        prev_interval = new_intervals.pop()
        first_first_el = prev_interval[0]
        first_second_el = prev_interval[1]
        second_first_el = intervals[idx][0]
        second_second_el = intervals[idx][1]
        
        if second_first_el == 0 and second_second_el == 0:
            new_intervals.append(prev_interval)
            idx += 1
            continue
        if first_first_el < second_first_el and first_second_el > second_second_el:
            new_intervals.append(prev_interval)
            idx += 1
            continue
        if (second_first_el > first_first_el and second_first_el <= first_second_el) or (first_second_el >= second_first_el and first_second_el < second_second_el):
            prev_interval[0] = first_first_el
            prev_interval[1] = second_second_el
            new_intervals.append(prev_interval)
        else:
            new_intervals.append(prev_interval)
            new_intervals.append(intervals[idx])
        idx += 1
        
    return new_intervals


if __name__ == '__main__':
    intervals = [[1,2], [3,5], [4,7], [6,8], [9,10]]
    # intervals = [[100,105], [1,104]]
    # intervals = [[1, 22], [-20, 30]]
    print(mergeOverlappingIntervals(intervals))

    # 