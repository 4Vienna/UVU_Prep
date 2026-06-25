# Vienna LaRose, Final, Text based adventure Game

################### Step 1: Variables ##########################
player = { # <= Dictionary (key, value pairs to have details about an item)
    "hp": 15,
    "def": 10,
    "attack": 5,
    "inventory": []
}
goblin = {
    "hp": 8,
    "def": 5,
    "attack": 7
}
boss = {
    "hp": 25,
    "def": 10,
    "attack": 10
}
current_room = "start"



################### Step 2: Functions ##########################
# Combat function
def combat(player, enemy):
    turn = random.choice(["player", "enemy"])
    #in a while true loop
    if turn == "player":
        #give your user options of things to do (at least 3)
        enemy["hp"] -= player["attack"]
    else:
        player["hp"] -= enemy["attack"]
    # Break when one of them are at 0 HP and return both player and enemy 
    return player, enemy

# Room 1 (start room)
    #must explain what happens in this room
    return "well"

# Room 2 (Wishing Well) 
    #to call combat
    player, goblin = combat(player, goblin)


################### Step 3: While True loop #####################

#conditional that checks the current room
#update current room by calling the correct room function
##### EXAMPLE
if current_room == "start":
    current_room = start()
elif current_room == "combat":
    current_room = combat_1(player, goblin)
