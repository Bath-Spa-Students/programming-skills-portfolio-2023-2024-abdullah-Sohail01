# Qustion1: Print Strings.

print("Question1:")
print('''\nTwinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are ''')



# Question2: Print the Version of Python 

import sys
print("\n\nQuestion2:")
print("\nPython version=",sys.version)

# Question3: Print date and Time 

from datetime import datetime

today=datetime.today()
print("\n\nQuestion3:")
print("\nToday's date and time:",today)


#Question4: Strings Concatination 

Firstname="Abdullah"
Middlename="Mohammad"
Lastname="Sohail"
print("\n\n Question4:")
print("\n")
print(Firstname + Middlename + Lastname)


#Question5:Compute area of Circle 

import math

def circle_area(radius):

 return math.pi * radius**2

print("\n\n Question5:")
radius = float (input ("\n Enter the radius of the circle:"))

area= circle_area(radius)

print("The area of the circle with radius" , radius, "is:", area) 
