from test_function import calc_sum
import asyncio

async def main():
    print(calc_sum(1, 2))

result = asyncio.run(main())


