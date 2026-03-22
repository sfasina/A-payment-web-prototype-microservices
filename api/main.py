from fastapi import FastAPI
import aio_pika
import os

app = FastAPI(title="Payment API", description="API for payment processing")
RABBITMQ_URL = os.environ["RABBITMQ_URL"]

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/pay")
async def create_payment():
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel()