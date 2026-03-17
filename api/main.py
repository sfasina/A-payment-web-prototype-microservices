from fastapi import FastAPI

app = FastAPI(title="Payment API", description="API for payment processing")

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Payment API is running"}