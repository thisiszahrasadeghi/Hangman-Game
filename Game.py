import Hangman_words
import Hangman_art
import random
from replit import clear

print(Hangman_art.logo)

word_list = Hangman_words.words_list
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word :
    display.append("_")
    
guessed_letters = []
lives = 6
game_is_done = False 
while not game_is_done :
    guess = input("Guess a letter : ").lower()
    clear()
    if guess in guessed_letters :
        print("You had chosen this letter before.")
    else:
        guessed_letters += guess
        for position in range (0 , len(chosen_word)) :
            letter = chosen_word[position]
            if letter == guess :
                display[position] = guess
        if guess not in chosen_word :
            lives -= 1
            print(f" You guessed \"{guess}\" , that's not in the word. You lose a life! ")
            if lives == 0 :
                print(f"You lose , the word was = {chosen_word}")
                game_is_done = True 
        print(f"{' '.join(display)}\n")
        if "_" not in display :
            print("Gongrats , you saved the man. ")
            game_is_done = True 
        print(Hangman_art.stages[lives])

