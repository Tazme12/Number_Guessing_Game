import random

def game_rules():
    print ("1. Easy (10 guesses)")
    print ("2. Medium (5 guesses)")
    print ("3. Hard (3 guesses)")
    optionselect = input("Please select the difficulty level: ").upper()
    while True:
        if optionselect == "EASY":
            print("Great! You have selected the Easy difficulty level.")
            print("Let's start the game!")
            print ("I'm thinking of a number between 1 and 100.")
            menueasy()
            return
        elif optionselect == "MEDIUM":
            print("Great! You have selected the Medium difficulty level.")
            print("Let's start the game!")
            print ("I'm thinking of a number between 1 and 100.")
            menumedium()
            return
        elif optionselect == "HARD":
            print("Great! You have selected the Hard difficulty level.")
            print("Let's start the game!")
            print ("I'm thinking of a number between 1 and 100.")
            menuhard()
            return
        else:
            print("Please enter either 'Easy', 'Medium' or 'Hard'")

def menueasy():
    guesses = 10
    attempts = 0
    number = random.randint(1, 100)
    while guesses > 0:    
        try:
            userinput = int(input("Please enter a number to guess: "))
            if userinput == number:
                guesses -= 1
                print("Congratulations, you guessed correctly")
                attempts += 1
                print("You took", attempts,"attempts")
                print("Would you like to play again?")
                pa_input = input("Enter Y/N: ").upper()
                if pa_input == 'Y':
                    continue
                else:
                    break
            elif userinput > number:
                print("Incorrect, lower")
                guesses -= 1
                print("You have", guesses,"guesses left")
                attempts += 1
            elif userinput < number:
                print("Incorrect, higher")
                guesses -= 1
                print("You have", guesses,"guesses left")
                attempts += 1
        except ValueError:
            print("Thats not a number, Try again.")
    print(f"Game over! You run out of chances. The number was {number}\n")
    attempts = None
    return guesses, attempts

def menumedium():
    guesses = 5
    attempts = 0
    number = random.randint(1, 100)
    while guesses > 0:    
        try:
            userinput = int(input("Please enter a number to guess: "))
            if userinput == number:
                guesses -= 1
                print("Congratulations, you guessed correctly")
                attempts += 1
                print("You took", attempts,"attempts")
                print("Would you like to play again?")
                pa_input = input("Enter Y/N: ").upper()
                if pa_input == 'Y':
                    continue
                else:
                    break
            elif userinput > number:
                print("Incorrect, lower")
                guesses -= 1
                print("You have", guesses,"guesses left")
                attempts += 1
            elif userinput < number:
                print("Incorrect, higher")
                guesses -= 1
                print("You have", guesses,"guesses left")
                attempts += 1
        except ValueError:
            print("Thats not a number, Try again.")
    print(f"Game over! You run out of chances. The number was {number}\n")
    attempts = None
    return guesses, attempts

def menuhard():
    guesses = 3
    attempts = 0
    number = random.randint(1, 100)
    while guesses > 0:    
        try:
            userinput = int(input("Please enter a number to guess: "))
            if userinput == number:
                guesses -= 1
                print("Congratulations, you guessed correctly")
                attempts += 1
                print("You took", attempts,"attempts")
                print("Would you like to play again?")
                pa_input = input("Enter Y/N: ").upper()
                if pa_input == 'Y':
                    continue
                else:
                    break
            elif userinput > number:
                print("Incorrect, lower")
                guesses -= 1
                print("You have", guesses,"guesses left")
                attempts += 1
            elif userinput < number:
                print("Incorrect, higher")
                guesses -= 1
                print("You have", guesses,"guesses left")
                attempts += 1
        except ValueError:
            print("Thats not a number, Try again.")
    print(f"Game over! You run out of chances. The number was {number}\n")
    attempts = None
    return guesses, attempts

print ("Welcome to the Number Guessing Game!")
print ("Below are the difficulty levels for the game:")
game_rules()
print("Would you like to play again?")
while True:
    pa_input = input("Enter Y/N: ").upper()
    if pa_input == 'Y':
        game_rules()
    else:
        break