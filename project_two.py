#!/usr/bin/ env python3

import crayons

def showInstructions():
    """Game intsructions for user to follow"""
    #print a main menu and the commands
    print(crayons.green('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    '''))

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print(crayons.green('You are in the ' + currentRoom))
    
    #prints item the player has
    print(crayons.blue('Inventory:', inventory))
    # Print item in current room
    if "item" in rooms[currentRoom]:
      print(crayons.red('You see a ' + rooms[currentRoom]['item']))
      
    print("---------------------------")


# list of inventory which is empty
inventory = []

# a dictionary of all the rooms which are linked together
rooms = {

            'Hall' : {
                  'south': 'Kitchen',
                  'east' : 'Dining Room',
                  'west' : 'Living Room',
                  'north': 'Media Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north': 'Hall',
                  'item' : 'monster'
                },

            'Dining Room' : {
                  'west' : 'Hall',
                  'north' : 'Bathroom one',
                  'item' : 'potion'
             },

             'Living Room' : {
              'east' : 'Hall',
              'item' :'gold'

             },

             'Media Room' : {
              'south' : 'Hall'
              
             },

             'Bathroom one' : {
              'south' : 'Dining Room',
              'west' : 'Bedroom one',
              'east' : 'Bedroom two',
              'item' : 'map'
             },

             'Bedroom one' : {
              'east' : 'Bathroom one',
              'item' : 'wand'
              
              },

              'Bedroom two' : {
                'west' : 'Bathroom one',
                'north' : 'Bathroom two',
                'item'  : 'health'
              },

              'Bathroom two' : {
                'north' : 'Bedroom two',
                'south' : 'Sun Room'

              },

              'Sun Room': {
                'north' : 'Bathroom two',
                 'west' : 'Office'
              },

              'Office' : {
                'east' : 'Sun Room',
                'north': 'Room with Trap Door'

              },

              'Room with Trap Door' : {
                'east' : 'Tunnel'
              },

              'Tunnel' : {
                'west' : 'Room with Trap Door',
                'item' : 'teleport'

              }
        }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    #player input
    move = ''
    while move == '':  
        move = input('>')

    # .lower() to convert input into lowercase and .split() to turn it into a list      
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
       
        else:
            print(crayons.red('You can\'t go that way!'))

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(crayons.green(move[1] + ' got!'))
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        else:
            #tell them they can't get it
            print(crayons.red('Can\'t get ' + move[1] + '!'))

     #shows how a player can lose
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print(crayons.red('A monster has got you... GAME OVER!'))
        break 

          #shows how a player wins
    if currentRoom == 'Sun Room' and 'key' in inventory and 'gold' in inventory:
        print(crayons.red('You escaped the house with the ultra rare key and magic potion... YOU WIN!'))
        break
      
    #shows how a player can move to any room from their current location
    if currentRoom == 'Tunnel' and 'teleport' in inventory:
        
        #prints a list of all the rooms
        print(crayons.red(rooms.keys()))

        #user input to choose a room they want to move to 
        choice = input(crayons.green("Choose a room: "))
        currentRoom = choice
  

      


