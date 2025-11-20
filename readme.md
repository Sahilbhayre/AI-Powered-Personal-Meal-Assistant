# Life Assistant — Problem Solver (VS Code Project)

This repository contains a small multi-agent scaffold for the Kaggle × Google 5-Day AI Agent Intensive course.
It is intentionally simple so you can run it locally, capture screenshots, and record a short demo video.

## Services (FastAPI microservices)
- Planner Agent: `agents/planner/planner_service.py` (port 8000)
- Recipe Worker: `agents/recommender/recipe_worker.py` (port 8001)
- Product Worker: `agents/recommender/product_worker.py` (port 8002)
- Grocery Mock API (tool): `tools/grocery_api.py` (port 8003)
- Executor Agent: `agents/executor/executor_service.py` (port 8004)
- Monitor Agent: `agents/monitor/monitor_service.py` (port 8005)

## Quick start (local)
1. Create a virtualenv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
