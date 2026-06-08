# Output => computer sends information to the user 
print("Hello World!")

# Variables: storage containers for data. variables names are important! they need to be specific! 
name = "Ms. LaRose"
print(name)
print("Hello " + name + "!")

# String: Letters, numbers, or symbols inside of quotation marks. Hold data, seperates instructions from information. 

# Input => users give information to the program (inputs always go in variables!)

#                                              v This makes the first letter capitalized
user = input("What is your name? ").strip().title()
#                                     ^ this gets rid of spaces on the outside of the string
print("Hello " + user + "!")

