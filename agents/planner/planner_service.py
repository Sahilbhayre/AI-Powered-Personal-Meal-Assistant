from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import random

app = FastAPI(title="Planner-Agent")

GOALS = [
    "Plan 3 dinners",
    "Plan 2 healthy lunches",
    "Plan 5 meals for the week",
    "Plan quick vegetarian dishes",
    "Plan protein-rich meals",
]

class PlannerRequest(BaseModel):
    user_id: str
    goal: str = ""          # allow empty for random goal
    constraints: dict = {}

@app.post("/create_task")
def create_task(req: PlannerRequest):
    session_id = str(uuid.uuid4())

    # ✔ RANDOM GOAL if empty
    goal = req.goal or random.choice(GOALS)

    task_payload = {
        "session_id": session_id,
        "goal": goal,
        "constraints": req.constraints
    }

    return {
        "planner": "ok",
        "session_id": session_id,
        "task_payload": task_payload
    }
