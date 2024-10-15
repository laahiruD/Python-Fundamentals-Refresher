#lambda function is a single expression that returns a value.
squared = lambda num : num * num
print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(4))

addition = lambda a,b : a +b
print(addition(2,6))

########################################
#When to use : lambda is often used inside an another function

def func(x):
  return lambda num : num + x

addten = func(10)
print(addten(7))

####################################
#Higher order function : is a function that takes one or more functions as arguments or a function that reuturns a function as it's result
#below are some inbuilt higher order fuctions
#map function
numbers = [1,15,89,63,2]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

#filter function
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

#reduce function
from functools import reduce
total = reduce(lambda acc, cur: acc + cur, numbers)
print(total)

names = ['James May', 'Edward Snowden', 'Jamie Smith']

char_count = reduce(lambda acc, curr : acc + len(curr), names,0)
print(char_count)