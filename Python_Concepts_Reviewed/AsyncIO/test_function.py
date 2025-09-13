from time import sleep
import asyncio

def calc_sum(a, b):
    print("Calculating Sum...")
    sleep(3) 
    print("Sum Computed!!")
    return a + b

async def calc_sum_async(a, b):
    print("Calculating Sum...")
    asyncio.sleep(3) 
    print("Sum Computed!!")
    return a + b