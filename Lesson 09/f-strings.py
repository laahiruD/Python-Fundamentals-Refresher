#ways to print in python
person = 'Dave'
coins = 3

print(person + ' has ' + str(coins) + ' coins left')

message1 = '%s has %s coins left.' % (person, coins)
print(message1)

message2 = '{} has {} coins left.'.format(person,coins)
print(message2)

message3 = '{1} has {0} coins left.'.format(coins, person)
print(message3)

message4 = '{person} has {coins} coins left.'.format(coins = coins, person = person)
print(message4)

#using dictionary
player = {'person':'Dave', 'coins':3}
message5 = '{person} has {coins} coins left.'.format(**player)
print(message5)

#using  f strings
message6 = f'{person} has {coins} coins left.'
print(message6)

message7 = f'{person.lower()} has {2*9} coins left.'
print(message7)

num = 10
print(f'2.25 times {num} is {2.25 * num:.2f}') #using formatting options in a f string
#you can use w3schools for more formatting options
