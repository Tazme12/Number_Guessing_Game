import random

print ("""Welcome to the Number Guessing Game!
       I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.""")

def game_rules():
    None

def menu1():
    for i in range(10):
        number = random.randint(1, 100)
        userinput = ("Please enter a number to guess: ")

menuchoice = input("Enter your choice: ")
if menuchoice == 1:
    print("Great! You have selected the Easy difficulty level.")
    print("Let's start the game!")
    menu1()