#!/usr/bin/env python3

''' My RPG game in my NAPYA class '''

def showInstructions():
    print('''
    RPG Game
    ** Your task is to escape the house with the key and the potion **
    --------
    Commands:
        go [direction]
        get [item]
    --------
    ''')

def showStatus(): # Displays the players status
    print('====================')
    print('You are in the ', currentRoom)
    # Show inventory
    print('Inventory : ', str(inventory))
    # Show item if one is in the room
    if 'item' in rooms[currentRoom]:
        print('You see a', rooms[currentRoom]['item'])
    print('====================')

# Init an empty list
inventory = []

# create our world and its rooms
rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'east' : 'Dining Room',
            'item' : 'key',
                },
        'Kitchen' : {
            'north' : 'Hall',
            'east' : 'Den',
            'item' : 'monster',
                    },
        'Den' : {
            'west' : 'Kitchen',
            'north' : 'Dining Room',
            'south' : 'Garden',
            'item' : 'chad',
                },
        'Dining Room' : {
            'south' : 'Den',
            'west' : 'Kitchen',
            'north' : 'Pantry',
            'item' : 'potion',
                    },
        'Garden' : {
            'north' : 'Den',
                    },
        'Pantry' : {
            'south' : 'Dining Room',
            'item' : 'cookie',
                    },
        }
# Player start location
currentRoom = 'Hall'

# Show instructions to the player
showInstructions()

# Create an infinite loop
while True:
    showStatus()
    # Ask the player what they want to do
    move = ''
    while move == '':
        move = input('>') # So long as the move does not have a value. Ask the user for input.

    move = move.lower().split() # Makes everything lowercase. Splits input into a list.

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            # If YES that direction exists, then assign your new current room to the value of the key the user has entered.
        else:
            print("\nYOU CANNOT GO THAT WAY!\n")

    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # Add item to inventory
            print('\n' + move[1] + ' received!\n') # Prints that the item was acquired
            del rooms[currentRoom]['item'] # Removed item user just picked up from the dictionary
        else:
            print("\nSorry I don't see a " + move[1] + "\n" )
    
    # Added a drop command to drop an item
    if move[0] == 'drop':
        if move[1] not in rooms[currentRoom] and move[1] in inventory:
            inventory.remove(move[1]) # Removes item from inventory
            print('You dropped the ' + move[1] )
            rooms[currentRoom].update({'item': move[1] }) # Adds item back into the dictionary
        else:
            print('\nSorry, nothing to drop!\n')
            
    # If you enter the kitchen with the cookie
    if 'cookie' in inventory and 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('The monster steals your cookie and runs away!')
        inventory.remove('cookie')
        del rooms[currentRoom]['item']

    # Going to get eaten by a monster in the Kitchen if you don't have the cookie
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('\nA monster has eaten you! GAME OVER!\n')
        break # break makes us escape the loop

    if move[0] == 'look':
        print("\nYou are in the " + currentRoom + "\n")

    # Winning scenario
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'chad' in inventory:
        print("\nSorry, you can't escape with Chad! He must remain in the house. Please drop him like it's hot\n")

    elif currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("\nYou have escaped with they key and magic potion while leaving Chad to fend for himself. YOU WIN!\n")
        break

    else:
        print("\nYou are in the garden but need some items to escape!\n")






























