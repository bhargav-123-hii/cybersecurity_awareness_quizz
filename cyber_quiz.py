# Cybersecurity Awareness Quiz in Python

# List of quiz questions, options, and correct answers
questions = [
    {
        "question": "1. What is the most secure way to store a password?",
        "options": ["A. Plain text", "B. Hashed and salted", "C. Excel file", "D. Email"],
        "answer": "B"
    },
    {
        "question": "2. Which one is a type of malware?",
        "options": ["A. VPN", "B. Firewall", "C. Ransomware", "D. HTTPS"],
        "answer": "C"
    },
    {
        "question": "3. What should you check before clicking a link?",
        "options": ["A. Design", "B. Domain name", "C. Font", "D. Color"],
        "answer": "B"
    },
    {
        "question": "4. What does 2FA stand for?",
        "options": ["A. 2 File Access", "B. Two-Factor Authentication", "C. Transfer File Account", "D. None"],
        "answer": "B"
    },
    {
        "question": "5. What is a strong password example?",
        "options": ["A. password123", "B. 123456", "C. MySecure$Pass9", "D. qwerty"],
        "answer": "C"
    }
]

# Initialize score to 0
score = 0

# Welcome message
print("Cybersecurity Awareness Quiz")
print("-----------------------------------")

# Loop through each question
for q in questions:
    # Display the question
    print("\n" + q["question"])
    
    # Display all options
    for option in q["options"]:
        print(option)
    
    # Ask user for input and convert to uppercase for easy comparison
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    # Check if the answer is correct
    if answer == q["answer"]:
        print(" Correct!")  # Positive feedback
        score += 1           # Increase score
    else:
        print(f" Wrong! Correct answer is {q['answer']}")  # Show correct answer

# Show final score
print("\n--------------------------")
print(f"Your Score: {score}/{len(questions)}")

# Give feedback based on the score
if score == 5:
    print(" Excellent cybersecurity knowledge!")
elif score >= 3:
    print(" Good job! But you can improve.")
else:
    print("You need to learn more about cybersecurity.")