#Aibek Abasov
#10/8/2024
print("Hello World!")
#Prints the "Hello Wolrd"

name = input("What is your name?")
print("Hello," + name)
#Asks name of the user and prints Hello + his name

name = input("give me your name!")
name1 = "Aibek"
name2 = "Benjamin"
#check it if the name is the same as name1, name2 
#yes/no welcome/unwelcome them
if name == name1:
    print("Welcome Back!")
if name == name2:
    print("Welcome Back!")
else:
    print("Unauthorized use")

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")
#Ask user to enter the radius
#Using the radius calculate the area
