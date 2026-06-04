# Quiz Game Application

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. XML"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["A. Charles Babbage", "B. Newton", "C. Einstein", "D. Tesla"],
        "answer": "A"
    },
    {
        "question": "Which planet is called the Red Planet?",
        "options": ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"],
        "answer": "C"
    }
]

score = 0

print("===== QUIZ GAME =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== RESULT =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")