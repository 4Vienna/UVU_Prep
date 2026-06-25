import random
import time
# ^ allows me to get random numbers 
"""
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
# Float: decimal numbers 
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


# Convert data types

number = float(input("Give me a number. . . please. "))

print(f"{number} + 2 = {number + 2}")

# lists <= Lets you save multiple peices of information in 1 variable
# index <= the number assocaited with an items spot in the list
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

print(siblings)

#siblings.append("Vienna") # <= adds an item to the end of the list
siblings.insert(3, "Vienna") # <= adds an item at a specific index
print(siblings[1])
siblings[4] = "Victoria"
siblings.pop(0)
siblings.pop(5)
print(siblings)

# For Loops <= repeat the number of times of items in your list
for sibling in siblings:
    print(f"Hi {sibling}")

for num in range(2,11, 2):
    print(num)

animals = []

for x in range(5):
    animals.append(input("Tell me an animal: "))

print(random.choice(animals))

print(random.randint(1,20))

# While Loops

# print the number when you hit the table
# **clap**
# **snap**

x = 1 # <= start point
while x <= 6: # <= stop point (loop stops when this condition is false)
    count = 1
    if x <= 2:
        while count < 8:
            time.sleep(.5)
            print(count)
            count += 1
    elif x <= 4:
        while count < 8:
            time.sleep(.5)
            if count % 2 == 0:
                print("**clap**")
            else:
                print(count)
            count += 1
    else:
        while count < 8:
            time.sleep(.5)
            if count == 2 or count == 5:
                print("**clap**")
            elif count % 3 == 0:
                print("**snap**")
            else:
                print(count)
            count += 1
    print("")
    x += 1 # <= increase the count (saved in the start point)

goose = random.randint(1,11)
count = 0

while True:
    if count == goose:
        break # <= stops the loop without meeting a condition
    else:
        print("Duck")
    count += 1
print("GOOSE!")"""

# functions! 
# v keyword to start a funciton
def hello(name): #<= inside the parenthesis we list arguements (variables that only exist in the function)
    # ^ name of the function 
    print(f"Hello {name}") # <= What happens when the funciton is called

hello("Katie") # We call a funciton by writing its name and parenthesis 
hello("Tia") # IF I have parameters, arguements are given as the values for those parameters

def turn(name, enemy_hp, enemy_defense):
    attack = random.randint(1,20) + 3
    if enemy_defense > attack:
        print("Your attack missed!")
        return enemy_hp
    else:
        damage = random.randint(1,8) + 2
        print(f"{damage} damage. {name} has {enemy_hp-damage} HP left!")
        return enemy_hp - damage

monster_hp = 20   
player_hp = 50
while True:
    monster_hp = turn("Monster",monster_hp, 10)
    if monster_hp > 0:
        player_hp = turn("Player",player_hp, 10)
        if player_hp <= 0:
            print("You died")
            break
    else:
        print("You won!")
        break
