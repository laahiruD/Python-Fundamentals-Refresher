#Rock Paper Scessors using oython loops

import random
import sys
from enum import Enum

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCESSORS = 3

playAgain = True

while playAgain:
  playerInput = input("Please Enter... \n 1 for Rock, \n 2 for Paper, or \n 3 for scissors:\n\n")
  intplayer = int(playerInput)
  computerInput = random.choice("123")
  intComp = int(computerInput)

  if intplayer > 3 or intplayer < 1:
    sys.exit("Please select a value between 1 and 3") 

  print("You Choose: " + str(RPS(intplayer)).replace("RPS.", ""))
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

  playAgain = input("\n You want to play again? Type Y for yes or any other letter for quit \n")

  if(playAgain.lower() == "y"):
    continue
  else:
    print("Thank you for playing!!!")
    playAgain =  False #break keyword would also end the loop

sys.exit("Bye👋")