# Write a Python function using asyncio that:
# 	•	Defines an asynchronous function fetch_data(id, delay) that simulates fetching data by await asyncio.sleep(delay) and then prints:
# "Fetched data for ID {id} after {delay} seconds"
# 	•	Runs three such tasks concurrently with different delays:
# 	•	id=1, delay=2 seconds
# 	•	id=2, delay=1 second
# 	•	id=3, delay=3 seconds
# 	•	Ensure that the total execution time is around 3 seconds, not the sum of all delays.


import asyncio
import time
from asyncio import TaskGroup


async def fetch_data(id, delay):
    await asyncio.sleep(delay)
    return f"Fetched data for ID {id} after {delay} seconds"


async def main():
    start_time = time.time()
    async with TaskGroup() as td:
        task_1 = td.create_task(fetch_data(1, 2))
        task_2 = td.create_task(fetch_data(2, 1))
        task_3 = td.create_task(fetch_data(3, 3))
    tasks = [task_1, task_2, task_3]
    
    for task in tasks:
        print(task.result())
    end_time = time.time()

    diff = end_time - start_time
    print(f"Time taken is {diff}")


if __name__=="__main__":
    asyncio.run(main())