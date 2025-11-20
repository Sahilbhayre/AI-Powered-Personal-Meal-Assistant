# memory/session_service.py
from typing import Dict, Any
import uuid
import time

class InMemorySessionService:
    def __init__(self):
        # This stores active user sessions
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self, user_id: str) -> str:
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            "user_id": user_id,
            "created_at": time.time(),
            "context": [],
            "task_id": None
        }
        return session_id

    def get(self, session_id: str):
        return self.sessions.get(session_id)

    def append_message(self, session_id: str, message: dict):
        """Stores conversation / logs inside session."""
        if session_id in self.sessions:
            self.sessions[session_id]["context"].append(message)

    def set_task(self, session_id: str, task_id: str):
        if session_id in self.sessions:
            self.sessions[session_id]["task_id"] = task_id
