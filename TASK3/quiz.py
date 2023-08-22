import random
from tabulate import tabulate

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.user_answers = {}

    def display_welcome(self):
        print("\033[1;33mWelcome to the Quiz Game!\033[0m")
        print("\033[1;36mAnswer multiple-choice or fill-in-the-blank questions to test your knowledge.\033[0m")
        print("Type '\033[1mquit\033[0m' anytime to exit the quiz.\n")

    def present_question(self, question):
        print("\033[1m" + question['question'] + "\033[0m")
        if 'choices' in question:
            for i, choice in enumerate(question['choices'], start=1):
                print(f"{i}. {choice}")
            while True:
                user_choice = input("\033[1mSelect your choice (1, 2, 3, 4):\033[0m ")
                if user_choice.isdigit() and 1 <= int(user_choice) <= len(question['choices']):
                    break
                else:
                    print("\033[31mInvalid choice. Please select a valid option.\033[0m")
            user_answer = question['choices'][int(user_choice) - 1]
        else:
            user_answer = input("\033[1mYour answer:\033[0m ")
        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\033[32mCorrect!\033[0m\n")
            return True
        else:
            print(f"\033[31mIncorrect. The correct answer is: \033[32m{correct_answer}\033[0m\n")
            return False

    def display_final_results(self):
        print("\033[1;34mQuiz Completed!\033[0m")
        print(f"Your final score is: {self.score}/{len(self.questions)}\n")

        table_headers = ["Question", "Your Answer", "Correct Answer", "Result"]
        table_data = []

        for q_number, question in enumerate(self.questions, start=1):
            user_answer = self.user_answers.get(q_number, "-")
            correct_answer = question.get('blank', question.get('answer'))
            result = "\033[32mCorrect\033[0m" if user_answer.lower() == correct_answer.lower() else "\033[31mIncorrect\033[0m"

            table_data.append([q_number, user_answer, correct_answer, result])

        table = tabulate(table_data, headers=table_headers, tablefmt="pretty")
        print(table)

        if self.score == len(self.questions):
            print("\n\033[32mCongratulations! You got all the questions right.\033[0m")
        elif self.score >= len(self.questions) / 2:
            print("\nGood job! You did well.")
        else:
            print("\nKeep practicing to improve your knowledge.")

    def play(self):
        self.display_welcome()

        play_again = 'yes'
        while play_again.lower() == 'yes':
            self.score = 0
            self.user_answers = {}
            random.shuffle(self.questions)
            for q_number, question in enumerate(self.questions, start=1):
                print(f"Question {q_number}/{len(self.questions)}:")
                user_answer = self.present_question(question)
                self.user_answers[q_number] = user_answer
                if user_answer.lower() == 'quit':
                    break
                if 'blank' in question:
                    self.evaluate_answer(user_answer, question['blank'])
                else:
                    self.evaluate_answer(user_answer, question['answer'])

            if user_answer.lower() == 'quit':
                print("\nExiting the quiz.")
                break

            self.display_final_results()

            play_again = input("Do you want to play again? (yes/no): ")

        print("Thank you for playing!")

# Define quiz questions
quiz_questions = [
    {
        'question': 'Which type of Programming does Python support?',
        'choices': ['Object-oriented programming', 'Structured programming', 'Functional programming', 'All the Above'],
        'answer': 'All the above'
    },
    {
        'question': 'What will be the value of the following Python expression \n 4 + 3 % 5',
        'choices':['7','2','4','1'],
        'answer': '7'
    },
    {
        'question': ' _______ keyword is used to define a function in python.',
        'blank': 'def'
    },
    {
        'question':'Which of the following is not a core data type in Python programming?',
        'choices':['Tuples','Lists','Class','Dictionary'],
        'answer':'Class'
    },
    {
        'question':'The correct extension of a Python file is _______',
        'blank':'.py'
    }
    # Add more questions here
]


# Create and play the quiz game
quiz_game = QuizGame(quiz_questions)
quiz_game.play()
