

def optimalFreelancing(jobs):
    # Write your code here.
    max_payment = 0
    lst_slots = [False] * 7
    jobs.sort(key=lambda job: job["payment"], reverse=True)

    for i in range(len(jobs)):
        if jobs[i]['deadline'] > 7:
            jobs[i]['deadline'] = 7
        if not lst_slots[jobs[i]['deadline'] - 1]:
            lst_slots[jobs[i]['deadline'] - 1] = True
            max_payment += jobs[i]['payment']
        else:
            j = jobs[i]['deadline'] - 1
            while j >= 0:
                if not lst_slots[j]:
                    lst_slots[j] = True
                    max_payment += jobs[i]['payment']
                    break
                j -= 1
    return max_payment


if __name__ == '__main__':
    jobs = [
        {
        "deadline": 8,
        "payment": 3
        },
        {
        "deadline": 1,
        "payment": 1
        },
        {
        "deadline": 1,
        "payment": 2
        }
    ]
    jobs2 = [
    {
      "deadline": 2,
      "payment": 1
    },
    {
      "deadline": 2,
      "payment": 2
    },
    {
      "deadline": 2,
      "payment": 3
    },
    {
      "deadline": 2,
      "payment": 4
    },
    {
      "deadline": 2,
      "payment": 5
    },
    {
      "deadline": 2,
      "payment": 6
    },
    {
      "deadline": 2,
      "payment": 7
    }
  ]
    jobs3 = [
    {
      "deadline": 1,
      "payment": 1
    },
    {
      "deadline": 2,
      "payment": 1
    }
  ]
    jobs4 = [
    {
      "deadline": 2,
      "payment": 1
    },
    {
      "deadline": 1,
      "payment": 4
    },
    {
      "deadline": 3,
      "payment": 2
    },
    {
      "deadline": 1,
      "payment": 3
    },
    {
      "deadline": 4,
      "payment": 3
    },
    {
      "deadline": 4,
      "payment": 2
    },
    {
      "deadline": 4,
      "payment": 1
    },
    {
      "deadline": 5,
      "payment": 4
    },
    {
      "deadline": 8,
      "payment": 1
    }
  ]
    
    print(optimalFreelancing(jobs3)) 