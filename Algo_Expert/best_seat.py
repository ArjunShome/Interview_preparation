

def bestSeat(seats):
    # Write your code here.
    best_seat = -1
    longest = 0
    i = 0

    while i < len(seats):
        if seats[i] != 0:
            i += 1
            continue
        j = i
        while j < len(seats) and seats[j] == 0:
            j += 1
        free_seats = j - i
        if free_seats > longest:
            best_seat = (i + j - 1) // 2 
            longest = free_seats
        i = j
    
    return best_seat




if __name__ == '__main__':
    seats = [1, 0 , 1, 0, 0, 0, 1]
    seats = [1, 0, 1]
    seats = [1, 0 , 0, 1, 0, 0, 1]
    print(bestSeat(seats))