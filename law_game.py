import sys

cases = [
    {
        "scenario": "Alex has been caught copying his friend’s homework and submitting it as his own. What legal principle applies here?",
        "options": [
            "Freedom of Expression",
            "Copyright Infringement",
            "Theft of Property",
            "Right to Privacy"
        ],
        "answer": 2
    },
    {
        "scenario": "Jamie posts false rumors about a classmate online. What law could Jamie be violating?",
        "options": [
            "Defamation",
            "Fraud",
            "Trademark Violation",
            "Parental Consent Law"
        ],
        "answer": 1
    },
    {
        "scenario": "Lee hacks into a company’s database and retrieves private information. Which law is most likely to be relevant?",
        "options": [
            "Data Protection Law",
            "Environmental Law",
            "Employment Law",
            "Tax Law"
        ],
        "answer": 1
    },
    {
        "scenario": "Riya downloads a movie from an unauthorized website. What offence has Riya committed?",
        "options": [
            "Patent Infringement",
            "Copyright Infringement",
            "Breach of Contract",
            "Right to Education Violation"
        ],
        "answer": 2
    }
    # Add more cases as needed
]

score = 0

print("Welcome to Legal Eagle: Courtroom Challenge!")
print("Test your knowledge of basic legal principles.\n")

for idx, case in enumerate(cases):
    print(f"Case {idx+1}: {case['scenario']}")
    for i, option in enumerate(case['options'], 1):
        print(f"  {i}. {option}")
    try:
        choice = int(input("Your choice (1-4): "))
    except ValueError:
        print("Invalid input. Game over.")
        sys.exit(1)
    if choice == case["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer was: {case['options'][case['answer'] - 1]}\n")
        score -= 1

print(f"Game Over. Your final score: {score}")
if score == len(cases):
    print("Excellent! You are a legal eagle!")
elif score > 0:
    print("Good job! Review more to become a law master.")
else:
    print("Keep studying! Law takes practice.")
