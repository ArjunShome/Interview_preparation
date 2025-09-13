import uvicorn
from fastapi import FastAPI
from middlewares import logging_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=logging_middleware)


@app.get(
    path="/api/say_hello/{name}",
    summary="Say Hello to a person",
)
async def say_hello_world(name: str):
    return {"message": f"Hello: {name}"}

@app.get(
    path="/"
)
async def welcome():
    return {"message": "Welcome to Logging Middleware Practice"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
