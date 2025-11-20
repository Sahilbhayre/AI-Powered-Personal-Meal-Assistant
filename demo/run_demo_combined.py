# demo/run_demo_combined.py
import httpx
import json
import sys

BASE = "http://localhost:8000"

PLANNER = f"{BASE}/planner/create_task"
RECIPE = f"{BASE}/recommender/recipe/recommend"
EXECUTE = f"{BASE}/executor/execute"

def main():
    print("\n=== STEP 1: Creating task ===")
    payload = {
        "user_id": "user1",
        "goal": "Plan 3 dinners this week under 600",
        "constraints": {"budget": 600, "diet": "vegetarian"}
    }

    r = httpx.post(PLANNER, json=payload, timeout=10.0)
    if r.status_code != 200:
        print("Planner error:", r.status_code, r.text)
        sys.exit(1)

    planner_resp = r.json()
    print("\nPlanner Response:")
    print(json.dumps(planner_resp, indent=2))

    # Robust session_id & task_payload extraction supporting multiple planner formats
    session_id = None
    task_payload = None

    # new format: planner returns "task_payload"
    if "task_payload" in planner_resp:
        task_payload = planner_resp["task_payload"]
        session_id = task_payload.get("session_id") or planner_resp.get("session_id")
    # older format: planner returned {"payload": {...}}
    elif "payload" in planner_resp:
        task_payload = planner_resp["payload"]
        session_id = task_payload.get("session_id") or planner_resp.get("session_id")
    # fallback: top-level session_id
    elif "session_id" in planner_resp:
        session_id = planner_resp["session_id"]
        task_payload = planner_resp.get("task_payload", {})
    else:
        print("Planner response missing session info:", planner_resp)
        sys.exit(1)

    if not session_id:
        print("Could not determine session_id from planner response. Exiting.")
        sys.exit(1)

    print(f"\nUsing session_id: {session_id}")

    print("\n=== STEP 2: Calling Recipe Worker ===")
    r2 = httpx.post(RECIPE, json={
        "user_id": "user1",
        "session_id": session_id,
        "constraints": {}
    }, timeout=10.0)

    if r2.status_code != 200:
        print("Recipe worker error:", r2.status_code, r2.text)
        sys.exit(1)

    print("\nRecipe Worker Response:")
    print(json.dumps(r2.json(), indent=2))
    proposals = r2.json().get("proposals", [])

    print("\n=== STEP 3: Calling Executor ===")
    exec_payload = {
        "user_id": "user1",
        "session_id": session_id,
        "task_payload": task_payload or {},
        "proposals": {"recipe": proposals}
    }

    r3 = httpx.post(EXECUTE, json=exec_payload, timeout=10.0)
    if r3.status_code != 200:
        print("Executor error:", r3.status_code, r3.text)
        sys.exit(1)

    print("\nExecutor Response (Final Meal Plan):")
    print(json.dumps(r3.json(), indent=2))

    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
