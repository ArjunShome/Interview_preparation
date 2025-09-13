
from fastapi import Request
from log import logger
import time
import math


async def logging_middleware(request: Request, call_next):
    logger.info(f"Request URL: {request.url}")
    logger.info(f"Request Method: {request.method}")
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    elapsed_time_str = f"{minutes} minutes {math.ceil(seconds)} seconds"
    logger.info(f"Request processed in: {elapsed_time_str}")
    response.headers["X-Process-Time"] = elapsed_time_str
    return response