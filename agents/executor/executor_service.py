from fastapi import FastAPI
from pydantic import BaseModel
from memory.memory_bank import MemoryBank
import httpx
import random

app = FastAPI(title="Executor-Agent")
memory = MemoryBank()

class ExecuteRequest(BaseModel):
    user_id: str
    session_id: str
    task_payload: dict
    proposals: dict

@app.post("/execute")
async def execute(req: ExecuteRequest):

    recipe_proposals = req.proposals.get("recipe", [])

    # ✔ RANDOM selection from proposals
    selected = random.choice(recipe_proposals) if recipe_proposals else None

    deliverable = {
        "meals": [p["name"] for p in recipe_proposals],
        "selected": selected,
        "shopping_list": []
    }

    # ✔ get inventory (combined app)
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"http://localhost:8000/tools/grocery/inventory/{req.user_id}",
            timeout=10.0
        )
        inventory = r.json().get("inventory", [])

    inventory_items = [i["item"] for i in inventory]

    # ✔ compute missing ingredients
    if selected:
        missing = [
            ing for ing in selected.get("ingredients", [])
            if ing not in inventory_items
        ]
        deliverable["shopping_list"] = missing

    # ✔ Save to long-term memory
    memory.update_user_memory(req.user_id, {"last_plan": deliverable})

    return {
        "status": "ok",
        "deliverable": deliverable
    }
