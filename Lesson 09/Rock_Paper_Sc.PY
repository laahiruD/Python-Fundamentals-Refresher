import sys
import random
from enum import Enum

def rps():

  game_count = 0
  playerWins = 0
  compWins = 0

  def play_rps():
    nonlocal playerWins
    nonlocal compWins
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

    print(f'You Enterd:{str(RPS(intplayer)).replace('RPS.', '')}')
    print(f'Computer Choose: {str(RPS(intComp)).replace("RPS.", "")}')

    def decide_winner(player, computer):
      nonlocal playerWins
      nonlocal compWins

      if intplayer == 1 and intComp == 3:
        "🎉 You won!!!"
        playerWins += 1
      elif intplayer == 2 and intComp == 1:
        playerWins += 1
        return "🎉 You won!!!"
        
      elif intplayer == 3 and intComp == 2:
        playerWins += 1
        return "🎉 You won!!!"
       
      elif intplayer == intComp:
        return "😲 Tie Game!"
      else:
        compWins += 1
        return "😢 Computer Won"
        
    game_result = decide_winner(intplayer,intComp)
    print(game_result)
    nonlocal game_count
    game_count += 1

    print(f'Game Count: {str(game_count)}')
    print(f'Player Wins: {str(playerWins)}')
    print(f'Computer Wins: {str(compWins)}')
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

  return play_rps

play = rps()
play()