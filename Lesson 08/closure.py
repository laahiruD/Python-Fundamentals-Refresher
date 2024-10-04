#Closure is, a function having the access to the scope of its parent function after the parent function has returned

def parent_func(player):
  coins = 3

  def play_game():
    nonlocal coins
    coins -= 1

    if coins > 1:
      print('\n' + player + ' has ' + str(coins) + ' coins left')
    elif coins == 1:
      print('\n' + player + ' has ' + str(coins)+ ' coin left')
    else:
      print('\n' + player + ' is out of coins')

  return play_game

james = parent_func('James')
emily =parent_func('emily')

james()
james()
emily()
james()