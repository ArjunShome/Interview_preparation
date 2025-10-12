"""
Write a Python program using the multiprocessing module that:
	•	Defines a function calculate_square(n) that prints the process ID and returns the square of the number.
	•	Uses a Process Pool (multiprocessing.Pool) to compute the squares of the numbers [1, 2, 3, 4, 5] in parallel.
	•	Collects and prints the results as a list.
	•	Ensures that the multiprocessing block runs only when __name__ == "__main__" to avoid infinite process spawning.
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import os
import time

def calculate_square(n):
    p_id = os.getpid()
    time.sleep(1)
    return n * n, p_id

if __name__=="__main__":
    start = time.time()
    output = []
    with ProcessPoolExecutor(max_workers=5) as mp:
        futures = [mp.submit(calculate_square, n) for n in [1, 2, 3, 4, 5]]
        for f in as_completed(futures):
            square, p_id = f.result()
            output.append((square, p_id))
            print(f"Proces ID -> {p_id}, Square -> {square}")
    end = time.time()
    diff = end - start
    print(f"With multi Processing - {diff}")
    print(output)
    
    start_wmp = time.time()
    print(calculate_square(1))
    print(calculate_square(2))
    print(calculate_square(3))
    print(calculate_square(4))
    print(calculate_square(5))
    end_wmp = time.time()
    diff_wmp = end_wmp - start_wmp
    print(f"Without Multi processing - {diff_wmp}")
            

