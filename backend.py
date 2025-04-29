import random

def game_rules():
    print ("1. Easy (10 chances)")
    print ("2. Medium (5 chances)")
    print ("3. Hard (3 chances)")
    optionselect = input("Please select the difficulty level: ").upper()
    if input == "EASY":
        print("Great! You have selected the Easy difficulty level.")
        print("Let's start the game!")
        menueasy()
        return


def menueasy():
    for i in range(10):
        number = random.randint(1, 100)
        userinput = ("Please enter a number to guess: ")
        if userinput == number:
            print("Congratulations, you guessed correctly")
        elif userinput != int:
            print("Please enter a number: ")
            break
        else:
            print("Incorrect, you have", i ,"guesses left")

print ("Welcome to the Number Guessing Game!")
print ("Below are the difficulty levels for the game:")
game_rules()
print ("I'm thinking of a number between 1 and 100.")