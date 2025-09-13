from test_function import calc_sum_async
import asyncio
from asyncio import create_task, gather
from time import time

async def calc_mul_async(a, b):
    print("Calculating Mul...")
    await asyncio.sleep(3) 
    if a == 0 or b == 0:
        raise ValueError("Cannot multiply by zero")
    print("Mul Computed!!")
    return a * b    

async def main():
    start_time = time()
    results = await gather(calc_sum_async(1, 5), calc_sum_async(1, 7), calc_mul_async(0,5), calc_sum_async(1, 7))
    # results = await gather(calc_mul_async(12,5) ,calc_sum_async(1, 5), calc_sum_async(1, 7), calc_sum_async(1, 7))
    end_time = time()

    for result in results:
        print(result)
    print(f"Ttoal proces execution took - {end_time - start_time} seconds")

asyncio.run(main())