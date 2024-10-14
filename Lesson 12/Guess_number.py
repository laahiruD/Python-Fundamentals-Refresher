#This is a mini projec using lessons learn so far
import sys
import random

def guess_number(name='Player 01'):
  gameCount = 0
  playerWins = 0
  playerloss = 0

  def playGame():
    playerInput = input(f'Please enter your guess (should be between 1 and 3)')

    if(playerInput not in ['1', '2', '3']):
      print(f'{name}, You must enter a value between 1 and 3')
      return playGame() 
    
    playerGuess = int(playerInput)
    computerGuess = int(random.choice('123'))

    
    def decideWinner(player, computer):
      nonlocal playerWins
      nonlocal playerloss

      if(player == computer):
        playerWins +=1
        return f'🎉 {name},You won!!!'
      else:
        playerloss += 1
        return f'😢 Computer Won, sorry {name}...'

    game_result = decideWinner(playerGuess, computerGuess)
    print(game_result)

    nonlocal gameCount
    gameCount += 1

    print(f'Game Count: {gameCount}')
    print(f'{name},You  Wins: {playerWins}')
    print(f'Computer Wins: {playerloss}')
    print('Play Again?')

    while True:
      playAgain = input("\nType Y for yes or Q for quit \n")
      
      if playAgain.lower() not in ['y', 'q']:
        continue
      else:
        break
    
    if playAgain.lower() == 'y':
      return playGame()
    else:
      print("\nThank you for playing!!!")
      sys.exit("Bye👋")

  return playGame


if __name__ == '__main__':
  import argparse

  parser =  argparse.ArgumentParser(
    description = 'Provides a personalized game experience.'
  )

  parser.add_argument(
    '-n', '--name', metavar='name', required=True, help='Name of the person playing the game'
  )

  args = parser.parse_args()
  gues_num = guess_number(args.name)
  gues_num()

    