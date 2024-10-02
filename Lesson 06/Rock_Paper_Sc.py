import sys
import random
from enum import Enum

def play_rps():
  class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

  playerInput = input("Please Enter... \n 1 for Rock, \n 2 for Paper, or \n 3 for scissors:\n\n")
  
  if playerInput not in ['1', '2', '3']:
    return play_rps()
  
  intplayer = int(playerInput)
  computerInput = random.choice("123")
  intComp = int(computerInput)

  print('You Enterd:' + str(RPS(intplayer)).replace('RPS.', ''))
  print("Computer Choose: " + str(RPS(intComp)).replace("RPS.", ""))

  if intplayer == 1 and intComp == 3:
    print("🎉 You won!!!")
  elif intplayer == 2 and intComp == 1:
    print("🎉 You won!!!")
  elif intplayer == 3 and intComp == 2:
    print("🎉 You won!!!")
  elif intplayer == intComp:
    print("😲 Tie Game!")
  else:
    print("😢 Computer Won")

  print('Play Again?')

  while True: 
    playAgain = input("\nType Y for yes or Q for quit \n")
    if playAgain.lower() not in ['y','q']:
      continue
    else:
      break
      
  if(playAgain.lower() == "y"):
        return play_rps()
  else:
    print("\nThank you for playing!!!")
    sys.exit("Bye👋")


play_rps()