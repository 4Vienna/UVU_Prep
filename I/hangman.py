# Vienna LaRose, Hangman
import random 

####### Step 1: Create varaibles ########## (day 1)
# letter the user guessed (set during our loop not here): str (not day 1)
# words: list (10 or less)
words = ["word", "test", "stuff"]
# word for this round (randomly selected from a list): str
# wrong guesses: int 
# guessed letters: list []

######## Step 2: Build functions that are needed ####### 
# function to print out scaffold based on wrong guesses (takes in wrong guesses): (Day 2)
    # Conditional to check wrong guesses and print the correct scaffold
    # if wrong == 6:
        # print("""____
        #         |    |
        #         |    O
        #         |   /|\\   
        #         |   / \\
        #         |________
        # """)

# create a function to show user blanks and right guesses (takes in word and the list of guessed letters) (Day 1 (start))
def display(word, letters):
    # variable collecting display word for user: str
    display_word = ""
    # use for loop to look at each letter in the word individually:

        # check if the letter is in the list of guessed letters
            # add letter to the display word
        # if not in guessed letters
            # add _ to the display word 
    # return the display word 

# Create a while true loop (day 2)
    # Call function to print scaffold (day 2)
    # print my display function by calling it (day 2)
    # Show user the letters that have been guessed (day 2)
    # Save user guess as a variable (remember to stupid proof with strip and lower) (day 2)
    # add the letter to the guessed letters (day 2)
    # check to see if letter not in word (day 3)
        # Increase the amount of wrong guesses (day 3)

    # check to see if wrong guesses is 6 (day 3)
        # Tell them they lost (day 3)
        # show anything we want them to see (scaffold and/or correct word)(day 3)
        # break out of loop(day 3)
    # Check to see if they win (check if word matches the word display function)(day 3)
        # Tell them they win!(day 3)
        # break out of loop(day 3)
