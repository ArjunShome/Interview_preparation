from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("app/process_image/")
async def process_image(image_file: UploadFile):
    # Placeholder for image processing logic
    # task_id =
    return {"task_id": 1}


@app.get("/app/task_status/")
async def task_status(task_id: str):
    # Placeholder for task status checking logic
    status = "completed"
    return {"task_id": task_id, "status": status}


if __name__ == "__main__":
    main()
