# Output => computer sends information to the user 
print("Hello World!")

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