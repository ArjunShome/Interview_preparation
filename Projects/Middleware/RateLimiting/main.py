import time
import asyncio
import uvicorn

from fastapi import FastAPI, Request
from log import logger
from middlewares import RateLimiter

app = FastAPI()


app.add_middleware(RateLimiter)

@app.get(path="/api/v1/get_data")
async def get_data():
    logger.info("Getting data from the server")
    await asyncio.sleep(0.2)
    data = {
        "id": 1,
        "name": "Arjun Shome",
        "description": "This is a sample data response",
        "mobile": 9007172411,
        "email_id": "arjunshome111@gmail.com"
    }
    logger.info("Retrieved data from the server")
    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)