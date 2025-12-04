import random
guessed_number = random.randint(2,99)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
def game(attempts):
    game_ends = False
    while not game_ends:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a Guess."))
        if user_number > guessed_number :
            print("Too high.")
            print("Guess again.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again ")
                game_ends = True
        elif user_number < guessed_number:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again ")
                game_ends = True
        else:
            print(f"You got it! The answer was {user_number}.")
            game_ends = True

difficulty = input("Choose a difficulty.Type 'easy' or ' hard'.\n").lower()
if difficulty == "easy":
    game(10)
else:
    game(5)

