from random import choice

capital = 'Colombo'
flower = 'water lily'

def randomFunFact():
  funFats = [
    'Pearl of the Indian Ocean & Teardrop of India',
    'The Sri Lankan head waggle',
    'Adam\’s Peak',
    'Cinnamon\’s origins'
  ]

  print(funFats[int(choice('0123'))])

  