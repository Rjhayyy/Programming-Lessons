#FORMATTED STRING
first = "Rjhay"
last = "Garcia"

name = f"{first} [{last}] is a programmer"
print(name)

#String Methods

#Length 
course = "Python for Beginners"
print(len(course))

#Uppercase and Lowercase Methods
full_Name = "Rhonel Garcia"
print(full_Name.upper())
print(full_Name.lower())

#Title and Capitalize
print(full_Name.title()) #Makes every first letter of every word capital
print(full_Name.capitalize()) #Makes only the first letter capital

#In methood
print("Rhonel" in full_Name) #Returns True if True and False if the word isnt found