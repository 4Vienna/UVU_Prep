import random
import time
# ^ this allows me to access the random library 

# Variables: containers that hold information 
# variables are created when we lable the space

"""name = "Ms. LaRose"

# Output => information sent from the computer to the user

print("Hello World!")

# To print a variable, write tne name of the variable with no quotation marks
print(name)

# input => lets you get information from your user

user = input("What is your name? ").strip().title()
animal = input("Tell me an animal: ").strip().lower()

print("Hello " + user + "!" + "I love " + animal + "s too!")

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

# convert data type
num = input("Tell me a number: ")

print(float(num) + 2)

# Lists => a data type that holds multiple items in it
# index => a number associated with where the item is in a list
sibs = ["Alex", "Jayshree", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
print(sibs)
nums = [1351,684,651,68,465,16,84,651,68,76,54]
sibs.append("Sam") #<= adds  to the end of the list
sibs.insert(4, "Vienna") #<= adds an item at the given index
sibs.pop(1) #<= removes an item from the end of a list OR a specified index will be removed
sibs[0] = "Eric"
# for loops => a loop that repeats for every item in a list
for sib in sibs:
    if sib == "Jayshree":
        print(f"{sib} Sampali LaRose")
    else:
        print(f"{sib} LaRose")

# range creates a list of numbers (range stops at the number you put in)
for num in range(1,10,2):
    print(num)

animals = []

for x in range(4):
    animals.append(input("Tell me an animal: "))

print(random.randint(1,21))
print(random.choice(animals))

# While Loops
count = 1 # <= Start point (keep track of the number we are on)
while count <= 10: # < = Stop point (loop stops when the condition is false)
    time.sleep(.5) # <= not needed, delays the print
    print(count)
    count += 1 # <= Increases our count 

round = 1
while round <= 4:
    beat = 1
    if round <= 2:
        while beat <= 7:
            time.sleep(.25)
            print(beat)
            beat += 1
    else:
        while beat <= 7:
            time.sleep(.25)
            if beat % 2 == 0:
                print("**clap**")
            else:
                print(beat)
            beat += 1
    print("")
    round += 1

goose = random.randint(1,11)
number = 1
while True: # <= This loop will run forever because True always == True
    if number == goose:
        break # <= lets you leave the loop even if the condition isn't met
    else:
        time.sleep(1)
        print("duck. . . . ")
        number += 1

print("GOOSE!")"""

# Functions 
# Keep us from writing repetitive code
# Make the code more versitile (good in many situations)
# Makes code easier to read
user = "Vienna"

# v the keyword to write a function
def hello(name): # <= parameters (they go in the parenthesis). special variables that only exist for the function
    # ^ name the function (that is how we call it later)
    print(f"Hello {name}")

hello("Katie") # <= function call, this is how we tell the computer to run the function
hello(input("Tell me a name: "))
hello(user) # <= in the parenthesis of a function call you put arguements, 1 for each parameter in the function definition 

def add(num1, num2):
    return num1 + num2 # <= sends the information to where I called the funciton

print(add(4,2))

number = add(12,-5)

print(add(number, add(6,4)))

def turn(name, HP, defense):
    attack = random.randint(1,20) + 2
    if attack > defense:
        damage = random.randint(1,8) + 2
        print(f"{damage} damage. {name} now has {HP - damage}!")
        return HP-damage
    else:
        print("Attack missed")
        return HP
    

monster_HP = 40
player_HP = 30
while True:
    monster_HP = turn("monster", monster_HP, 10)
    if monster_HP <= 0:
        print("You won!")
        break
    else:
        player_HP = turn("player",player_HP, 15)
        if player_HP <= 0:
            print("You died :(")
            break
