from fastapi import FastAPI
import importlib
import sys
import os

# Ensure project root in PYTHONPATH
PROJECT_ROOT = os.path.dirname(__file__)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# CREATE MAIN FASTAPI APP
app = FastAPI(title="AI-Powered Personal Meal Assistant by Team H10")

# helper function
def import_subapp(module_path: str):
    mod = importlib.import_module(module_path)
    if hasattr(mod, "app"):
        return mod.app
    if hasattr(mod, "router"):
        sub = FastAPI()
        sub.include_router(mod.router)
        return sub
    raise ImportError(f"No app or router in {module_path}")

grocery_app = import_subapp("tools.grocery_api")
recipe_app = import_subapp("agents.recommender.recipe_worker")
product_app = import_subapp("agents.recommender.product_worker")
planner_app = import_subapp("agents.planner.planner_service")
executor_app = import_subapp("agents.executor.executor_service")
monitor_app = import_subapp("agents.monitor.monitor_service")

app.mount("/tools/grocery", grocery_app)
app.mount("/recommender/recipe", recipe_app)
app.mount("/recommender/product", product_app)
app.mount("/planner", planner_app)
app.mount("/executor", executor_app)
app.mount("/monitor", monitor_app)

@app.get("/root")
def root():
    return {
        "service": "Life Assistant - Combined Agent",
        "docs": {
            "planner": "/planner/docs",
            "recipe": "/recommender/recipe/docs",
            "product": "/recommender/product/docs",
            "grocery": "/tools/grocery/docs",
            "executor": "/executor/docs",
            "monitor": "/monitor/docs",
        }
    }
