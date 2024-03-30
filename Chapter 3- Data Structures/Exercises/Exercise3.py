











# # Question1:- Names:

# print("\n ---------> Question1: <---------")

#names = ["Ahmed","Bilal","Rafay"]
# print(names[0])
# print(names[1])
# print(names[2])






























# # Question2:- Greetings:
# names = ["Ahmed","Bilal","Rafay"]
# print("\n\n ---------> Question2: <---------")

# print("Good Morning", names[0])
# print("Good Afternoon", names[1])
# print("Good Evening", names[2])













# # Question3:- Your own List:

# print("\n\n ---------> Question3: <---------")

# transportation = ["Supra MK4","RAM TRX","Car"]

# print("My Dream Car is a", transportation[0])
# print("I would like to own",transportation[1],"Truck.")
# print("I prefer using my", transportation[2],"to go to University")






















# # Question4:- Guest List:

# print("\n\n ---------> Question4: <---------")

Guestlist = ["Rafay","Ammar","Ali"]

# print("Hi!", Guestlist[0],"Come over for dinner, and let's make some new memories together.")
# print("Hi!", Guestlist[1],"Come over for dinner, and let's make some new memories together.")
# print("Hi!", Guestlist[2],"Come over for dinner, and let's make some new memories together.")







# # Question5:- Change Guest List:


# print("\n\n ---------> Question5: <---------")

# print("Hi!", Guestlist[0],"Come over for dinner, and let's make some new memories together.")
# print("Hi!", Guestlist[1],"Come over for dinner, and let's make some new memories together.")
# print("Hi!", Guestlist[2],"Come over for dinner, and let's make some new memories together.")
# guestnotcoming = Guestlist.pop(1)

# New_Guest = "Qudoos"
# Guestlist.insert(1,New_Guest)
# print("\n I am inviting",Guestlist[1],"for dinner")
# print("Hi!",Guestlist[1] ,"Come over for dinner, and let's make some new memories together.")
# for guest in Guestlist:
#    print('Dear',guest)
# print('You are invited to dinner.')
# print('Sorry',guestnotcoming,'can not come for dinner')




























# # Exercise 6: Shrinking guests list:
# print("\n\n\n\n ---------> Question6: <---------")


# print("Hi!", Guestlist[0],"Come over for dinner, and let's make some new memories together.")
# print("Hi!", Guestlist[1],"Come over for dinner, and let's make some new memories together.")
# print("Hi!", Guestlist[2],"Come over for dinner, and let's make some new memories together.")
# guestnotcoming = Guestlist.pop(1)

# New_Guest = "Qudoos"
# Guestlist.insert(1,New_Guest)
# print("I am inviting",Guestlist[1],"for dinner")
# print("Hi!",Guestlist[1] ,"Come over for dinner, and let's make some new memories together.")
# for guest in Guestlist:
#  print('Dear',guest)
# print('You are invited to dinner.')
# print('Sorry',guestnotcoming,'can not come for dinner')

# print("Sorry, I can invite two guests for dinner due to space restrictions.")

# while len(Guestlist) > 2:

#  removed_guest = Guestlist.pop()
# print("Sorry",removed_guest,"I can not have you for dinner.")

# for guest in Guestlist:
#  print("Dear",guest,"You are still invited")

# del Guestlist [:]
# print(Guestlist)























# Exercise 7: Seeing the World:
print("\n\n\n\n ---------> Question7: <---------")

My_Fav_Places = ['Canada','Turkey','Swizerland','Maldives','India']

print(My_Fav_Places)

print(sorted(My_Fav_Places))
print(My_Fav_Places)

print(sorted(My_Fav_Places, reverse=True))
print(My_Fav_Places)

My_Fav_Places.reverse()
print(My_Fav_Places)

My_Fav_Places.reverse()
print(My_Fav_Places)


My_Fav_Places.sort()
print(My_Fav_Places)


My_Fav_Places.sort(reverse=True)
print(My_Fav_Places)
