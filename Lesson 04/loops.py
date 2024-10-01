#While loop - Will execute a block of code while a condition is true
value = 1

# while value < 10:
#   print(value)
#   value += 1

#break and continue 
#break - will stop the exicution of the loop once break is reached
# while value < 10:
#   if value == 5:
#     break
#   print(value)
#   value += 1

#output is - 1 2 3 4

#continue - will skip to the next iteration of the loop
# while value < 10:
#   value += 1
#   if value == 5:
#     continue
#   print(value)

#output is - 1 2 3 4 6 7 8 9 10

#for loop
names = ["James", "Dave", "Anderson", "David"]

# for name in names:
#   print(name)

# for num in range(2,4):
#   print(num)

# for number in range(1,101, 5):
#   print(number)

#Nested Loops
actions = ["eats", "sleeps", "codes"]

for name in names:
  for action in actions:
    print(name + " " + action)