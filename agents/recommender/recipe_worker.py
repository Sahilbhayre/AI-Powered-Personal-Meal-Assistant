from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import random
from tools.recipe_scorer import get_scored_recipes

app = FastAPI(title="Recipe Worker")

class RecipeRequest(BaseModel):
    user_id: str
    session_id: str
    constraints: dict

@app.post("/recommend")
async def recommend(req: RecipeRequest):

    # ✔ Use combined app grocery endpoint
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"http://localhost:8000/tools/grocery/inventory/{req.user_id}",
            timeout=10.0
        )
        inventory = r.json().get("inventory", [])

    inventory_items = [i["item"] for i in inventory]

    # ✔ dynamic scoring from tool
    scored = get_scored_recipes(inventory_items)

    # ✔ RANDOM number of proposals (2–4)
    count = random.randint(2, 4)

    proposals = scored[:count]
    random.shuffle(proposals)  # randomize order

    return {
        "worker": "recipe",
        "proposals": proposals
    }
