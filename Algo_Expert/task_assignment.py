
def taskAssignment(k, tasks):
    # Write your code here.
    tasks_dummy = sorted(tasks)
    final_pairs = []
    mapping = {}

    for idx, val in enumerate(tasks):
        if val in mapping:
            mapping[val].append(idx) 
        else:
            mapping[val] = [idx]

    i = 0
    j = len(tasks) - 1

    while i <= j:
        final_pairs.append([mapping[tasks_dummy[i]].pop(), mapping[tasks_dummy[j]].pop()])
        i += 1
        j -= 1
        
    return final_pairs


if __name__ == '__main__':
    k = 3
    tasks = [1,3,5,3,1,4]
    print(taskAssignment(k, tasks))