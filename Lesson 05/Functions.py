#fUNCTIONS are reusable blocks of codes

#defining a function
def addition(num1, num2):
  return num1+num2

#calling the function
total = addition(2,8)

#In the addition function num1 and num2 are parameters and two numbers that passed(2 and 8) are the arguments
#We can also set default values for parameters of a function like (num1=0, num2=2)
#We also can check the type of the parameters and accept or reject them based on a logic
#Furthemore it is not a necceasarry to return somthing from a function as well

#if there are multple parameters it can be used like following
def multiple_args(*args): #args is not a keyword here 
  print(args)