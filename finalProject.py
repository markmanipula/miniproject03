#!/usr/bin/python3

"""Author - Mark Manipula
   Purpose is to add more (fun) functionality to the code   
   skeleton code by Chad"""

import os
import random

#to clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

stalkerRoom = ""

def stalkerTeleport():
      #global variable here so the main function can read it
      global stalkerRoom
      #moves the stalker around the map
      move = random.randint(0,9)
      if move == 0:
            stalkerRoom = "Hall"
      elif move == 1:
            stalkerRoom = "Kitchen"
      elif move == 2:
            stalkerRoom = "Dining Room"
      elif move == 3:
            stalkerRoom = "Garden"
      elif move == 4:
            stalkerRoom = "Pantry"
      elif move == 5:
            stalkerRoom = "Basement"
      elif move == 6:
            stalkerRoom = "Bedroom"
      elif move == 7:
            stalkerRoom = "Bathroom"
      elif move == 8:
            stalkerRoom = "Attic"

      print(f"Your stalker now is in the {stalkerRoom}")

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  stalkerTeleport()
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
            #Hall is the starting point
            'Hall' : {
                  'north' : 'Attic',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west' : 'Bedroom',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'south' : 'Basement',
                  'west' : 'Bathroom',
                },

            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },

            'Garden' : {
                  'north' : 'Dining Room'
               },

            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },

            'Basement' : {
                  'north' : 'Kitchen'
            },

            'Bedroom' : {
                  'east' : 'Hall',
                  'south' : 'Bathroom'
            },

            'Bathroom' : {
                  'north' : 'Bedroom',
                  'east' : 'Kitchen',
            },

            'Attic' : {
                  'south' : 'Hall'
            }
         }

#start the player in the Hall
currentRoom = 'Hall'
         
#creates a stalker and youre in the same room with the stalker, you deeeed
#stalker can teleport

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  #stalker will move now move = random.randint(0,4)
  stalkerTeleport()
  
  if currentRoom == stalkerRoom:
        print("Your stalker appeared! and killed you...")
        break
  
  cls()