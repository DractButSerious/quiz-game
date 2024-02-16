import random
import questions.culture
import questions.gaming
import questions.programming
from colorama import init, Fore
init(autoreset=True)

subjects = [questions.culture.questions, questions.gaming.questions, questions.programming.questions]

subject = 0
question = 0
options = []

score = 0

def welcome():
    print("Welcome! You'll be asked a question and you will be given four choices, one of which is correct, and you will enter the corresponding number to your answer. Ready?\n")

def display_question():
    subject = random.randint(0, 2)
    question = random.randint(0, 4)
    correct_answer = subjects[subject][question].get("correct_answer")
    options = subjects[subject][question].get("options")
    print(Fore.LIGHTCYAN_EX + subjects[subject][question].get("question"))
    for i, x in enumerate(options):
        print(Fore.BLUE + str(i + 1) + ". " + Fore.RESET + x)
    answer = 0
    while True:
        try:
            answer = int(input(Fore.LIGHTBLUE_EX + "Enter your answer: " + Fore.RESET))
        except ValueError:
            print(Fore.LIGHTRED_EX + "ERROR: Invalid response, try again.")
        else:
            if answer < 1 or answer > 4:
                print(Fore.LIGHTRED_EX + "ERROR: Invalid answer, try again.")
            else:
                break
    if options[answer - 1] == correct_answer:
        print(Fore.LIGHTGREEN_EX + "Correct! " + Fore.GREEN + "Next question!")
        return True
    else:
        print(Fore.LIGHTRED_EX + "Incorrect! " + Fore.RED + "Game over!")
        return False
    
def display_score():
    print("Score: " + Fore.YELLOW + str(score) + "\n")

welcome()
score = 0
correct = True
while correct:
    correct = display_question()
    if correct:
        score += 1
    display_score()