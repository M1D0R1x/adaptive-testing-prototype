import numpy as np
from scipy.optimize import minimize_scalar
from database import questions_collection, sessions_collection
from bson.objectid import ObjectId
from typing import Dict, List, Any


def logistic(theta: float, b: float) -> float:
    return 1 / (1 + np.exp(-(theta - b)))


def select_next_question(session_id: str) -> Dict[str, Any]:
    session = sessions_collection.find_one({"session_id": session_id})
    if not session:
        raise ValueError("Session not found")

    asked_ids = session.get("questions_asked", [])
    ability = session.get("current_ability", 0.5)

    questions = list(
        questions_collection.find({"_id": {"$nin": asked_ids}})
    )

    if not questions:
        raise ValueError("No more questions available")

    # Choose question with highest information at ability level
    def information(q):
        b = q["difficulty"]
        p = logistic(ability, b)
        return p * (1 - p)

    best = max(questions, key=information)

    return best


def update_ability(session_id: str) -> float:
    session = sessions_collection.find_one({"session_id": session_id})
    if not session:
        raise ValueError("Session not found")

    answers = session.get("answers", [])

    if not answers:
        return 0.5

    question_ids = [ObjectId(a["question_id"]) for a in answers]

    questions = {
        str(q["_id"]): q
        for q in questions_collection.find({"_id": {"$in": question_ids}})
    }

    def neg_log_likelihood(theta: float) -> float:
        ll = 0
        for ans in answers:
            q = questions.get(ans["question_id"])
            if not q:
                continue

            b = q["difficulty"]
            p = logistic(theta, b)

            if ans["correct"]:
                ll += np.log(p + 1e-9)
            else:
                ll += np.log(1 - p + 1e-9)

        return -ll

    result = minimize_scalar(
        neg_log_likelihood,
        bounds=(0.0, 1.0),
        method="bounded",
    )

    if not result.success:
        raise ValueError("Ability optimization failed")

    return float(result.x)