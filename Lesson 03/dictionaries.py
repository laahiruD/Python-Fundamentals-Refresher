#Dictionaries - Dictionaroes are used store data in key-valu pairs
#creating a dictionary
people = {
        "Name" : "Ann",
        "Age" : 21
}
#using constructor

people2 = dict(name ="graham", Age = 31)

#Access Items
print(people["Name"])
print(people.get("Name"))

#List all keys
print(people.keys())

#List all values
print(people.values()) 

#Verify a key in a dict.
print("Name" in people)

#Change Values
people2["Age"] = 36
people2.update({"Country": "England"})


#Removing Item
print(people2.pop("Age"))

#remove last key value pair added
#people2["Vehicle"] = "Car"
#people2.popitem() # Thi will return the last add key value pair as a tuple

#Delete and Clear
people2["Vehicle"] = "Car"
del people2["Vehicle"]

people2.clear() #clear all data
del people2 #delete the dict.

#Copy dictionaries
people3 = people.copy()
people3["Name"] = "David"


#using constructionr function for copying
people4 = dict(people)
people4["Name"] = "Raj"

#Nested dictionaries (Use dictionary inside a dictionary)
person1 = {
  "Name": "Susan",
  "Age" : 34
}
person2 = {
  "Name": "Andrew",
  "Age" : 28
}

Department = {
  "Manager": person1,
  "CFO": person2
}

#accessing data in nested dictionaries
print(Department["Manager"]["Name"])

####----------------------------Sets---------------------------------------####
#no duplicates are allowed in sets

#create a set
numbres = {1,2,3,4}
#using constructor function
numbres2 = set((5,6,7,8))

#Duplicates will reject while creating a set
numbres3 = {1,2,2,3}

#check if a value is in a set
print(2 in numbres)

#Add a new element
numbres.add(16)

#Add elemnts from one se to another
numbres.update(numbres2)


#merge two sets and create a new set
newNumbers = numbres.union(numbres2)

#keep only duplicates
#numbres.intersection_update(numbres3)

#keep everything except duplicates
numbres.symmetric_difference_update(numbres3)