from fastapi import FastAPI
import random

app = FastAPI(title="Mock Grocery Inventory API")

ITEMS = [
    "rice", "milk", "eggs", "onion", "potato", "bread", "tomato",
    "cheese", "pasta", "chicken", "apple", "banana", "yogurt", "beans"
]

@app.get("/")
def root():
    return {"message": "Grocery API running"}

@app.get("/inventory/{user_id}")
def get_inventory(user_id: str):
    # Random sample of 5–8 ingredients
    sample_size = random.randint(5, 8)
    sample = random.sample(ITEMS, sample_size)

    inventory = [{"item": item, "qty": "1"} for item in sample]

    return {"user_id": user_id, "inventory": inventory}
