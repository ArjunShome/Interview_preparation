from test_function import calc_sum, calc_sum_async
import asyncio

async def main():
    print(await calc_sum_async(1, 2))

asyncio.run(main())