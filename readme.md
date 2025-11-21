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
🔥 AI-Powered-Personal-Meal-Assistant

A multi-agent system built for the Kaggle × Google 5-Day AI Agent Intensive.

This repository contains a simple, modular multi-agent architecture that runs locally in VS Code using FastAPI microservices.
It is designed for easy testing, screenshots, and creating a short demo video.

🚀 Services (FastAPI Microservices)
Service	File	Port
Planner Agent	agents/planner/planner_service.py	8000
Recipe Worker	agents/recommender/recipe_worker.py	8001
Product Worker	agents/recommender/product_worker.py	8002
Grocery Mock API (Tool)	tools/grocery_api.py	8003
Executor Agent	agents/executor/executor_service.py	8004
Monitor Agent	agents/monitor/monitor_service.py	8005

Each service exposes a REST API with FastAPI and can run independently.

⚙️ Quick Start (Local Setup)
1️⃣ Create virtual environment
```bash
python -m venv venv

2️⃣ Activate environment

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run All Services (6 Terminals)
uvicorn agents.planner.planner_service:app --port 8000 --reload
uvicorn agents.recommender.recipe_worker:app --port 8001 --reload
uvicorn agents.recommender.product_worker:app --port 8002 --reload
uvicorn tools.grocery_api:app --port 8003 --reload
uvicorn agents.executor.executor_service:app --port 8004 --reload
uvicorn agents.monitor.monitor_service:app --port 8005 --reload

🧪 Demo Script

Trigger the full pipeline:

python demo/run_demo_combined.py


This runs:

Planner → Recipe Worker → Executor
and outputs the final meal plan + shopping list.

🙏 Thank You

Thank you for reviewing this project, built with ❤️ for the Kaggle × Google AI Agent Intensive.
