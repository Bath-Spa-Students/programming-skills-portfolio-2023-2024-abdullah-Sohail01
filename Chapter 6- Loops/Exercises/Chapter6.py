#Q1: 
print("\n\n ---------> Question1: <---------")
print("\n\n <------((PIZZA TOPPING SECTION))------>")

while True:
     topping = input("\nEnter a Pizza topping of your wish (type <---:('quit'):---> to finish ):")

     if topping == 'quit':
         print("Quiting the topping section. Have a nice day and enjoy your pizza with your fav toppings :) .")

         break

     print(f"We will add {topping} to your pizza.")







#Q2: 
print("\n\n ---------> Question2: <---------")
print("\n\n <------((MOVIE TICKET SECTION))------> ")

while True:

  Age = input("\n Enter your Age (or Enter 'quit' to exit):")

  if Age.lower() == 'quit':
  
   break 
 
  Age = int(Age) 
  if Age < 3:
   print("YOUR TICKET IS FREE .")

  elif 3 <= Age <=12:
  
   print("YOUR TICKET COSTS $10.")

  else:
  
   print("YOUR TICKET COSTS $15.")










#Q4: 

print("\n\n ---------> Question4: <---------")


sandwich_orders = ['Angus Beef', 'Peri-Peri-Chicken', 'Minced Beef', 'Egg & Cheese']
finished_sandwiches = []

while sandwich_orders:
     current_sandwich = sandwich_orders.pop(0)
     print(f"I have made your {current_sandwich} sandwich.")
     finished_sandwiches.append(current_sandwich)

print("\n<< Finished Sandwiches >>")
for sandwich in finished_sandwiches:
   print(sandwich)






 #Q5: 

print("\n\n ---------> Question5: <---------")

sandwich_orders = ['pastrami', 'Angus Beef', 'pastrami', 'Peri-Peri-Chicken', 'pastrami', 'Minced Beef', 'pastrami', 'Egg & Cheese']
finished_sandwiches = []

print("\n I regret to inform you that we have Ran out of Pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n The Remaining Sandwich Orders are:")
print(sandwich_orders)


