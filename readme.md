🔥 AI-Powered-Personal-Meal-Assistant

A multi-agent system built for the Kaggle × Google AI Agent Intensive.

This project contains a complete multi-agent architecture (Planner, Recipe Worker, Product Worker, Executor, Monitor, Grocery API) — all running from ONE combined FastAPI app for easy demo, screenshots, and video submission.

🚀 Features

Full multi-agent system in one app

Planner → Recipe Worker → Executor workflow

Custom grocery inventory tool

Long-term memory

Session tracking

FastAPI + Swagger UI

One-command execution

⚙️ Setup
1️⃣ Create virtual environment
```python -m venv venv```

2️⃣ Activate it

Windows:

```venv\Scripts\activate```

3️⃣ Install requirements
```pip install -r requirements.txt```

▶️ Run All Agents (Combined in ONE Terminal)

You only need one command:

```uvicorn combined_app:app --port 8000 --reload```


Everything becomes available at:

```http://localhost:8000/docs```

📡 Available Services (Inside Combined App)
Agent / Tool	Endpoint
Planner Agent	/planner/plan
Recipe Worker	/recommender/recipe
Product Worker	/recommender/product
Grocery API Tool	/inventory/{user_id}
Executor Agent	/executor/execute
Monitor Agent	/monitor/feedback
🧪 Run the Demo

Use the demo script to call all agents automatically:

```python demo/run_demo_combined.py```


The script performs:

✔ Step 1: Planner
✔ Step 2: Recipe Worker
✔ Step 3: Executor
✔ Step 4: Final Meal Plan + Shopping List

🙏 Thank You

Thank you for reviewing this project — built with ❤️ for the Kaggle × Google AI Agent Intensive.
