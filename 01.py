class Quiz:
    def __init__(self):
        self.score = 0

    def ask_question(self, question, options, correct_option):
        print(question)
        for key, value in options.items():
            print(f"  {key} : {value}")
        answer = input("Your answer: ").strip().upper()
        if answer == correct_option:
            self.score += 1
            print("Correct!\n")
        else:
            print("Incorrect!\n")

    def run(self):
        self.ask_question(
            "What does CPU stand for?",
            {'A': 'Control Processing Unit', 'B': 'Central Processing Unit', 'C': 'Control Processed Unit', 'D': 'Central Processed Unit'},
            'B'
        )
        self.ask_question(
            "How many colours are in a rainbow?",
            {'A': '6', 'B': '7', 'C': '8', 'D': '9'},
            'B'
        )
        self.ask_question(
            "Wavelength of colour red in nanometers?",
            {'A': '650', 'B': '550', 'C': '750', 'D': '850'},
            'A'
        )
        print(f"Your final score is: {self.score}/3\n")


def main():
    print("Welcome to my computer quiz!\n")

    while True:
        playing = input("Wanna play? (Y/N): ").strip().upper()
        if playing == 'N':
            print("Okay, maybe next time!")
            break
        elif playing == 'Y':
            quiz = Quiz()
            quiz.run()
            break
        else:
            print("Invalid input. Please enter Y or N.\n")

if __name__ == "__main__":
    main()
