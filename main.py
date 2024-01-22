#Vlad Calin & Desmond Lassaline
#RST - Adventure Game
#January 17, 2024

import sys
import time as t

#Creates all variables that are used in the program
action = 0
beenInR2 = False
beenInR1 = False
beenInUpstairs_hallway = False
beenInUpstairs_room = False
beenInBasement = False
have_ladder = False
have_jello = False
have_toaster = False
have_crowbar = False
have_cross = False

#Those are lists of items in the rooms that are able to be explored in the game. Those lists make sure that a player is allowed or not to use certain objects in certain rooms
AllItems = ['flashlight','batteries','ladder','jello','keys','toaster','crowbar','cross']
room = 'r1'
r1list = ['cabinet','ceiling','light','ladder', 'safe']
r2list = ['jello', 'oven', 'keys', 'toaster']
upstairs_hallway_list = ['door']
upstairs_list = ['cabinet', 'bath', 'crack', 'elevator']
basement_list = ['coffin']
commands = ['help','inventory','getAllItems']
inventoryV = ['nothing'] #This is the inventory list. As the user discovers more items in the game, they are added to this list
flashlight = 'off'
cabinet = 'full'
inventoryLoopRepeater = False
HaveLadder = False

# Function to get room description and print it with colors
def getRoomDescription():
  print('\033[32m\033[3m')
  global beenInR1
  global beenInR2
  global beenInUpstairs_room
  global beenInUpstairs_hallway
  global beenInBasement
  global room

  #ROOM #1
  if room == 'r1': #if the user is in room #1, then the lines below are executed
    if beenInR1 == False: #if the user has not been in room 1 before, then this long descriptive message appears
      print("You are in the only lighted room in the house. Your neighbors have told you that there is a power outage in your area, so you immediately came home to seen it. The fact that the entrance is the only room in your with electricity is strange. The rest of the rooms are all dark. In order for you to see in them, you need a flashlight. There is water dripping from the ceiling where a battery functioning light lights up the room, a ladder and a cabinet are right next to you as well as a safe in the corner of the room. There is a door leading forwards.")
      beenInR1 = True
    else: #if the user has been in room 1 before, and they return in this room, they are going to get a less descriptive message
      if ('ladder' not in inventoryV) and (flashlight == 'off'): #depending on what items the user has picked up from the room, the messages are going to be slightly different
        print("There is water dripping from the ceiling where a battery functioning light lights up the room, a ladder and a cabinet are right next to you as well as a safe in the corner of the room. There is a door leading forwards")
        gameLoop()
      elif ('ladder' in inventoryV) and (flashlight == 'off'):
        print(print("There is water dripping from the ceiling where a battery functioning light lights up the room, a cabinet is right next to you as well as a safe in the corner of the room. There is a door leading forwards"))
        gameLoop()
      elif flashlight == 'on':
        print(print("There is water dripping from the ceiling where a battery functioning light lies dormant, a cabinet is right next to you as well as a safe in the corner of the room. There is a door leading forwards"))
        gameLoop()

  #ROOM #2
  elif room == 'r2': #if the user is in room #2, then the lines below are executed
    if beenInR2 == False: #if the user has not been in room 2 before, then this long descriptive message appears
      if flashlight == 'off':
        print("You entered the darkness. You can't see anything. It's almost like you need light. Hint hint.")
        gameLoop()
        beenInR2 = True
      else:
        print("Because of the flashlight, you can see everything in the room. This is the kitchen. You remember that you left your keys in jello last night, the jello getting hard and your keys being blocked there. You need to heat up the jello in order to get the keys out. There is a gas oven in front of you, as well as a toaster. There is also stairs leading upstairs and a door leading backwards")
        beenInR2 = True
        gameLoop()
    else: #if the user has been in room 2 before, and they return in this room, they are going to get a less descriptive message
      if flashlight == 'off':
        print("You entered the darkness. You can't see anything. It's almost like you need light. Hint hint.")
        gameLoop()
      elif ('keys' not in inventoryV) and ('toaster' not in inventoryV): #depending on what items the user has picked up from the room, the messages are going to be slightly different
        print("This is the kitchen. You remember that you left your keys in jello last night, the jello getting hard and your keys being blocked there. You need to heat up the jello in order to get the keys out. There is a gas oven in front of you, as well as a toaster. There is also stairs leading upstairs and a door leading backwards")
        gameLoop()
      elif ('keys' not in inventoryV) and ('toaster' in inventoryV):
        print("This is the kitchen. You remember that you left your keys in jello last night, the jello getting hard and your keys being blocked there. You need to heat up the jello in order to get the keys out. There is a gas oven in front of you. There is also stairs leading upstairs and a door leading backwards")
        gameLoop()
      elif ('keys' in inventoryV) and ('toaster' in inventoryV): 
        print('This is the kitchen there is also stairs leading upstairs and a door leading backwards')
        gameLoop()
      elif ('keys' in inventoryV) and ('toaster' not in inventoryV): 
        print('This is the kitchen. There is a toaster on the counter There is also stairs leading upstairs and a door leading backwards')
        gameLoop()


  #UPSTAIRS HALLWAY
  elif room == 'upstairs_hallway':
    if beenInUpstairs_hallway == False:
      if flashlight == 'off':
        print("You entered the darkness. You can't see anything. It's almost like you need light. Hint hint.")
        gameLoop()
      else:
        print("This is the hallway from upstairs. There is only one room here. There is a door in front of you and one going backwards.")
        beenInUpstairs_hallway = True 
        gameLoop()
    elif (beenInUpstairs_hallway == True) and (beenInUpstairs_room == False):
      if flashlight == 'off':
        print("You entered the darkness. You can't see anything. It's almost like you need light. Hint hint.")
        gameLoop()
      else:
        print("This is the hallway from upstairs. There is only one room here. There is a door in front of you and one going backwards.")
        gameLoop()
    else:
      room = 'upstairs_room'
      getRoomDescription()


  #UPSTAIRS ROOM
  elif room == 'upstairs_room': #if the user is in the room upstairs, then the lines below are executed
    if beenInUpstairs_room == False: #if the user has not been in the room upstairs before, then this long descriptive message appears
      if flashlight == 'off':
        print("You entered the darkness. You can't see anything. It's almost like you need light. Hint hint.")
        gameLoop()
      else: #if the user has been in the room upstairs before, and they return in this room, they are going to get a less descriptive message
        print("This is the bathroom. There is a cabinet next to you and also, a bath in front of you. As you look around, you see a crack in you ceiling. That wasn't there before. Weird. You start to think that you have to go to your basement in order to turn on the electricity. In this bathroom, there is a dummy elevator. You lost the keys for this elevator, so you need to pry it open. There are also stairs going downstairs.")
        beenInUpstairs_room = True #This line sets the value of the variable to true, so that in the case of coming to this room again, the program prints the less disruptive message about the room. 
        gameLoop()
    else:
      print("You are in the bathroom, the upstairs room.")
      gameLoop()

  #BASEMENT
  elif room == 'basement':
    if beenInBasement == False:
      print("This is the basement. As soon as you enter, there is a weird feeling that you feel. It's just like one of those horror movies you saw on Netflix. After looking around for a couple of seconds, you see a coffin in the middle of the room. You start approaching it.")
      beenInBasement = True
      gameLoop()
    else:
      print("You are in the basement again. The coffin is in front of you.")
      gameLoop()
  else:
    print("Error, room not found")


# Function to display help information
def help():
  print("To do anything just write the word of anything you wish to inspect or take. You can also move rooms by typing which direction you wish to go (forwards, backwards, upstairs, downstairs, or if taking an elevator, just type 'elevator'). To check inventory type ('inventory') once in inventory you type the object you wish to use then when prompted you must type the thing in the world that you want to use it on or for. ")
  gameLoop()


# Function to display inventory and handle user input
def inventory():
  print('\033[33m')
  global inventoryV
  global room
  global have_ladder, have_cross, have_crowbar, have_toaster, have_jello
  inventoryLoopRepeater = True
  while inventoryLoopRepeater:
    item = input(f"Which item in your inventory would you like to use, {inventoryV} : \033[4m\033[35m")
    print('\033[33m\033[24m')
    if item == 'nothing':
      break
    elif item not in inventoryV:
      print('please enter a valid item')
      continue
    useOn = input("What would you like to use it on: \033[4m\033[35m")
    print('\033[24m\033[32m\033[3m')

    #ROOM #1
    if room == 'r1':
      if useOn not in r1list:
        print("please enter a valid option")
        continue
      else:
        if item == 'ladder' and useOn == 'light':
          print("The batteries fall into the palm of your hand and you put them away")
          print('batteries added to inventory')
          inventoryV = inventoryV + ['batteries']
          break
        elif item == 'keys' and useOn == 'safe' and have_crowbar == False:
          print('You open the safe and inside is a crowbar which you take')
          print('crowbar added to inventory')
          inventoryV = inventoryV + ['crowbar']
          have_crowbar = True
          break
        else:
          print('there is nothing to do')
          break

    #ROOM #2
    elif room =='r2':
      if useOn not in r2list:
        print("please enter a valid option")
        continue
      else:
        if item == 'jello' and useOn == 'oven' :
          print("The jello got slushy enough that the keys got out and slid in your pocket")
          print("Keys added to inventory")
          inventoryV += ['keys']
          del inventoryV[inventoryV.index('jello')]
          break
        else:
          print("There is nothing to do!")
          break


    #UPSTAIRS HALLWAY
    elif room == 'upstairs_hallway':
      if useOn not in upstairs_hallway_list:
        print("please enter a valid option")
        continue
      else:
        if item == 'keys' and useOn == 'door':
          print("You opened the door and entered the room!")
          room = 'upstairs_room'
          getRoomDescription()
        else:
          print("There is nothing to do!")
          break

    #UPSTAIRS ROOM
    elif room == 'upstairs_room':
      if useOn not in upstairs_list:
        print("please enter a valid option")
        continue
      else:
        if item == 'ladder' and useOn == 'crack' and have_cross == False:
          print("You just got a cross! ✟")
          inventoryV += ['cross']
          have_cross = True
          break
        elif item == 'ladder' and useOn == 'crack' and have_cross == True:
          print("You already got the cross!")
          break
        if item == 'toaster' and useOn == 'bath':
          print("You die. Bye bye.")
          sys.exit(1)
        if item == 'crowbar' and useOn == 'elevator':
          print("You took the elevator! You are in the basement")
          room = 'basement'
          getRoomDescription()
          break
        else:
          print("There is nothing to do")
          break

    #BASEMENT
    elif room == 'basement':
      if useOn not in basement_list:
        print("please enter a valid option")
        continue
      else:
        if item == 'cross' and useOn == 'coffin':
          print("You banished the vampire! Congratulations, you finished the game!")
          sys.exit(1)
        elif item == 'cross' and useOn == 'vampire':
          print("You banished the vampire! Congratulations, you finished the game!")
          sys.exit(1)
        else:
          print("There is nothing to do")
          break

# Function to handle user actions based on the current room
def turnAction(act):
  global inventoryV
  global room
  global have_ladder, have_cross, have_crowbar, have_toaster, have_jello

  #ROOM #1
  if room == 'r1':
    if act in commands:
      if act == 'help':
        help()
      elif act == 'inventory':
        inventory()
        gameLoop()
      elif act == 'getAllItems':
        inventoryV = inventoryV + AllItems
        gameLoop()
    elif act in r1list:
      if act == 'ladder' and have_ladder == False:
        inventoryV = inventoryV + ['ladder']
        print('ladder added to inventory')
        have_ladder = True
      else:
        print("You already have a ladder!")
      if act == 'light':
        print("This is a battery powered light, it is too high for you to reach")
      if act == 'ceiling':
        print("The ceiling is dripping with water... strange...")
      if act == 'cabinet':
        print('You open the cabinet and you see a flashlight without batteries, you pick it up')
        print('flashlight added to inventory')
        inventoryV = inventoryV + ['flashlight']
      if act == 'safe':
        print("safe is locked")
      gameLoop()
    elif act == 'forwards':
      room = 'r2'
      getRoomDescription()
    else:
      print('Sorry, that is not a valid command, try again.')
      gameLoop()


  #ROOM #2
  if room == 'r2':
    if act in commands:
      if act == 'help':
        help()
      elif act == 'inventory':
        inventory()
        gameLoop()
    elif act in r2list:
      if act == 'jello' and have_jello == False:
        inventoryV = inventoryV + ['jello']
        print('jello added to inventory')
        have_jello = True
      elif act == 'jello' and have_jello == True:
        print("You already got the jello!")
      if act == 'oven':
        print("This is a gas oven.")
      if act == 'toaster' and have_toaster == False:
        print("This is a battery functioning toaster, you pick it up")
        print("Toaster added to inventory")
        inventoryV += ['toaster']
        have_toaster = True
      elif act == 'toaster' and have_toaster == True:
        print("You already have the toaster!")
      gameLoop()
    elif act == 'backwards':
      room = 'r1'
      getRoomDescription()
    elif act == 'upstairs':
      room = 'upstairs_hallway'
      getRoomDescription()
    else:
      print('Sorry, that is not a valid command, try again.')
      gameLoop() 


  #UPSTAIRS HALLWAY
  if room == 'upstairs_hallway':
    if act in commands:
      if act == 'help':
        help()
      elif act == 'inventory':
        inventory()
        gameLoop()
      else:
        print("Enter a valid action!")
        gameLoop()
    elif act == 'downstairs':
      room = 'r2'
      getRoomDescription()
    elif act == 'door':
      print("The door is locked, it looks like you'll need a key to access it.")
      gameLoop()
    else:
      print("Enter a valid action!")
      gameLoop()


  #UPSTAIRS ROOM
  if room == 'upstairs_room':
    if act in commands:
      if act == 'help':
        help()
      elif act == 'inventory':
        inventory()
        gameLoop()
    elif (act in upstairs_list) and (beenInBasement == False):
      if act == 'cabinet':
        print("This is an empty cabinet. There is nothing inside")
      elif act == 'crack':
        print("This is a big crack in the ceiling. Oh there is something glowing there. It is to high to reach.")
      elif act == 'bath':
        print("This is a bath")
      elif act == 'elevator' and (beenInBasement == False):
        print("This is a dummy elevator. You need something to break the door.")
      gameLoop()
    elif (act in upstairs_list) and (beenInBasement == True):
      if act == 'cabinet':
        print("This is an empty cabinet. There is nothing inside")
      elif act == 'crack':
        print("This is a big crack in the ceiling. Oh there is something glowing there. It is to high to reach.")
      elif act == 'bath':
        print("This is a bath")
      elif act == 'elevator' and (beenInBasement == True):
        room = 'basement'
        getRoomDescription()
      gameLoop()
    elif act == 'downstairs':
      room = 'r2'
      getRoomDescription()
    else:
      print('Sorry, wrong room.')
      gameLoop()

  #BASEMENT
  if room == 'basement':
    if act in commands:
      if act == 'help':
        help()
      elif act == 'inventory':
        inventory()
        gameLoop()
    elif act in basement_list:
      if act == 'coffin':
        print("You opened the coffin. There is a vampire inside! Oh no! Vampires are your biggest fear since you were a child. As you grew up you were comforted by the idea that they do not truly exist. So now, you are shocked to see one in real life.")
        gameLoop()
    elif act == 'elevator':
      print("You took the elevator and went upstairs")
      room = 'upstairs_room'
      getRoomDescription()
    else:
      print("Sorry, wrong room")
      gameLoop()

# Main game loop. When this function is called during the program, it asks the user what they want to do next, in order for the game to continue
def gameLoop():
  global flashlight
  print()

  if 'batteries' in inventoryV and 'flashlight' in inventoryV and flashlight != 'on':
    print("You take out the batteries and put them in the flashlight which immediately turns on, now you should be able to go into areas that were too dark before.")
    flashlight = 'on'
    print()

  action = input("\033[31m\033[23m what would you like to do: \033[4m\033[35m")
  print('\033[24m\033[34m')
  turnAction(action)

# Welcome message and initial description of the game, how it works
print("Welcome to Adventure in the House of Vladmond! This is a text based adventure game where your job is to banish the evil vampire Vladmond. To do this you’ll need to find a cross as well as his coffin. Then you will need to lure him there and banish him. To do anything just write the word of anything you wish to inspect or take. You can also move rooms by typing which direction you wish to go, you can also open your inventory and type HELP for any further assistance. Good luck!")
print()

gameNotStart = True

while gameNotStart:
  start = input("\033[31m To start the game PRESS ENTER: \033[38m")
  if start == '':
    for i in range(50):
      print('/')
      t.sleep(0.01)
    getRoomDescription() #This line gets the user to run this function in order for the game to start and continue
    gameLoop()
    break
  else:
    continue