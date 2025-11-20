# agents/recommender/product_worker.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Product Worker")

class ProductRequest(BaseModel):
    query: str
    user_id: str

@app.post("/compare")
async def compare(req: ProductRequest):
    # Mocked comparison - replace with real API (Google Search, Amazon API, etc)
    candidates = [
        {"id": "p1", "name": "Pixel 8a", "camera_score": 9, "battery_hours": 24},
        {"id": "p2", "name": "Galaxy A56", "camera_score": 8, "battery_hours": 30}
    ]

    return {
        "worker": "product",
        "candidates": candidates
    }
