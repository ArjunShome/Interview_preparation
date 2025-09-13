from test_function import calc_sum_async
import asyncio
from asyncio import create_task
from time import time

async def main():
    start_time = time()
    task1 = create_task(calc_sum_async(1, 5))
    task2 = create_task(calc_sum_async(1, 7))
    task3 = create_task(calc_sum_async(1, 7))

    # Sequential excution of tasks not parallel, not very efficient
    # Can use gather here
    
    res1 = await task1
    res2 = await task2
    res3 = await task3
    end_time = time()

    print(res1)
    print(res2)
    print(res3)
    print(f"Ttoal proces execution took - {end_time - start_time} seconds")

asyncio.run(main())