# Vienna LaRose, hangman
import random 

############### Step 1: Variables ################ (Day 1)
# list of possible words: list (of strings) (10 words)
words = ["word", "stuff", "things", "school"]
# the word (randomly selected from a list): str

# guessed letters: list (of strings)
guesses = []
# wrong guesses: int 

################ Step 2: Functions #################
# function to display the scaffold (take in wrong guesses) (Day 2)
    # Conditional that checks wrong guesses and prints the correct scaffold 
    # print("""____
    #         |   O
    #         |  /|\\
    #         |  / \\
    #         |_______
    # """)

# Function to build the display word (needs the word and the guessed letters) (Day 1)

    # a variable keeping track of the display word (starts as an empty string)
    # create a loop that looks at each letter in the word 
        # Is the letter in the guessed letters list
            # add letter to display word variable 
        # if it isn't
            # add an underscore to the display word variable 
    # return display word variable 

########### Step 3: The game loop ###################
# Build a while true loop (Day 2)
    # call the function to display the scaffold (Day 2)
    # print the function to display the word (underscores and guessed letters) (Day 2)
    # Show the what letters have been guessed already(Day 2)
    # variable for user input to guess a letter (strip and lower stupid proofing) (Day 2)
    # add the letter to the guessed letters list (Day 2)
    # If letter is not in the word (Day 3)
        # Increase wrong the wrong guesses count (Day 3)
    # Check to see if they won (Check to see if word matches the output from the display word function) (Day 3)
        # Tell user they won(Day 3)
        # break out of loop (Day 3)
    # Check to see if they lost (wrong guess is 6)(Day 3)
        # Tell user the lost(Day 3)
        # Tell user the word (maybe display the completed hangman)(Day 3)
        # break out of the loop(Day 3)

