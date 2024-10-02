name = 'David' #Since we have defined the name outside any function it belongs to global scope. Hence it can be access anywhere
count = 1

#def greeting():
#  colour = 'blue'
#  print(colour)
#  print(name)

#greeting()
#print(color) #We will get an error heare. Because color is defined inside the function and it belongs to local scope of the function. Hence it can only be accessed inside it's local scope

def greeting(name):
  greeting = 'Hello'
  print(greeting +' ' + name)

greeting('Jhon')

#In above function parameter 'name' will be used inside the function istead of the global scope's 'name'

def another_func():
  greeting('William')

another_func()

#In above scenario since the greeting function is defined in the global scope it can be accessed in inside another function
#If greeting function is defined inside the another_func then it can't be accessed outside the another_func 
#we can re define a name of a variable that is already defined in the global scope, inside local scope
#In order to access a global variable inside a function we have o use the global keyword
def new_func():
  global count
  count += 1
  print(count)

new_func()