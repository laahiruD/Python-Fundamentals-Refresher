#modules can be considerd as small code libraries that are based on related features that contain functions and features
import math
print(math.pi)

#instead of importing the whole module we can import only the required part as well
from random import choice
print(choice('123'))

#we can create a alias to refer the module instead of its name
import random as rdm
print(rdm.choice('897'))

#dir function can be used to check what are available inside a module

for item in dir(rdm):
  print(item)

#use python module index to check more details about the module content

#customized module
import my_module

print(my_module.capital)
my_module.randomFunFact()

from Rock_Paper_Sc import rock_paper_scissors
rock_paper_scissors()