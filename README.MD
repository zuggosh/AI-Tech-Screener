AI Tech Screener 🤖
A LangGraph-based AI agent for automated resume screening. The application evaluates candidate-job fit and generates either technical interview questions (for high scores) or a polite rejection letter.

Stack: Angular, FastAPI, LangGraph, Pydantic, OpenAI (gpt-4o-mini).

Quick Start
Create a .env file in the backend folder with OPENAI_API_KEY=your_key.

1. Backend
Bash
cd backend
python -m venv .venv
..\.venv\Scripts\activate  # For Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
2. Frontend
In a new terminal:

Bash
cd frontend
npm install
npm run start
UI: http://localhost:4200