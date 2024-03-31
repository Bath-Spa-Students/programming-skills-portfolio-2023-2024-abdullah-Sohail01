






#Q1: 
print("\n\n ---------> Question1: <---------")


def display_message():
       print("In this chapter, I will be learning about functions in Python.")

display_message()




#Q2: 
print("\n\n ---------> Question2: <---------")

def favorite_book(title):
      print(f"{title} is my favorite book")

favorite_book("Wimpy-Kid")











# #Q3: 
print("\n\n ---------> Question3: <---------")

def make_shirt(size,message):
     print(f"The Shirt size is ({size}) and the Message is: {message} ")

make_shirt("Large","BATHSPA")
make_shirt(size="XXL",message="Introduction to Programming")    






#Q4: 
print("\n\n ---------> Question4: <---------")

def make_shirt(size="Large",message="I Love Python "):
      print(f"The Shirt size is ({size}) and the Message is: {message} ")

make_shirt()
make_shirt("Medium")
make_shirt("XL","Abdullah Sohail")   
    

#Q5: 
print("\n\n ---------> Question5: <---------")

def cities(city,country="England"):
     print(f"{city} is in {country}")

cities("Bath")
cities("Peshawar","Pakistan")
cities("Toronto","Canada")    
