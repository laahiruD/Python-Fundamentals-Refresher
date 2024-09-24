#creating a list
users = ['Dave', 'Jhon', 'Sara'] #It doesn't have to be the same data type inside a list
usersList = list(["David", "Alex", "Bill"]) #using list constructor

#checking if a value is in a list
print("Dave" in users)

#Accessing a value based on the position of the value
#Positions starts with 0 and -1 can be used for access the last position
print(users[1])

#Finding the position of the specific value
print(users.index('Jhon')) 

#Getting values for a range of positions
print(users[0:2])

#Findinf the length of the list
print(len(users))

#Add more items to list
users.append("Emily")

# Add anothe list to existing list
users += ["Vick", 'Harry'] #use [] here. If not each letter will count as a single item
users.extend(["Williom",'Zack'])

#add item to a certian place of a list
users.insert(2, "Neil") 
users[1:3] = ["Ann", "Graham"] #This will replace the current items of the specified location with the given items

#Removing values
users.remove("Dave")

#We can use the pop method as well. It will return the last item of the list and remove it from the list as well
print(users.pop())

#Delete Using del keyword
del users[3]
#del users -> this will delete the whole list
#users.clear() #This will remove all the items in the list while keeping the empty list

#Sorting the list
users.sort()
print(users)

#Make a copy of a list
usersCopy1 = users.copy()
usersCopy2 = list(users)
usersCopy3 = users[:]


#Tuples
#Tuples are very much simmilar to list. Main differences are data type of the items in a tuple is same for each item and 
#order of the items will not change

#create a tuple
myTuple = tuple((1,2,3,4,5)) #Using constructor
myTuple2 = ("A","B","C")

#unpack a tuple
(one, two, three, *remaining) = myTuple
