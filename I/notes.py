import random
# ^ this allows me to use the random library 
import time
# Output => computer sends information to the user 
"""print("Hello World!")

# Variables: storage containers for data. variables names are important! they need to be specific! 
name = "Ms. LaRose"
print(name)
print("Hello " + name + "!")

# String: Letters, numbers, or symbols inside of quotation marks. Hold data, seperates instructions from information. 

# Input => users give information to the program (inputs always go in variables!)

#                                              v This makes the first letter capitalized
#user = input("What is your name? ").strip().title()
#                                     ^ this gets rid of spaces on the outside of the string
#print("Hello " + user + "!")

# MATH
print(1-(12*2-1)/7) # Computer knows order of operations! PEMDIMAS
# +add -sub *mul /div **ex //int div %mod (modulo/modulus)

# Integer: whole number 
# Float: Decimal numbers 
num = 24

num = 7

print(num/5) # 8.4
print(num//5) #Just the whole number 
print(num%5) #the remainder 

apples = 25
people = 5

# conditional: checks IF something is true or false and gives different outputs 
if apples // people > 3: # <= you must start with an if
    print("Everyone can have 3 apples")
elif apples % people == 0: # <= double = check IF they are the same single = says they are the same
    print(f"Everyone can have {apples//people} apples.")
elif apples < people:
    print("Sorry there aren't enough apples for everyone :(")
else: # <= you must end with an else
    print(f"Everyone can have {apples//people} apples and {apples%people} people can have an extra!")

# Data Type Conversion

number = int(input("What is your favorite number? ")) #this is always a string

print(f"{number} + 2 = {number+2}")

# lists => multiple peices of data in 1 variable
# index => the number connect to each item in the list
siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"]

print(siblings)
print(siblings[2])
siblings[0] = "Eric"
siblings.append("Sam") # <= append adds to the end of the list
#siblings.append(["Joseph", "Israel", "Zee"])
siblings.insert(1, "Jayshree")
siblings.pop(4) # <= if no index is given it removes the last item
siblings.sort() # <= puts list in alphabetical order 

# for loop => repeat for the number times that there are items in the list
for sibling in siblings:
    print(f"Hi {sibling}")

for x in range(5,11, 2):
    print(x)

animals = []

for i in range(5):
    animals.append(input("Tell me an animal: "))

print(animals)

print(random.randint(1,20))
print(random.choice(animals))

words = []
topics = ["noun", "verb", "name", "place"]

for topic in topics:
    words.append(input(f"Please give me a {topic}: "))"""

"""# While Loops
count = 1 # <= Set the start point 
while count <= 10: # <= Set the end point (loop runs while the condition is True, it will end when the condition is False)
    time.sleep(1)
    print(count)
    count += 1 # <= increase the count (iterator) 
"""
"""print("Rhythm game")

section = 1
while section <= 4:
    beat = 1
    if section <= 2:
        while beat <=7:
            time.sleep(.5)
            print(beat)
            beat += 1
    else:
        while beat <=7:
            time.sleep(.5)
            if beat % 2 == 0:
                print("**clap**")
            else:
                print(beat)
            beat += 1
    print("")
    section += 1"""
"""
goose = random.randint(1,11)
people = 1

while True: # <= This loop will run forever
    time.sleep(.25)
    if goose == people:
        break # <= lets you leave a loop without meeting a condition
    else:
        print("Duck. . . ")
        people += 1
print("GOOSE!!!!")"""

# Functions
# Decreased repetition in written code
# Organized Code (easier to read)
# More modular (more versitile (usable in more situations))
user = "Vienna"

# v keyword to start a function
def hello(name): # <= parameters go inside of the perenthesis, kinda like variables just for this funciton
    # ^ the name of the function (we can name it anything)
    print(f"Hello {name}")

hello("Andrew") # <= function call, tells the funciton to run
hello(input("What is your name: "))
hello(user) # <= arguments go inside of perenthesis, they give a value for the parameters

def add(num1, num2):
    return num1 + num2 #<= passes information back to where the function is called instead of to the user

total = add(42, 3)
print(total * .064)

print(add(7, 1))
print(add(8, add(40,8)))


def turn(hp, defense, turn):
    if turn == "Monster":
        attacker = "the monster"
        defender = "you"
    else:
        attacker = turn
        defender = "the monster"
    attack = random.randint(1,20) + 6
    if attack > defense:
        damage = random.randint(1,8) + 2
        print(f"{attacker} hit {defender} for {damage} damage. {defender}'s health is now {hp-damage}")
        return hp-damage 
    else:
        print(f"{attacker} missed")
        return hp
    
monster_hp = 30
player_hp = 50
while True:
    time.sleep(.25)
    monster_hp = turn(monster_hp, 12, user)
    if monster_hp <= 0:
        print("You won!")
        break
    else:
        player_hp = turn(player_hp, 14, "Monster")
        if player_hp <= 0:
            print("You died.")
            break