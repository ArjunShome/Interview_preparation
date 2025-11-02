from fastapi import FastAPI
from model import StoredNames, Name, Names
import uvicorn

app = FastAPI()

stored_names = StoredNames()

@app.post("/app/store_name")
async def store_name(name: Name):
    stored_names.add_names(name)
    return {"message": "Name stored successfully."}


@app.get("/app/get_names", response_model=Names)
async def get_names():
    names = stored_names.get_names()
    return {"names": names}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

