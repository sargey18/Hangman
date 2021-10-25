import random
from words import words
import string

# 1) we need to get the computer to pick a word, but we need a word with no space 

def get_valid_word(words):
    word = random.choice(words)  # random.choice randomly chooses something from the list 
    while '-' in word or ' ' in word:
        word = random.choice(words)  # while there is a - or a space in the word variable keep randomly choosing a word from the words list imported 
        
    return word.upper()

# 2) we have to keep track of the letters we have guessed and the letters we have corectly guessed  ... and what is a valid letter and what isnt 

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed 
    
    
    lives = 6
    # getting user input 
    
    # so now that we have the user input we want the user to keep guessing until they get the word 
    # in this case we will use a loop 
    # in this case we will use a while loop because we want the user to keep gussing until the get the word 
    # the condition we are looking for is when word_letters is actually equal to zero
    
    while len(word_letters) > 0 and lives > 0:
        # letters used 
        print('You have', lives, 'You have used these letters: ', ' '.join(used_letters))
        
        # now we create a list where every single letter that guessed is shown and where all the letters they have not guessed are -
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
    
        user_letter = input('Guess a letter: ').upper()
        # if this is a valid character in the apphabet that I have not used yet then i will add this to the used_letter set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            #then if the letter i guessed is in the word, then i will remove that letter from word_letters
            # every time i guess correctly the the word_letters which is keeping track of all the letters in a word decreases
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1 # takes a life away
                print('letter not in the word')
            # and then if this user_letter that the user just entered is in used letters then that means they have already used it before and it is invalid 
            
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
                
        else:
            print('Invalid character. Please try again. ')
            
    if lives == 0:
        print('You died sorry the word was', word)
    else: 
        print('You guessed the word')



    
user_input = input('Type something: ')
print(user_input)

hangman()