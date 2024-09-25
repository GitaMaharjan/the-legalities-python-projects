# 22.  Simple Quiz Application   
#     *Description*: Create a quiz application that asks multiple-choice questions and provides feedback.  
#     *Skills*: Lists, loops, conditionals.

import random

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer_index):
        # Check if the user's chosen index (0-based) matches the index of the correct answer
        return user_answer_index == self.options.index(self.answer)
    def shuffle_options(self):
        random.shuffle(self.options)


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def conduct_quiz(self):
        random.shuffle(self.questions)  # Shuffle the order of questions

        for question in self.questions:
            question.shuffle_options()  # Shuffle the options for each question
            print(question.prompt)
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")

            # Ensure user enters a valid option number
            while True:
                try:
                    user_answer = int(input("Choose the option number: "))
                    if 1 <= user_answer <= len(question.options):
                        # Check correctness using the 0-based index
                        if question.is_correct(user_answer - 1):  # Convert to 0-based index
                            print("Correct!")
                            self.score += 1
                        else:
                            print(f"Wrong! The correct answer is: {question.answer}")
                        break
                    else:
                        print("Please choose a valid option number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            print()  # Print a newline for better formatting

        self.display_score()

    def display_score(self):
        print(f"You scored {self.score} out of {len(self.questions)}.")


def main():
    # Create quiz instance
    quiz = Quiz()

    # Define questions
    question1 = Question(
        "What is the capital of France?",
        ["Berlin", "Madrid", "Paris", "Rome"],
        "Paris"
    )
    question2 = Question(
        "Which planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Saturn"],
        "Mars"
    )
    question3 = Question(
        "What is the largest mammal in the world?",
        ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "Blue Whale"
    )
    question4 = Question(
        "What is the chemical symbol for gold?",
        ["Au", "Ag", "Pb", "Fe"],
        "Au"
    )
    question5 = Question(
        "In which year did the Titanic sink?",
        ["1905", "1912", "1915", "1920"],
        "1912"
    )
    question6 = Question(
        "Who wrote 'Romeo and Juliet'?",
        ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "William Shakespeare"
    )
    question7 = Question(
        "What is the smallest country in the world?",
        ["Monaco", "Vatican City", "Nauru", "Malta"],
        "Vatican City"
    )
    question8 = Question(
        "Which gas do plants absorb from the atmosphere?",
        ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "Carbon Dioxide"
    )
    question9 = Question(
        "What is the main ingredient in guacamole?",
        ["Tomato", "Onion", "Avocado", "Pepper"],
        "Avocado"
    )
    question10 = Question(
        "Who painted the Mona Lisa?",
        ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "Leonardo da Vinci"
    )

    # Add questions to the quiz
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)
    quiz.add_question(question4)
    quiz.add_question(question5)
    quiz.add_question(question6)
    quiz.add_question(question7)
    quiz.add_question(question8)
    quiz.add_question(question9)
    quiz.add_question(question10)

    # Conduct the quiz
    quiz.conduct_quiz()


if __name__ == "__main__":
    main()
