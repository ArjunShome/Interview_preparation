from test_function import calc_sum_async
import asyncio
from asyncio import TaskGroup
from time import time

async def calc_mul_async(a, b):
    print("Calculating Mul...")
    await asyncio.sleep(3) 
    if a == 0 or b == 0:
        raise ValueError("Cannot multiply by zero")
    print("Mul Computed!!")
    return a * b  

async def main():
    tasks = []
    start_time = time()
    async with TaskGroup() as tg:
        task0 = tg.create_task(calc_mul_async(1,5))
        task1 = tg.create_task(calc_sum_async(1, 5))
        task2 = tg.create_task(calc_sum_async(1, 7))
        task3 = tg.create_task(calc_sum_async(1, 8))
        tasks = [task0, task1, task2, task3]
    end_time = time()

    print(''.join(str(task.result()) for task in tasks))
    
    print(f"Ttoal proces execution took - {end_time - start_time} seconds")




if __name__ =='__main__':
    asyncio.run(main())