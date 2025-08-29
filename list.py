#Any app should be able to perform CRUD - Creat, Retrieve, Update, Delete
# # A List ia a CSV - Comma Separated Value
name1 = "kamsi"
name2 = "justina"
name3 = "despina"

classNames = ["kamsi","justina", "despina", "ohakwe", "nenye", "chidinmma"]
print(len(classNames))

#Print thev values according to the index
print(classNames[2])
print(classNames[1])
print(classNames[0])

name = "kamsi"
height = 5.6
gender = "female"
isMarried = False
myDetails = ["kamsy", 5.6, "female", False]

construct = list(("kamsy", 5.6, "female", False,))

print(type(construct))
print(len(construct))
print(construct)


# name = input("enter your name: ")
# height = float(input("enter your height: "))
# gender = input("what's your gender: ")
# isMarried = bool(input("are you married? True or False: "))
# myDetails = ["kamsy", 5.6, "female", False]

# con = list((name1, height, gender, isMarried))

#method
# print(myDetails[4])

#Using a negative index number will start count from the back(ie. - from right to left)
print(myDetails[-2])


