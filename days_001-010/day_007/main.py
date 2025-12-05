import random

import hangman_art
import hangman_words
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
place_holder = ""
for letters in chosen_word:
    place_holder += "_"
print(f"Word to guess: {place_holder}")
lives = 6
game_over = False
letter_store = []


while not game_over:
    guess = input("Guess a letter:")
    display = ""
    if guess in letter_store:
        print(f"You have already guessed {guess}.")
    for letters in chosen_word:
        if letters == guess :
            display += guess
            letter_store.append(guess)
        elif letters in letter_store:
            display += letters
        else :
            display += "_"
    print(f"Word to guess: {display}")


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} that's not  in the word. You lose a life.")


    print(f"****************************{lives}/6 LIVES LEFT****************************")

    if "_" not in display :
        game_over = True
        print("****************************YOU WIN****************************.")
    elif lives == 0 :
        game_over = True
        print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************.")

    print(hangman_art.stages[lives])









