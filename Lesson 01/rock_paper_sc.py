import random
import sys
from enum import Enum

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCESSORS = 3

player_input = input("Enter... \n 1 for Rock, \n 2 for Paper, or \n 3 for scissors:\n\n")
computer_input = random.choice("123")

player = int(player_input)
computer = int(computer_input)

print("\nYou Chose :" + str(RPS(player)).replace('RPS.',''))
print("Computer Chose :" + str(RPS(computer)).replace('RPS.',''))

if player <1 or player >3:
  sys.exit("\nPlease enter a value between 1 and 3!") 

if player == 1 and computer == 3:
  print("🎉You Won!!!")
elif player == 2 and computer == 1:
  print("🎉You Won!!!")
elif player == 3 and computer == 2:
  print("🎉You Won!!!")
elif player == computer:
  print("😲 Game Tie!!!")
else:
  print("😢 Computer Won!!!")