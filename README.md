# AI Adaptive Diagnostic Engine

This project implements a **1-Dimensional Adaptive Testing System** using Item Response Theory (IRT).  
The system dynamically selects questions based on a student's estimated ability and produces an AI-generated study plan.

The objective is to simulate the core mechanics used in real adaptive exams such as **GRE, GMAT, and Duolingo English Test**.

---

# Architecture

Backend
- FastAPI
- Python
- MongoDB

Frontend
- Streamlit

AI
- Google Gemini API

---

# Project Structure

adaptive.py  
Core adaptive algorithm and ability estimation.

app.py  
FastAPI backend providing adaptive test endpoints.

database.py  
MongoDB connection and collections.

seed.py  
Seeds GRE-style question bank.

llm.py  
Gemini integration for generating study plans.

frontend.py  
Streamlit UI for running the adaptive test.

---

# Adaptive Algorithm

The system uses a **1-parameter IRT (Rasch Model)**.

Probability of correct answer:

P(correct) = 1 / (1 + e^(θ - b))

Where:

θ = student ability  
b = question difficulty

Workflow:

1. Student begins with ability θ = 0.5
2. System selects question maximizing information at θ
3. After response, ability is re-estimated using **Maximum Likelihood Estimation**
4. The process repeats for 10 questions
5. Weak topics are extracted
6. Gemini generates a personalized learning plan

---

# MongoDB Schema

Questions Collection


{
question_text: str
options: dict
correct_answer: str
difficulty: float
topic: str
tags: list
}


UserSessions Collection


{
session_id: str
current_ability: float
questions_asked: list
answers: list
}


Indexes:
- difficulty
- session_id

---

# API Endpoints

POST /start_session  
Creates a new testing session.

GET /next_question/{session_id}  
Returns next adaptive question.

POST /submit_answer/{session_id}  
Submits answer and updates ability estimate.

GET /study_plan/{session_id}  
Returns AI-generated study plan after test completion.

---

# Setup Instructions

Install dependencies


pip install -r requirements.txt


Create `.env`


MONGO_URI=your_mongo_uri

GEMINI_API_KEY=your_key


Seed questions


python seed.py


Start backend


uvicorn app:app --reload


Start frontend


streamlit run frontend.py


---

# AI Log

AI tools used:
- ChatGPT
- Cursor

AI was used to accelerate:

- adaptive algorithm scaffolding
- FastAPI endpoint structure
- Gemini integration
- debugging MongoDB TLS errors

Manual engineering work included:

- refining IRT likelihood optimization
- designing Mongo schema
- improving LLM prompt quality

---

# Key Design Decisions

Adaptive selection uses **information maximization** rather than naive difficulty matching.

Ability estimation uses **MLE optimization**.

LLM generation focuses on **specific actionable study steps** instead of generic advice.

---

# Future Improvements

- multi-dimensional IRT
- question discrimination parameter
- response time modeling
- question exposure control