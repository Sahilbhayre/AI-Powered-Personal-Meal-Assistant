# memory/memory_bank.py
import json
from typing import Dict, Any
import os

MEMORY_FILE = "memory_store.json"

class MemoryBank:
    def __init__(self, filename: str = MEMORY_FILE):
        self.filename = filename
        # Create empty JSON file if not exists
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def _read(self) -> Dict[str, Any]:
        with open(self.filename, "r") as f:
            return json.load(f)

    def _write(self, data: Dict[str, Any]):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def get_user_memory(self, user_id: str):
        data = self._read()
        return data.get(user_id, {})

    def update_user_memory(self, user_id: str, kv: Dict[str, Any]):
        data = self._read()
        user_mem = data.get(user_id, {})
        user_mem.update(kv)
        data[user_id] = user_mem
        self._write(data)
