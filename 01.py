import requests
import html
import random

class Question:
    def __init__(self, question, options, correct):
        self.question = question
        self.options = options
        self.correct = correct

    def ask(self):
        print(self.question)
        for key, value in self.options.items():
            print(f"{key}: {value}")
        answer = input("Your answer: ").strip().upper()
        return answer == self.correct

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for q in self.questions:
            print("\n-------------------------")
            if q.ask():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")

def fetch_questions_from_api(amount=5):
    url = f"https://opentdb.com/api.php?amount={amount}&category=19&difficulty=medium&type=multiple"
    response = requests.get(url)
    data = response.json()

    questions = []

    for item in data['results']:
        question_text = html.unescape(item['question'])
        correct_answer = html.unescape(item['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in item['incorrect_answers']]
        all_answers = incorrect_answers + [correct_answer]
        random.shuffle(all_answers)

        option_labels = ['A', 'B', 'C', 'D']
        options = {label: ans for label, ans in zip(option_labels, all_answers)}
        correct_label = next(label for label, ans in options.items() if ans == correct_answer)

        questions.append(Question(question_text, options, correct_label))

    return questions

def main():
    print("Welcome to the API-based quiz!")

    while True:
        play = input("Do you want to play? (Y/N): ").strip().upper()
        if play == 'N':
            print("Goodbye!")
            break
        elif play == 'Y':
            quiz = Quiz(fetch_questions_from_api(5))
            quiz.start()
        else:
            print("Please enter Y or N.")

if __name__ == "__main__":
    main()
