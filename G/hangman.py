# Vienna LaRose, Hangman 

# Variables List: (Day 1)
    # Possible words: list
word_list = ["word", "test", "sample", "guess"]
    # Body Parts? => # of wrong guesses: int
wrong = 0
    # Guessed letters: list 
    # Specific word for this round: str
    #

# Function to print scaffold at correct wrong level (takes in wrong guesses) (day 2)
    # Conditional to check level and print correct image
    # example 
    # if wrong == 6:
        #print("""___
                #|   |
                #|   O
                #|  /|\\
                #|  / \\
                #|_____
        # """)

# Function for word display (takes in guessed letters, word) (Day 1)
    #variable that has our current display
    # look at each letter in the word
        #check to see if the letter is in the guessed letters
            # Add the letter to the current display
        #otherwise
            # add an _ to the current display
    # return the current display 


# randomly select word from list of possible words (day 2)
# while True (day 2)
    # call function to print the scaffold (day 2)
    # print function to display word (day 2)
    # print guessed letters variable (day 2)
    # create letter variable equal to user input asking for a letter (don't forget to strip and lower) (day 2)
    # add letter to guessed letters (day 2)
    # if the letter is not in the word (day 3)
        # increase wrong guesses

    # check if word matches word display function (day 3)
        # Tell the user they won!
        # Stop the loop
    # check of 6 wrong guesses (day 3)
        # tell user they lost
        # call scaffold function
        # show correct word 
        # Stop the loop

