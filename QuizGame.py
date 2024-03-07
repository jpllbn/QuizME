# Importing required modules
import json
import random
import pyfiglet
from colorama import *


class Main:

    @staticmethod
    def banner():
        banner = pyfiglet.figlet_format("QuizMe", font="doom")
        print(f"{Fore.CYAN} {banner.strip()} by John Paul Labanon")
        print("-----------------------------------------------------")
        print(
            f"{Fore.RED + "Instructions:"}{Fore.CYAN} You have 3 lives to answer this Quiz Game.\nAnswer the questions "
            f"as much as you can and enjoy the game :)")
        print("-----------------------------------------------------")

    @staticmethod
    def correct_answer():
        print(f"{Fore.GREEN}--------------")
        print("Correct Answer")
        print("--------------")

    @staticmethod
    def wrong_answer():
        print(f"{Fore.RED}-----------------------------------")
        print(f"Wrong Answer, you have {lives} life left.")
        print(f"-----------------------------------")

    @staticmethod
    def learn():
        print("Guido Van Rossum developed Python Programming and was released in 1991. It was inspired by movie Monty "
              "Python\'s Flying Circus")


Main.banner()

# Open the JSON file for reading
with open("questions.json", "r") as file:
    # Load data from JSON
    data = json.load(file)

    # Extract questions and answers from JSON data
    questions = []
    answers = []
    for item in data:
        questions.append(item["question"])
        answers.append(item["answer"])

    score = 0
    lives = 3
    i = 0

    # Combine questions and answers into a list of tuples
    # Index                             0          1
    question_answer_pairs = list(zip(questions, answers))

    # Shuffle the list of question-answer pairs
    random.shuffle(question_answer_pairs)

    # while i is less than the length question_answer_pairs and lives is greater than zero
    # continue to ask the user questions
    # if the user_answer is equal to the answers inside the question_answer_pairs
    # print "Correct Answer" then add 1 pts in score
    # else "Wrong Answer, you have {lives} life left." if the user got wrong answer their lives
    # will be deducted by 1
    while i < len(question_answer_pairs) and lives > 0:
        user_answer = input(f"{Fore.WHITE}{question_answer_pairs[i][0]} ")
        if user_answer == question_answer_pairs[i][1]:
            Main.correct_answer()
            score += 1
        else:
            lives -= 1
            Main.wrong_answer()
        i += 1

        # If the user lives is equal to zero
        # print "Oh no, you don't have life left. Try again later!"
        if lives == 0:
            warning = 'Oh no, you don\'t have life left. Try again later!'
            print(warning.strip())

print("-------------------------------------------------")
print()

print(f"{Fore.YELLOW}------------------")
print(f"| You got {score} pts. |")
print(f"------------------")
