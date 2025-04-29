import random

print ("""Welcome to the Number Guessing Game!
       I'm thinking of a number between 1 and 100.""")

def game_rules():
    optionselect = input("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""").upper()
    if input == "EASY":
        print("Great! You have selected the Easy difficulty level.")
        print("Let's start the game!")
        menueasy()


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
            print("Incorrect, you have", i "guesses left")