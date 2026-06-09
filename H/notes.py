# Variables: containers that hold information 
# variables are created when we lable the space

name = "Ms. LaRose"

# Output => information sent from the computer to the user

print("Hello World!")

# To print a variable, write tne name of the variable with no quotation marks
print(name)

# input => lets you get information from your user

#user = input("What is your name? ").strip().title()
#animal = input("Tell me an animal: ").strip().lower()

#print("Hello " + user + "!" + "I love " + animal + "s too!")

# Strings: a collection of letters, numbers or symbols that are surrounded by quotation marks. This is used to seperate instructions for the computer from data being used by the program! 

# Concatenation: puts strings together. + 

# Integers: whole numbers
# Float: decimal numbers 

print(5*4+7/3) #the computer knows order of operations! PEMDIMAS

num = 42

num += 1

num /= 10

num -= 2

print(num - 5)
print(num ** 5) #exponents
print(num / 5)
print(num // 5) #integer division (only gives the integer of a division problem)
print(num % 5) #Mod (modulo/modulus) gives the remainder of a division problem

# Conditionals: questions that allow us to control IF something is going to happen

if num == 42: # <= always start with if
    print("Life the univers and everything")
elif num % 2 == 0: # <= elif for all in between
    print(num, "is an equal number")
else: # <= always end with else
    print(num, "is an odd number")


# Comparison Operators: >= < > == != <=