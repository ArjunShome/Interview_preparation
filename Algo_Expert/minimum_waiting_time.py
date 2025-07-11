def minimumWaitingTime(queries):
    # Write your code here.
    total_time = 0
    queries = sorted(queries)
    
    for i in range(len(queries)):
        total_time += ((len(queries) - 1) - i) * queries[i] 

    return total_time


if __name__ == '__main__':
    queries = [3, 2, 1, 2, 6]
    [1,2,2,3,6]
    [0,1,1+2, 1+2+2, 1+2+2+3]
    print(minimumWaitingTime(queries)) 