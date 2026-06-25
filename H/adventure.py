# Vienna LaRose, Text Based Adventure Game

###################### Step 1: Variables ####################################
player = { # <= dictionary (key & Value pairs to give details about an item)
    "hp": 20,
    "attack": 8,
    "defense": 10,
    "inventory": []
}

goblin = {
    "hp": 8,
    "attack": 4,
    "defense": 12
}
# variable for the current room


###################### Step 2: Functions ####################################
# Combat function
def combat(player, enemy):
    turn = random.choice(["player", "enemy"])
    while True:
        if turn == "player":
            # Give 3 options in combat
            enemy["hp"] -= player["attack"]
        else: 
            player['hp'] -= enemy['attack']
        #check to see if died, break out of loop
    return player, enemy


# Room 1 (start room)
    # give discription of situation
    # Give options for where to go/things to do
    # Return what room they are going to next 

# Room 2 (kitchen)
    # give discription of situation
    # Give options for where to go/things to do
    # player, enemy = combat(player, goblin)
    # Return what room they are going to next 

###################### Step 3: Loop to run the game ##########################

# Make a while true loop
    #Build conditional that checks the room and calls the correct function
## example
if current_room == "start":
    current_room = start()
elif current_room == "dinning":
    current_room, player, goblin = dinning(player, goblin)

# Check if user died
# check is user won!