from database import questions_collection

# Clear existing questions to avoid duplicates (for re-seeding)
questions_collection.delete_many({})

# 20 GRE-style questions (10 verbal, 10 quantitative)
# Difficulties range from 0.1 to 1.0
# Topics: Vocabulary (verbal), Algebra/Geometry (quantitative)
questions = [
    # Verbal (Vocabulary)
    {
        "question_text": "Select the synonym for 'happy'.",
        "options": {"A": "Sad", "B": "Joyful", "C": "Angry", "D": "Tired"},
        "correct_answer": "B",
        "difficulty": 0.1,
        "topic": "Vocabulary",
        "tags": ["synonym", "basic"]
    },
    {
        "question_text": "Select the antonym for 'large'.",
        "options": {"A": "Big", "B": "Huge", "C": "Small", "D": "Vast"},
        "correct_answer": "C",
        "difficulty": 0.15,
        "topic": "Vocabulary",
        "tags": ["antonym", "basic"]
    },
    {
        "question_text": "Select the synonym for 'quick'.",
        "options": {"A": "Slow", "B": "Fast", "C": "Lazy", "D": "Tardy"},
        "correct_answer": "B",
        "difficulty": 0.2,
        "topic": "Vocabulary",
        "tags": ["synonym"]
    },
    {
        "question_text": "Select the antonym for 'ancient'.",
        "options": {"A": "Old", "B": "Modern", "C": "Historic", "D": "Antique"},
        "correct_answer": "B",
        "difficulty": 0.3,
        "topic": "Vocabulary",
        "tags": ["antonym"]
    },
    {
        "question_text": "Select the synonym for 'obfuscate'.",
        "options": {"A": "Clarify", "B": "Confuse", "C": "Reveal", "D": "Expose"},
        "correct_answer": "B",
        "difficulty": 0.8,
        "topic": "Vocabulary",
        "tags": ["synonym", "advanced"]
    },
    {
        "question_text": "Select the antonym for 'mitigate'.",
        "options": {"A": "Alleviate", "B": "Worsen", "C": "Reduce", "D": "Lessen"},
        "correct_answer": "B",
        "difficulty": 0.7,
        "topic": "Vocabulary",
        "tags": ["antonym", "advanced"]
    },
    {
        "question_text": "Select the synonym for 'ubiquitous'.",
        "options": {"A": "Rare", "B": "Everywhere", "C": "Scarce", "D": "Limited"},
        "correct_answer": "B",
        "difficulty": 0.6,
        "topic": "Vocabulary",
        "tags": ["synonym"]
    },
    {
        "question_text": "Select the antonym for 'ephemeral'.",
        "options": {"A": "Temporary", "B": "Permanent", "C": "Fleeting", "D": "Short-lived"},
        "correct_answer": "B",
        "difficulty": 0.9,
        "topic": "Vocabulary",
        "tags": ["antonym", "advanced"]
    },
    {
        "question_text": "Select the synonym for 'laconic'.",
        "options": {"A": "Verbose", "B": "Concise", "C": "Talkative", "D": "Loquacious"},
        "correct_answer": "B",
        "difficulty": 0.85,
        "topic": "Vocabulary",
        "tags": ["synonym", "advanced"]
    },
    {
        "question_text": "Select the antonym for 'prolific'.",
        "options": {"A": "Productive", "B": "Unproductive", "C": "Fertile", "D": "Abundant"},
        "correct_answer": "B",
        "difficulty": 0.75,
        "topic": "Vocabulary",
        "tags": ["antonym"]
    },
    # Quantitative (Algebra/Geometry)
    {
        "question_text": "What is 2 + 3?",
        "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
        "correct_answer": "B",
        "difficulty": 0.1,
        "topic": "Algebra",
        "tags": ["addition", "basic"]
    },
    {
        "question_text": "What is 4 * 5?",
        "options": {"A": "20", "B": "15", "C": "25", "D": "10"},
        "correct_answer": "A",
        "difficulty": 0.2,
        "topic": "Algebra",
        "tags": ["multiplication"]
    },
    {
        "question_text": "Solve for x: x - 7 = 3.",
        "options": {"A": "8", "B": "10", "C": "4", "D": "6"},
        "correct_answer": "B",
        "difficulty": 0.25,
        "topic": "Algebra",
        "tags": ["equation"]
    },
    {
        "question_text": "What is the area of a square with side 4?",
        "options": {"A": "12", "B": "16", "C": "20", "D": "8"},
        "correct_answer": "B",
        "difficulty": 0.3,
        "topic": "Geometry",
        "tags": ["area"]
    },
    {
        "question_text": "Solve for x: 2x + 4 = 10.",
        "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
        "correct_answer": "B",
        "difficulty": 0.4,
        "topic": "Algebra",
        "tags": ["linear equation"]
    },
    {
        "question_text": "What is the perimeter of a rectangle with length 5 and width 3?",
        "options": {"A": "16", "B": "15", "C": "8", "D": "10"},
        "correct_answer": "A",
        "difficulty": 0.35,
        "topic": "Geometry",
        "tags": ["perimeter"]
    },
    {
        "question_text": "Solve the quadratic: x^2 - 5x + 6 = 0 (roots).",
        "options": {"A": "1,6", "B": "2,3", "C": "3,4", "D": "4,5"},
        "correct_answer": "B",
        "difficulty": 0.6,
        "topic": "Algebra",
        "tags": ["quadratic", "advanced"]
    },
    {
        "question_text": "What is sin(90 degrees)?",
        "options": {"A": "0", "B": "1", "C": "0.5", "D": "-1"},
        "correct_answer": "B",
        "difficulty": 0.5,
        "topic": "Geometry",
        "tags": ["trigonometry"]
    },
    {
        "question_text": "Find the derivative of x^2.",
        "options": {"A": "x", "B": "2x", "C": "x^2", "D": "2"},
        "correct_answer": "B",
        "difficulty": 0.9,
        "topic": "Algebra",
        "tags": ["calculus", "advanced"]
    },
    {
        "question_text": "What is the probability of rolling a 6 on a die?",
        "options": {"A": "1/2", "B": "1/6", "C": "1/3", "D": "1/4"},
        "correct_answer": "B",
        "difficulty": 0.45,
        "topic": "Algebra",
        "tags": ["probability"]
    }
]

questions_collection.insert_many(questions)
print("Seeded 20 questions successfully.")