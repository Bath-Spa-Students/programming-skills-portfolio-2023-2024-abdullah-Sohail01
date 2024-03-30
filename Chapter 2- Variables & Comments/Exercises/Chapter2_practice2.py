# Exercise 1: Assigning a message to the variable and printing the message.
print("\n\n\n\n ---------> Question1: <---------")

name="Abdullah Sohail"
print(name)
Address="Sharjah"
print(Address)




# Exercise 2: a quote from a famous person i admire.
print("\n\n\n\n ---------> Question2: <---------")

message=""" Quaid-e-Azam once said, "Think a hundred times before you take a decision, but once that decision is taken, stand by it as one man." """
print(message)




# Exercise 3: Stripping Names:
print("\n\n\n\n ---------> Question3: <---------")

NaMe = "\t Abdullah Sohail \n"

print(f'Original: {NaMe}')
print(f'lstrip(): {NaMe.lstrip()}')
print(f'rstrip(): {NaMe.rstrip()}')
print(f'strip(): {NaMe.strip()}')




# Exercise 4: Favorite Number:
print("\n\n\n\n ---------> Question4: <---------")

MyFavoriteNumber = 10
print('My Favorite number is',MyFavoriteNumber)



# Exercise 5: USB Shopper:

print("\n\n\n\n ---------> Question5: <---------")

Money_Available = 50
Per_piece_price = 6

NumberofUSBsticks = Money_Available // Per_piece_price
MoneyRemaining = Money_Available % Per_piece_price

print('The Girl can purchase', NumberofUSBsticks , 'USB Sticks.')
print('She will be left with',MoneyRemaining, 'Pounds.')