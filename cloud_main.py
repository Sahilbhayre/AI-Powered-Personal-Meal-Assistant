from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Unified AI Agent System")

###########################################################
# 1) Grocery API
###########################################################

class Item(BaseModel):
    item: str
    qty: str

class InventoryResponse(BaseModel):
    inventory: List[Item]

SAMPLE_INVENTORIES = {
    "user1": [
        {"item": "rice", "qty": "2kg"},
        {"item": "eggs", "qty": "6"},
        {"item": "onion", "qty": "1kg"},
    ]
}

@app.get("/grocery/inventory/{user_id}", response_model=InventoryResponse)
def get_inventory(user_id: str):
    inventory = SAMPLE_INVENTORIES.get(user_id, [])
    return {"inventory": inventory}

###########################################################
# 2) Recipe Worker
###########################################################

class RecipeRequest(BaseModel):
    user_id: str
    session_id: str
    constraints: Dict = {}

@app.post("/recipe/recommend")
def recommend_recipe(req: RecipeRequest):
    return {
        "worker": "recipe",
        "proposals": [
            {
                "id": "veg_rice",
                "name": "Vegetable Fried Rice",
                "ingredients": ["rice", "onion"],
                "score": 30
            }
        ]
    }

###########################################################
# 3) Product Worker
###########################################################

class ProductRequest(BaseModel):
    query: str
    user_id: str

@app.post("/product/compare")
def compare_products(req: ProductRequest):
    return {
        "worker": "product",
        "candidates": [
            {"id": "p1", "name": "Pixel 8a"},
            {"id": "p2", "name": "Galaxy A56"}
        ]
    }

###########################################################
# 4) Planner Agent
###########################################################

class PlannerRequest(BaseModel):
    user_id: str
    goal: str
    constraints: Dict

@app.post("/planner/create_task")
def create_task(req: PlannerRequest):
    return {
        "task_id": "task123",
        "payload": {
            "planner_decision": "meal_plan",
            "session_id": "sess001"
        }
    }

###########################################################
# 5) Executor Agent
###########################################################

class ExecutorRequest(BaseModel):
    user_id: str
    session_id: str
    task_payload: Dict
    proposals: Dict

@app.post("/executor/run")
def run_task(req: ExecutorRequest):

    return {
        "status": "complete",
        "meal_plan": [
            {"name": "Vegetable Fried Rice", "ingredients": ["rice", "onion"]}
        ]
    }

###########################################################
# 6) Monitor Agent
###########################################################

class Feedback(BaseModel):
    user_id: str
    task_id: str
    rating: int
    notes: str = ""

@app.post("/monitor/feedback")
def feedback(f: Feedback):
    return {"status": "received"}
