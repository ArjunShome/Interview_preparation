Async Image Processing Pipeline with FastAPI + Celery + RabbitMQ + Redis

📌 Goal

Build an API where users upload an image, and instead of processing immediately (blocking), you queue the job with Celery → RabbitMQ.
While the task runs asynchronously, store status in Redis, and allow the user to poll status or retrieve the processed image later.

⸻

⚙️ Architecture Flow
![img.png](doc_img/img.png)


![img_1.png](doc_img/img_1.png)


🛠️ Features to Implement

![img_2.png](doc_img/img_2.png)

🚀 Bonus: Real DevOps Behavior
	•	Use Docker Compose to spin:
	•	fastapi-app
	•	celery-worker
	•	rabbitmq
	•	redis
	•	Track Celery dashboard via Flower UI
	•	Optionally, set retry policy with exponential backoff

![img_3.png](doc_img/img_3.png)

![img_4.png](doc_img/img_4.png)


Using UV package manager here