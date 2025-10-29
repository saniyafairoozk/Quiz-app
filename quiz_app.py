import random
import time

def load_questions(filename):
    """Reads quiz questions from a text file"""
    try:
        with open(filename, "r") as file:
            questions = []
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 6:
                    question = {
                        "question": parts[0],
                        "options": parts[1:5],
                        "answer": int(parts[5])
                    }
                    questions.append(question)
            return questions
    except FileNotFoundError:
        print("❌ Error: 'questions.txt' file not found!")
        return []

def run_quiz(questions):
    """Runs the quiz and tracks the score"""
    score = 0
    random.shuffle(questions)  # Bonus: Randomize question order

    print("\n===== 🧠 Welcome to the Python Quiz! =====\n")
    time.sleep(1)

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for j, option in enumerate(q['options'], start=1):
            print(f"   {j}. {option}")

        try:
            user_answer = int(input("Your answer (1-4): "))
            if user_answer == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer is {q['options'][q['answer'] - 1]}\n")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1 and 4.\n")

        time.sleep(0.8)  # Adds a short pause for readability

    print("===================================")
    print(f"🏁 Quiz Finished! Your Score: {score}/{len(questions)}")
    print("===================================")

# Main Program
if __name__ == "__main__":
    filename = "questions.txt"
    quiz_questions = load_questions(filename)

    if quiz_questions:
        run_quiz(quiz_questions)
    else:
        print("No questions to display. Please check your file.")
