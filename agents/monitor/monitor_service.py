# agents/monitor/monitor_service.py
from fastapi import FastAPI
from pydantic import BaseModel
from memory.memory_bank import MemoryBank
import logging

app = FastAPI(title="Monitor-Agent")
memory = MemoryBank()
logging.basicConfig(level=logging.INFO)

class Feedback(BaseModel):
    user_id: str
    task_id: str
    rating: int
    notes: str = ""

@app.post("/feedback")
def feedback(f: Feedback):
    # Log the feedback
    logging.info(f"Feedback received: {f}")

    # Load past memory
    user_mem = memory.get_user_memory(f.user_id)

    # Append new feedback
    feedbacks = user_mem.get("feedbacks", [])
    feedbacks.append({
        "task_id": f.task_id,
        "rating": f.rating,
        "notes": f.notes
    })

    # Save updated feedback history
    memory.update_user_memory(f.user_id, {"feedbacks": feedbacks})

    return {"status": "received"}
