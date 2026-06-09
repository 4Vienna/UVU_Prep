# Output => computer passes information to the user
print("Hello World!")

# Variables: containers that store data. Every variable must have a unique name
name = "Ms. LaRose"

print(name)

animal = "Panda"
verb2 = "swim"
print("Hello " + name + "! Do you like " + animal + "s?")

# Strings: Letters, characters, numbers, and symbols that are surrounded by quotation marks. Seperates data from commands 

# Inputs => User gives the computer information 
#user = input("What is your name? ").strip().title()

#print("Hello " + user + ".")
#print(user + " do you know " + name + "?")

# MATH
print(-2*7-(3+5)+8*6)
# Your computer knows order of operations! PEMDIMAS 

# Integers: whole numbers 
# + - * / **(exponenets) //(int div) %(mod, modulo, modulus gets the remainder)

apples = 4
print(apples)
#apples -= 3 #subtracts 3 and resets the answer as the variable 
print(apples)

print(apples/2)
print(apples//2)
print(apples%2)

# Conditionals: Only do this thing IF a condition is met
people = 6
# comparison operators: < > == >= <= !=
if apples//people > 3: # <= always starts with an if
    print("Each person can have 3 apples!")
elif apples < people:
    print("Sorry, not enough apples.")
elif apples % people == 0: # <= As many as we want! 
    print(f"Everyone gets {apples//people} apples!")
else: # <= ends with an else
    print(f"Each person gets {apples//people} apples, and there are {apples % people} apples left over!")