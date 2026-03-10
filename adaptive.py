import numpy as np
from scipy.optimize import minimize_scalar
from database import questions_collection, sessions_collection
from bson.objectid import ObjectId
from typing import Dict, Any
import random


def logistic(theta: float, b: float) -> float:
    return 1 / (1 + np.exp(-(theta - b)))


def information(theta: float, b: float) -> float:
    p = logistic(theta, b)
    return p * (1 - p)


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

    # compute information score
    scored = []

    for q in questions:
        b = q["difficulty"]
        info = information(ability, b)

        # slight randomness to avoid identical sequence
        info = info + random.uniform(0, 0.02)

        scored.append((info, q))

    scored.sort(reverse=True, key=lambda x: x[0])

    return scored[0][1]


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

    def neg_log_likelihood(theta: float):

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

    new_theta = float(result.x)

    # smoothing to prevent extreme jumps
    previous = session.get("current_ability", 0.5)

    smoothed = 0.7 * previous + 0.3 * new_theta

    return smoothed