import random
from words import words
import string


def get_valid_word(word):
    word= random.choice(word)
    while "-" in word or " " in word:
        word= random.choice(word)

    return word.upper()

def hangman():
    word= get_valid_word(words)
    word_letters= set(word)
    alphabet= set(string.ascii_uppercase)
    used_letters= set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("you have used these letters: ", ' '.join(used_letters))
        print("you have ", lives, "lives left")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print ('Current word: ' , ' '.join(word_list))

        print("  ")
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives=lives -1 
                print("")
                print(user_letter, " is not in the word")

        elif user_letter in used_letters:
            print("you have already guessed that letter. Please try again.")

        else:
            print("You've used a wrong character. Please try again")

    
    if lives == 0:
        print("you died. Sorry.  The word was ", word)
    else:
        print("You guessed the word.   The word is ",  word)
    
    print("")
    print("Do you want to play again? ")
    answer=input('(yes/no): ')
    x= "yes"
    if x == answer :
        print("")
        print(hangman())
    else:
        print("Maybe next time")
    #print(word)
    
hangman()