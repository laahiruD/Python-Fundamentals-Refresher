import sys
import random
from enum import Enum

game_count = 0

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

  def decide_winner(player, computer):
    if intplayer == 1 and intComp == 3:
      "🎉 You won!!!"
    elif intplayer == 2 and intComp == 1:
      "🎉 You won!!!"
    elif intplayer == 3 and intComp == 2:
      "🎉 You won!!!"
    elif intplayer == intComp:
      "😲 Tie Game!"
    else:
      "😢 Computer Won"

  game_result = decide_winner(intplayer,intComp)
  print(game_result)
  global game_count
  game_count += 1

  print('Game Count:' + ' ' + str(game_count))
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